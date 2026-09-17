# This file was automatically created by feynlag
from object_library import all_particles, Particle
import parameters as Param


h = Particle(pdg_code=25, name='h', antiname='h', spin=1, color=1, mass=Param.MH, width=Param.WH, texname='h', antitexname='h', charge=0, goldstoneboson=False)

a = Particle(pdg_code=22, name='a', antiname='a', spin=3, color=1, mass=Param.ZERO, width=Param.ZERO, texname='a', antitexname='a', charge=0, goldstoneboson=False)

Z = Particle(pdg_code=23, name='Z', antiname='Z', spin=3, color=1, mass=Param.MZ, width=Param.WZ, texname='Z', antitexname='Z', charge=0, goldstoneboson=False)

W__plus__ = Particle(pdg_code=24, name='W+', antiname='W-', spin=3, color=1, mass=Param.MW, width=Param.WW, texname='W+', antitexname='W-', charge=1, goldstoneboson=False)
W__minus__ = W__plus__.anti()

u = Particle(pdg_code=2, name='u', antiname='u~', spin=2, color=3, mass=Param.MU, width=Param.ZERO, texname='u', antitexname='u~', charge=2/3, goldstoneboson=False)
u__tilde__ = u.anti()

d = Particle(pdg_code=1, name='d', antiname='d~', spin=2, color=3, mass=Param.MD, width=Param.ZERO, texname='d', antitexname='d~', charge=-1/3, goldstoneboson=False)
d__tilde__ = d.anti()

e__minus__ = Particle(pdg_code=11, name='e-', antiname='e+', spin=2, color=1, mass=Param.ME, width=Param.ZERO, texname='e-', antitexname='e+', charge=-1, goldstoneboson=False)
e__plus__ = e__minus__.anti()

ve = Particle(pdg_code=12, name='ve', antiname='ve~', spin=2, color=1, mass=Param.ZERO, width=Param.ZERO, texname='ve', antitexname='ve~', charge=0, goldstoneboson=False)
ve__tilde__ = ve.anti()

c = Particle(pdg_code=4, name='c', antiname='c~', spin=2, color=3, mass=Param.MC, width=Param.ZERO, texname='c', antitexname='c~', charge=2/3, goldstoneboson=False)
c__tilde__ = c.anti()

s = Particle(pdg_code=3, name='s', antiname='s~', spin=2, color=3, mass=Param.MS, width=Param.ZERO, texname='s', antitexname='s~', charge=-1/3, goldstoneboson=False)
s__tilde__ = s.anti()

mu__minus__ = Particle(pdg_code=13, name='mu-', antiname='mu+', spin=2, color=1, mass=Param.MMU, width=Param.ZERO, texname='mu-', antitexname='mu+', charge=-1, goldstoneboson=False)
mu__plus__ = mu__minus__.anti()

vm = Particle(pdg_code=14, name='vm', antiname='vm~', spin=2, color=1, mass=Param.ZERO, width=Param.ZERO, texname='vm', antitexname='vm~', charge=0, goldstoneboson=False)
vm__tilde__ = vm.anti()

t = Particle(pdg_code=6, name='t', antiname='t~', spin=2, color=3, mass=Param.MT, width=Param.WT, texname='t', antitexname='t~', charge=2/3, goldstoneboson=False)
t__tilde__ = t.anti()

b = Particle(pdg_code=5, name='b', antiname='b~', spin=2, color=3, mass=Param.MB, width=Param.ZERO, texname='b', antitexname='b~', charge=-1/3, goldstoneboson=False)
b__tilde__ = b.anti()

ta__minus__ = Particle(pdg_code=15, name='ta-', antiname='ta+', spin=2, color=1, mass=Param.MTA, width=Param.ZERO, texname='ta-', antitexname='ta+', charge=-1, goldstoneboson=False)
ta__plus__ = ta__minus__.anti()

vt = Particle(pdg_code=16, name='vt', antiname='vt~', spin=2, color=1, mass=Param.ZERO, width=Param.ZERO, texname='vt', antitexname='vt~', charge=0, goldstoneboson=False)
vt__tilde__ = vt.anti()
