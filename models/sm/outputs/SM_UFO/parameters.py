# This file was automatically created by feynlag
import cmath
from object_library import all_parameters, Parameter
from function_library import (complexconjugate, re, im, csc, sec, acsc, asec, cot)


ZERO = Parameter(name='ZERO', nature='internal', type='real', value='0.0', texname='0')

gw = Parameter(name='gw', nature='external', type='real', value=0.65322889878251, texname='{g}', lhablock='FEYNLAG', lhacode=[1])
g1 = Parameter(name='g1', nature='external', type='real', value=0.3491928465111313, texname="{g'}", lhablock='FEYNLAG', lhacode=[2])
gs = Parameter(name='gs', nature='external', type='real', value=1.2177157847767197, texname='{g_s}', lhablock='FEYNLAG', lhacode=[3])
v = Parameter(name='v', nature='external', type='real', value=246.2184581018163, texname='{v}', lhablock='FEYNLAG', lhacode=[4])
lam = Parameter(name='lam', nature='external', type='real', value=0.1288691060169027, texname='{\\lambda}', lhablock='FEYNLAG', lhacode=[5])
MT = Parameter(name='MT', nature='external', type='real', value=173.0, texname='{m_t}', lhablock='FEYNLAG', lhacode=[6])
MB = Parameter(name='MB', nature='external', type='real', value=4.7, texname='{m_b}', lhablock='FEYNLAG', lhacode=[7])
MTA = Parameter(name='MTA', nature='external', type='real', value=1.777, texname='{m_\\tau}', lhablock='FEYNLAG', lhacode=[8])
WZ = Parameter(name='WZ', nature='external', type='real', value=2.4952, texname='{\\Gamma_Z}', lhablock='FEYNLAG', lhacode=[9])
WW = Parameter(name='WW', nature='external', type='real', value=2.085, texname='{\\Gamma_W}', lhablock='FEYNLAG', lhacode=[10])
WH = Parameter(name='WH', nature='external', type='real', value=0.00407, texname='{\\Gamma_h}', lhablock='FEYNLAG', lhacode=[11])
WT = Parameter(name='WT', nature='external', type='real', value=1.4915, texname='{\\Gamma_t}', lhablock='FEYNLAG', lhacode=[12])

MH = Parameter(name='MH', nature='internal', type='complex', value='cmath.sqrt(2)*cmath.sqrt(lam)*v', texname='{m_h}')
MW = Parameter(name='MW', nature='internal', type='complex', value='(1/2)*gw*v', texname='{m_W}')
MZ = Parameter(name='MZ', nature='internal', type='complex', value='(1/2)*v*cmath.sqrt(g1**2 + gw**2)', texname='{m_Z}')
mu2 = Parameter(name='mu2', nature='internal', type='complex', value='lam*v**2', texname='{\\mu^2}')
yb = Parameter(name='yb', nature='internal', type='complex', value='cmath.sqrt(2)*MB/v', texname='{y_b}')
yt = Parameter(name='yt', nature='internal', type='complex', value='cmath.sqrt(2)*MT/v', texname='{y_t}')
ytau = Parameter(name='ytau', nature='internal', type='complex', value='cmath.sqrt(2)*MTA/v', texname='{y_\\tau}')
