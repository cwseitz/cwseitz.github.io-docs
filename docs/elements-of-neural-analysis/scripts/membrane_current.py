import matplotlib.pyplot as plt
import numpy as np

v = np.linspace(-100, 100, 100)
v_reversal = 50
a = v - v_reversal
g = 1/(1+np.exp(-v))
i = g*a

fig, ax = plt.subplots()
ax.plot(v, a, label="(V-E)")
ax.plot(v, g, label="g")
ax.plot(v, i, label="I")
plt.legend()
plt.show()
