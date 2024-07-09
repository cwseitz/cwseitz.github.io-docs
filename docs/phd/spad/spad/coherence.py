import numpy as np
import matplotlib.pyplot as plt
from BaseSMLM.generators import Disc2D

def g_squared(N0, hi, hj, xi, B0):
    numerator = xi * hi**2 * hj**2 * N0**2 + xi * N0 * B0 * (hi**2 + hj**2) + B0**2
    denominator = xi**2 * hi**2 * hj**2 * N0**2 + xi * N0 * B0 * (hi**2 + hj**2) + B0**2
    return numerator / denominator

def plot_g_squared_for_xi(ax, xi_values, N0_values, hi, hj, B0):
    for xi in xi_values:
        g_squared_values = [g_squared(N0, hi, hj, xi, B0) for N0 in N0_values]
        ax.plot(N0_values, g_squared_values, label=r'$\xi={}$'.format(xi))

    ax.set_xlabel(r'$N_0$')
    ax.set_ylabel(r'$g^2_{ij}(0)$')
    ax.legend()
    ax.grid(True)

def plot_g_squared_for_xi_fixed_N0(ax, xi_values, N0, hi, hj, B0):
    g_squared_values = [g_squared(N0, hi, hj, xi, B0) for xi in xi_values]
    ax.plot(xi_values, g_squared_values, label=r'$N_0={}$'.format(N0))

    ax.set_xlabel(r'$\xi$')
    ax.set_ylabel(r'$g^2_{ij}(0)$')
    ax.legend()
    ax.grid(True)

generator = Disc2D(10,10)
generator.forward(0.001,1,plot=True)

# Example usage
xi_values = np.linspace(0, 1, 100)
B0 = 1.0
hi = np.sqrt(0.415)
hj = np.sqrt(0.03)
N0_fixed = 5.0
fig,ax=plt.subplots(1,2,figsize=(4,1.5))
plot_g_squared_for_xi_fixed_N0(ax[0], xi_values, N0_fixed, hi, hj, B0)

xi_values = [0.2,0.5,1.0]
N0_values = np.linspace(0,100,100)
plot_g_squared_for_xi(ax[1], xi_values, N0_values, hi, hj, B0)
plt.tight_layout()
plt.show()
