print("SHERIN MATHEW")
print("21MCA039")

import matplotlib.pyplot as plt
import numpy as np
fig,ax = plt.subplots(1,1)
a=np.array([61, 63, 64, 66, 68, 69, 71, 71.5, 72, 72.5, 73, 73.5, 74, 74.5, 76, 76.2,
76.5, 77, 77.5, 78, 78.5, 79, 79.2, 80, 81, 82, 83, 84, 85, 87.])
plt.hist(a, bins =5)
plt.title("Histogram Result")
plt.show()