import numpy as np
import matplotlib.pyplot as plt

number_pixels = 100
number_points = 100

edn = 2                                 # electron gain
RN_e = 3                                # read noise electrons
RN = RN_e/edn                           # read noise DN
FW_e = 10**5                            # full well in electrons
FW = FW_e/edn                           # full well in DN
SCALE = number_points / np.log10(FW)    # scale
PN = 0.02                               # fixed patter noise
T = 300                                 # temperature
k1 = 8.62*10**-5                        # Boltzman const
DFM = 0.5                               # Thermal figure of merit
DN = 0.30                               # Dark FPN
PA = (15*10**-4)**2                     # Pixel area
t = 0.01                                # intergration time
Eg = 1.1557-(7.021 * 10**-4 * T**2)/(1108 + T)
DARK_e = t * 2.55*10**15 * PA * DFM * T**1.5 * np.exp(-Eg/(2 * k1 * T))
DARK = DARK_e / edn

C = np.random.normal(0, 1, (number_pixels, 1))
F = np.random.normal(0, 1, (number_pixels, 1))




