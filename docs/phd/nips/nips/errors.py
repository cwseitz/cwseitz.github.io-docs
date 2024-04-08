import matplotlib.pyplot as plt

# Data
N0_values = [200, 500, 1000]

xerr = [0.8877236121056422,0.6374707169264318,0.5795656562318549]
txerr = [1.1232689159068578,0.796919385395769,0.7301242902211198]
jaccard = [0.795542261675029,0.8676529388244703,0.8732]
tjaccard = [0.9013712047012733,0.918908149033672,0.9166997223324078]

xerr = [27 * x for x in xerr]
txerr = [27 * y for y in txerr]

# Plotting
fig, axs = plt.subplots(1, 2, figsize=(6, 3))

#axs[0].set_xscale('log')
axs[0].plot(N0_values, jaccard, marker='o', label='Diffusion')
axs[0].plot(N0_values, tjaccard, marker='o', label='DeepSTORM')
axs[0].set_xlabel(r'$N_0$')
axs[0].set_ylabel('Jaccard Index')
axs[0].legend()

# Localization Error
#axs[1].set_xscale('log')
axs[1].plot(N0_values, xerr, marker='o', label='Diffusion')
axs[1].plot(N0_values, txerr, marker='o', label='DeepSTORM')
axs[1].set_xlabel(r'$N_0$')
axs[1].set_ylabel('Localization Error (nm)')
axs[1].legend()
axs[1].set_xticks(N0_values)
axs[1].set_xscale('log')
plt.tight_layout()
plt.show()

