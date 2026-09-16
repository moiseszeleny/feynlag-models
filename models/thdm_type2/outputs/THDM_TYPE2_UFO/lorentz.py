# This file was automatically created by feynlag
from object_library import all_lorentz, Lorentz


FFSL = Lorentz(name='FFSL', spins=[2, 2, 1], structure='ProjM(2,1)')
FFSR = Lorentz(name='FFSR', spins=[2, 2, 1], structure='ProjP(2,1)')
FFVL = Lorentz(name='FFVL', spins=[2, 2, 3], structure='Gamma(3,2,-1)*ProjM(-1,1)')
FFVR = Lorentz(name='FFVR', spins=[2, 2, 3], structure='Gamma(3,2,-1)*ProjP(-1,1)')
SSS1 = Lorentz(name='SSS1', spins=[1, 1, 1], structure='1')
SSSS1 = Lorentz(name='SSSS1', spins=[1, 1, 1, 1], structure='1')
VSS1 = Lorentz(name='VSS1', spins=[3, 1, 1], structure='P(1,2) - P(1,3)')
VVS1 = Lorentz(name='VVS1', spins=[3, 3, 1], structure='Metric(1,2)')
VVSS1 = Lorentz(name='VVSS1', spins=[3, 3, 1, 1], structure='Metric(1,2)')
VVV1 = Lorentz(name='VVV1', spins=[3, 3, 3], structure='P(3,1)*Metric(1,2) - P(3,2)*Metric(1,2) + P(2,3)*Metric(1,3) - P(2,1)*Metric(1,3) + P(1,2)*Metric(2,3) - P(1,3)*Metric(2,3)')
