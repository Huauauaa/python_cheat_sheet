import numpy as np

import matplotlib.pyplot as plt

t = np.arange(0.0, 5.0, 0.2)
plt.plot(t, t, t, t ** 2, t, t ** 3)
# plt.plot(t, t, 'r--', t, t ** 2, 'bs', t, t ** 3, 'g^')
plt.show()

# plt.plot([1, 2, 3, 4])
# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'yo')
# plt.ylabel('some numbers')
# plt.show()
