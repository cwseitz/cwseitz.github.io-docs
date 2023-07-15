import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import itertools
from sklearn.feature_selection import mutual_info_regression
from scipy.stats import ttest_ind

labels = np.load('/home/cwseitz/Desktop/labels.npy')
a_idx = np.where(labels == 0)
b_idx = np.where(labels == 1)
c_idx = np.where(labels == 2)

print(f'{a_idx[0].shape[0]} entries of type 0')
print(f'{b_idx[0].shape[0]} entries of type 1')
print(f'{c_idx[0].shape[0]} entries of type 2')

df = pd.read_csv('/home/cwseitz/Desktop/features.csv')
cols = df.columns
arr = df.to_numpy()

bins = 20
eps = 1e-10
cond_arr = np.zeros((arr.shape[1],))
marg_arr = np.zeros((arr.shape[1],))

###################################################################
#Quick check on miRNA counts in sample types
###################################################################

mi146 = df['miR146_num'].to_numpy()
mi155 = df['miR155_num'].to_numpy()
t, pval = ttest_ind(mi146[a_idx],mi146[b_idx])
fig, ax = plt.subplots(4,1,sharex=True)
ax[0].hist(mi146[a_idx],bins=25,density=True,color='red',alpha=0.75, label=r'$P(X|\omega_{1})$')
ax[0].set_ylabel('PDF')
ax[0].legend()
ax[1].hist(mi146[b_idx],bins=25,density=True,color='blue',alpha=0.75, label=r'$P(X|\omega_{2})$')
ax[1].set_ylabel('PDF')
ax[1].legend()
ax[2].hist(mi146[c_idx],bins=25,density=True,color='cyan',alpha=0.75, label=r'$P(X|\omega_{3})$')
ax[2].set_ylabel('PDF')
ax[2].legend()
ax[3].hist(mi146,bins=25,density=True,color='purple',alpha=0.75, label=r'$P(X)$')
ax[3].set_ylabel('PDF')
ax[3].set_xlabel('Counts')
ax[3].legend()
plt.show()
