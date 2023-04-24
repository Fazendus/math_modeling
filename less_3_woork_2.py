import numpy as np
import less_2_phys_module as pm

h = 100
a = np.pi /3
B = np.deg2rad(30)
g = pm.g

k = g * h * np.tan(B / 2) ** 2 * np.cos(a) ** 2 * (1 - np.tan(a) ** 2 / np.tan(B / 2) ** 2)
print(k)