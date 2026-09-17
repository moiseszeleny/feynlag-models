"""The objects every ``models/<id>/model.py`` produces.

``SMPieces`` is the *parent* object a child mutates before assembling the
feynlag ``Model`` (parent + delta); ``ModelBundle`` is what ``build()`` returns
and what tests, output scripts and the UFO exporter consume.
"""

from dataclasses import dataclass, field

import sympy as sp

from feynlag.export.ufo import UFOParticle  # noqa: F401  (re-exported for models)


@dataclass
class DiracSpec:
    """A Dirac fermion assembled from two Weyl fields, for export/flattening.

    Attributes:
        name: UFO particle name (``'t'``, ``'ta-'``, …).
        left, right: the ``IndexedBase`` components (gauge-component level; the
            first colour slot for quarks — colour is diagonal).
        particle, antiparticle: plain symbols used in UFO vertex tables.
        pdg, charge, color, mass: UFO attributes (``mass`` = parameter name).
        antiname: UFO antiparticle name.
    """

    name: str
    left: object
    right: object
    particle: sp.Symbol
    antiparticle: sp.Symbol
    pdg: int
    charge: float
    mass: str
    antiname: str
    color: int = 1
    width: str = "ZERO"
    #: further colour copies (IndexedBases) whose vertices duplicate the first
    #: slot and are therefore skipped silently by the UFO flattener
    copies: tuple = ()
    #: integer flavour index when several generations share one IndexedBase;
    #: ``None`` for the single-generation models (symbolic flavour index)
    flavor: int = None

    @property
    def ignored_bases(self):
        from feynlag import bar_partner
        out = set()
        for base in self.copies:
            out.add(base)
            out.add(bar_partner(base))
        return out

    @property
    def bases(self):
        """``{IndexedBase: symbol}`` for both field and bar legs; the keys are
        ``(IndexedBase, flavor)`` pairs when ``flavor`` is set."""
        from feynlag import bar_partner
        out = {}
        for base in (self.left, self.right):
            if base is None:
                continue
            key = (lambda b: b) if self.flavor is None else (lambda b: (b, self.flavor))
            out[key(base)] = self.particle
            out[key(bar_partner(base))] = self.antiparticle
        return out

    def ufo_particle(self):
        return UFOParticle(self.particle, self.pdg, self.name, antiname=self.antiname,
                           spin=2, charge=self.charge, mass=self.mass,
                           width=self.width, color=self.color,
                           antisymbol=self.antiparticle)


@dataclass
class SMPieces:
    """Everything the SM root declares *before* the ``Model`` is assembled."""

    SU2L: object
    U1Y: object
    SU3c: object
    gw: object
    g1: object
    gs: object
    W: object
    B: object
    G: object
    idx: tuple                          # (i, j) flavour index symbols
    fermions: dict                      # name → WeylFermion (Ll, eR, QL, uR, dR)
    params: list                        # ExternalParameter/InternalParameter, dependency-safe
    fields: list                        # every Field to hand to Model
    terms: list                         # (expr, sector, name)
    yukawa: dict = field(default_factory=dict)   # name → Lagrangian expr (for mass matrices)
    ew: object = None                   # ElectroweakScaffold when higgs=True
    benchmark: dict = field(default_factory=dict)
    discrete_groups: list = field(default_factory=list)
    generations: int = 1                # 1 (third generation only) or 3

    @property
    def gauge_groups(self):
        return [self.SU2L, self.U1Y, self.SU3c]

    def add_term(self, expr, sector, name):
        self.terms.append((expr, sector, name))

    def replace_term(self, name, expr):
        """Swap the expression of the term called ``name`` (sector kept)."""
        for k, (_expr, sector, n) in enumerate(self.terms):
            if n == name:
                self.terms[k] = (expr, sector, name)
                return
        raise KeyError(name)

    def lagrangian(self):
        from feynlag import Lagrangian
        L = Lagrangian()
        for expr, sector, name in self.terms:
            L.add(expr, sector=sector, name=name)
        return L


@dataclass
class ModelBundle:
    """What ``build()`` returns."""

    id: str
    model: object                       # feynlag Model, tadpoles solved, rotations registered
    pieces: SMPieces
    bosons: dict                        # name → physical boson symbol
    cmap: dict                          # {conjugate(sym): partner}
    charges: dict                       # {physical boson symbol: electric charge}
    conjugates: dict                    # full antiparticle map for hermiticity pairing
    params: object                      # ParameterSet including mass/angle internals (UFO)
    benchmark: dict                     # name → number (from metadata.yaml)
    dirac: list                         # [DiracSpec]
    boson_particles: list               # [UFOParticle] for the bosons (physical + Goldstone)
    goldstones: tuple = ()              # boson symbols to drop from a unitary-gauge export
    extra: dict = field(default_factory=dict)   # model-specific handles (rotations, angles, …)

    # ------------------------------------------------------------ helpers
    @property
    def boson_list(self):
        return list(self.bosons.values())

    def values(self):
        """``{symbol: number}`` for every parameter at the benchmark."""
        return self.params.numeric()

    def physical_fermion_lagrangian(self):
        """Yukawa + gauge sectors in the physical basis, conjugates normalised."""
        L = (self.model.physical_lagrangian(sector="yukawa")
             + self.model.physical_lagrangian(sector="gauge"))
        return sp.expand(L.xreplace(self.cmap))

    def fermion_table(self):
        from feynlag import extract_fermion_vertices
        return extract_fermion_vertices(self.physical_fermion_lagrangian(),
                                        self.boson_list)

    def ufo_particles(self):
        return list(self.boson_particles) + [d.ufo_particle() for d in self.dirac]
