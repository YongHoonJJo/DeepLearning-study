import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 6, 0.1)

y = np.sin(x)
plt.plot(x, y, label='sin')

y = np.cos(x)
plt.plot(x, y, linestyle="--", label="cos")

plt.xlabel("x")
plt.ylabel("y")

plt.title('sin & cos')
plt.legend()

plt.show()
