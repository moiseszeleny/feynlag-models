# This file was automatically created by feynlag
import cmath
from object_library import all_parameters, Parameter
from function_library import (complexconjugate, re, im, csc, sec, acsc, asec, cot)


ZERO = Parameter(name='ZERO', nature='internal', type='real', value='0.0', texname='0')

gw = Parameter(name='gw', nature='external', type='real', value=0.65322889878251, texname='gw', lhablock='FEYNLAG', lhacode=[1])
g1 = Parameter(name='g1', nature='external', type='real', value=0.3491928465111313, texname='g1', lhablock='FEYNLAG', lhacode=[2])
gs = Parameter(name='gs', nature='external', type='real', value=1.2177157847767197, texname='gs', lhablock='FEYNLAG', lhacode=[3])
v = Parameter(name='v', nature='external', type='real', value=246.2184581018163, texname='v', lhablock='FEYNLAG', lhacode=[4])
lam = Parameter(name='lam', nature='external', type='real', value=0.1288691060169027, texname='lam', lhablock='FEYNLAG', lhacode=[5])
MT = Parameter(name='MT', nature='external', type='real', value=173.0, texname='MT', lhablock='FEYNLAG', lhacode=[6])
MB = Parameter(name='MB', nature='external', type='real', value=4.7, texname='MB', lhablock='FEYNLAG', lhacode=[7])
MTA = Parameter(name='MTA', nature='external', type='real', value=1.777, texname='MTA', lhablock='FEYNLAG', lhacode=[8])
WZ = Parameter(name='WZ', nature='external', type='real', value=2.4952, texname='WZ', lhablock='FEYNLAG', lhacode=[9])
WW = Parameter(name='WW', nature='external', type='real', value=2.085, texname='WW', lhablock='FEYNLAG', lhacode=[10])
WH = Parameter(name='WH', nature='external', type='real', value=0.00407, texname='WH', lhablock='FEYNLAG', lhacode=[11])
WT = Parameter(name='WT', nature='external', type='real', value=1.4915, texname='WT', lhablock='FEYNLAG', lhacode=[12])

MH = Parameter(name='MH', nature='internal', type='complex', value='cmath.sqrt(2)*cmath.sqrt(lam)*v', texname='MH')
MW = Parameter(name='MW', nature='internal', type='complex', value='(1/2)*gw*v', texname='MW')
MZ = Parameter(name='MZ', nature='internal', type='complex', value='(1/2)*v*cmath.sqrt(g1**2 + gw**2)', texname='MZ')
mu2 = Parameter(name='mu2', nature='internal', type='complex', value='lam*v**2', texname='mu2')
yb = Parameter(name='yb', nature='internal', type='complex', value='cmath.sqrt(2)*MB/v', texname='yb')
yt = Parameter(name='yt', nature='internal', type='complex', value='cmath.sqrt(2)*MT/v', texname='yt')
ytau = Parameter(name='ytau', nature='internal', type='complex', value='cmath.sqrt(2)*MTA/v', texname='ytau')
