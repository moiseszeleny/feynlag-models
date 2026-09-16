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
vS = Parameter(name='vS', nature='external', type='real', value=500.0, texname='vS', lhablock='FEYNLAG', lhacode=[9])
lamS = Parameter(name='lamS', nature='external', type='real', value=0.3, texname='lamS', lhablock='FEYNLAG', lhacode=[10])
lamHS = Parameter(name='lamHS', nature='external', type='real', value=0.1, texname='lamHS', lhablock='FEYNLAG', lhacode=[11])
WZ = Parameter(name='WZ', nature='external', type='real', value=2.4952, texname='WZ', lhablock='FEYNLAG', lhacode=[12])
WW = Parameter(name='WW', nature='external', type='real', value=2.085, texname='WW', lhablock='FEYNLAG', lhacode=[13])
WH = Parameter(name='WH', nature='external', type='real', value=0.00407, texname='WH', lhablock='FEYNLAG', lhacode=[14])
WT = Parameter(name='WT', nature='external', type='real', value=1.4915, texname='WT', lhablock='FEYNLAG', lhacode=[15])
WH2 = Parameter(name='WH2', nature='external', type='real', value=1.0, texname='WH2', lhablock='FEYNLAG', lhacode=[16])

MW = Parameter(name='MW', nature='internal', type='complex', value='(1/2)*gw*v', texname='MW')
MZ = Parameter(name='MZ', nature='internal', type='complex', value='(1/2)*v*cmath.sqrt(g1**2 + gw**2)', texname='MZ')
mu2 = Parameter(name='mu2', nature='internal', type='complex', value='(1/2)*(2*lam*v**2 + lamHS*vS**2)', texname='mu2')
muS2 = Parameter(name='muS2', nature='internal', type='complex', value='-1/2*(lamHS*v**2 + 2*lamS*vS**2)', texname='muS2')
theta = Parameter(name='theta', nature='internal', type='complex', value='(1/2)*cmath.atan(lamHS*v*vS/(lam*v**2 - lamS*vS**2))', texname='theta')
yb = Parameter(name='yb', nature='internal', type='complex', value='cmath.sqrt(2)*MB/v', texname='yb')
yt = Parameter(name='yt', nature='internal', type='complex', value='cmath.sqrt(2)*MT/v', texname='yt')
ytau = Parameter(name='ytau', nature='internal', type='complex', value='cmath.sqrt(2)*MTA/v', texname='ytau')
MH1 = Parameter(name='MH1', nature='internal', type='complex', value='cmath.sqrt(2*lam*v**2*cmath.cos(theta)**2 + 2*lamHS*v*vS*cmath.sin(theta)*cmath.cos(theta) + 2*lamS*vS**2*cmath.sin(theta)**2)', texname='MH1')
MH2 = Parameter(name='MH2', nature='internal', type='complex', value='cmath.sqrt(2*lam*v**2*cmath.sin(theta)**2 - 2*lamHS*v*vS*cmath.sin(theta)*cmath.cos(theta) + 2*lamS*vS**2*cmath.cos(theta)**2)', texname='MH2')
