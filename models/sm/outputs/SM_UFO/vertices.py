# This file was automatically created by feynlag
from object_library import all_vertices, Vertex
import particles as P
import couplings as C
import lorentz as L


V_1 = Vertex(name='V_1',
    particles=[P.h, P.h, P.h, P.h],
    color=['1'],
    lorentz=[L.SSSS1],
    couplings={(0,0):C.GC_1})

V_2 = Vertex(name='V_2',
    particles=[P.h, P.h, P.h],
    color=['1'],
    lorentz=[L.SSS1],
    couplings={(0,0):C.GC_2})

V_3 = Vertex(name='V_3',
    particles=[P.W__minus__, P.W__plus__, P.h, P.h],
    color=['1'],
    lorentz=[L.VVSS1],
    couplings={(0,0):C.GC_3})

V_4 = Vertex(name='V_4',
    particles=[P.Z, P.Z, P.h, P.h],
    color=['1'],
    lorentz=[L.VVSS1],
    couplings={(0,0):C.GC_4})

V_5 = Vertex(name='V_5',
    particles=[P.W__minus__, P.W__plus__, P.h],
    color=['1'],
    lorentz=[L.VVS1],
    couplings={(0,0):C.GC_5})

V_6 = Vertex(name='V_6',
    particles=[P.Z, P.Z, P.h],
    color=['1'],
    lorentz=[L.VVS1],
    couplings={(0,0):C.GC_6})

V_7 = Vertex(name='V_7',
    particles=[P.W__minus__, P.W__plus__, P.Z],
    color=['1'],
    lorentz=[L.VVV1],
    couplings={(0,0):C.GC_7})

V_8 = Vertex(name='V_8',
    particles=[P.a, P.W__minus__, P.W__plus__],
    color=['1'],
    lorentz=[L.VVV1],
    couplings={(0,0):C.GC_8})

V_9 = Vertex(name='V_9',
    particles=[P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__],
    color=['1', '1'],
    lorentz=[L.VVVV2, L.VVVV3],
    couplings={(0,0):C.GC_9, (1,1):C.GC_9})

V_10 = Vertex(name='V_10',
    particles=[P.W__minus__, P.W__plus__, P.Z, P.Z],
    color=['1', '1'],
    lorentz=[L.VVVV2, L.VVVV3],
    couplings={(0,0):C.GC_10, (1,1):C.GC_10})

V_11 = Vertex(name='V_11',
    particles=[P.a, P.W__minus__, P.W__plus__, P.Z],
    color=['1', '1'],
    lorentz=[L.VVVV1, L.VVVV2],
    couplings={(0,0):C.GC_11, (1,1):C.GC_11})

V_12 = Vertex(name='V_12',
    particles=[P.a, P.a, P.W__minus__, P.W__plus__],
    color=['1', '1'],
    lorentz=[L.VVVV2, L.VVVV3],
    couplings={(0,0):C.GC_12, (1,1):C.GC_12})

V_13 = Vertex(name='V_13',
    particles=[P.b__tilde__, P.b, P.a],
    color=['Identity(1,2)'],
    lorentz=[L.FFVL, L.FFVR],
    couplings={(0,0):C.GC_13, (0,1):C.GC_13})

V_14 = Vertex(name='V_14',
    particles=[P.b__tilde__, P.b, P.Z],
    color=['Identity(1,2)'],
    lorentz=[L.FFVL, L.FFVR],
    couplings={(0,0):C.GC_14, (0,1):C.GC_15})

V_15 = Vertex(name='V_15',
    particles=[P.ta__plus__, P.ta__minus__, P.a],
    color=['1'],
    lorentz=[L.FFVL, L.FFVR],
    couplings={(0,0):C.GC_16, (0,1):C.GC_16})

V_16 = Vertex(name='V_16',
    particles=[P.ta__plus__, P.ta__minus__, P.Z],
    color=['1'],
    lorentz=[L.FFVL, L.FFVR],
    couplings={(0,0):C.GC_17, (0,1):C.GC_18})

V_17 = Vertex(name='V_17',
    particles=[P.t__tilde__, P.t, P.a],
    color=['Identity(1,2)'],
    lorentz=[L.FFVL, L.FFVR],
    couplings={(0,0):C.GC_19, (0,1):C.GC_19})

V_18 = Vertex(name='V_18',
    particles=[P.t__tilde__, P.t, P.Z],
    color=['Identity(1,2)'],
    lorentz=[L.FFVL, L.FFVR],
    couplings={(0,0):C.GC_20, (0,1):C.GC_21})

V_19 = Vertex(name='V_19',
    particles=[P.b__tilde__, P.b, P.h],
    color=['Identity(1,2)'],
    lorentz=[L.FFSL, L.FFSR],
    couplings={(0,0):C.GC_22, (0,1):C.GC_22})

V_20 = Vertex(name='V_20',
    particles=[P.t__tilde__, P.t, P.h],
    color=['Identity(1,2)'],
    lorentz=[L.FFSL, L.FFSR],
    couplings={(0,0):C.GC_23, (0,1):C.GC_23})

V_21 = Vertex(name='V_21',
    particles=[P.ta__plus__, P.ta__minus__, P.h],
    color=['1'],
    lorentz=[L.FFSL, L.FFSR],
    couplings={(0,0):C.GC_24, (0,1):C.GC_24})

V_22 = Vertex(name='V_22',
    particles=[P.b__tilde__, P.t, P.W__minus__],
    color=['Identity(1,2)'],
    lorentz=[L.FFVL],
    couplings={(0,0):C.GC_25})

V_23 = Vertex(name='V_23',
    particles=[P.ta__plus__, P.vt, P.W__minus__],
    color=['1'],
    lorentz=[L.FFVL],
    couplings={(0,0):C.GC_25})

V_24 = Vertex(name='V_24',
    particles=[P.vt__tilde__, P.ta__minus__, P.W__plus__],
    color=['1'],
    lorentz=[L.FFVL],
    couplings={(0,0):C.GC_25})

V_25 = Vertex(name='V_25',
    particles=[P.t__tilde__, P.b, P.W__plus__],
    color=['Identity(1,2)'],
    lorentz=[L.FFVL],
    couplings={(0,0):C.GC_25})

V_26 = Vertex(name='V_26',
    particles=[P.vt__tilde__, P.vt, P.Z],
    color=['1'],
    lorentz=[L.FFVL],
    couplings={(0,0):C.GC_26})
