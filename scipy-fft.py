# import scipy and numpy
import scipy
import numpy as np
from scipy.fft import fft



x = np.array(np.arange(10))
print(x)
# Using scipy.fft() method
gfg = fft(x)

print(gfg)
