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
print(cols.to_numpy())
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
ax[0].hist(mi146[a_idx],bins=25,density=True,color='red',alpha=0.75)
ax[1].hist(mi146[b_idx],bins=25,density=True,color='blue',alpha=0.75)
ax[2].hist(mi146[c_idx],bins=25,density=True,color='cyan',alpha=0.75)
ax[3].hist(mi146,bins=25,density=True,color='purple',alpha=0.75)
#plt.title(f'{pval}')
plt.show()
fig, ax = plt.subplots(4,1,sharex=True)
t, pval = ttest_ind(mi155[a_idx],mi155[b_idx])
ax[0].hist(mi155[a_idx],bins=25,density=True,color='red',alpha=0.75)
ax[1].hist(mi155[b_idx],bins=25,density=True,color='blue',alpha=0.75)
ax[2].hist(mi155[c_idx],bins=25,density=True,color='cyan',alpha=0.75)
ax[3].hist(mi155,bins=25,density=True,color='purple',alpha=0.75)
#plt.title(f'{pval}')
plt.show()

###################################################################
#compute mutual information with class label using histogram method
###################################################################

for i in range(arr.shape[1]):

    #compute marginal entropy
    vals, edges = np.histogram(arr[:,i],bins=bins)
    vals = vals/np.sum(vals)
    vals = vals[np.argwhere(vals > eps)]
    marg_entropy = np.sum(vals*np.log2(1/vals)) #nats

    #compute conditional entropy
    a_vals, a_edges = np.histogram(arr[a_idx,i],bins=edges)
    b_vals, b_edges = np.histogram(arr[b_idx,i],bins=edges)
    c_vals, c_edges = np.histogram(arr[c_idx,i],bins=edges)

    a_vals = a_vals/np.sum(a_vals)
    b_vals = b_vals/np.sum(b_vals)
    c_vals = c_vals/np.sum(c_vals)

    a_vals = a_vals[np.argwhere(a_vals > eps)]
    b_vals = b_vals[np.argwhere(b_vals > eps)]
    c_vals = c_vals[np.argwhere(c_vals > eps)]

    a_ent = -1*np.sum(a_vals*np.log2(a_vals))
    b_ent = -1*np.sum(b_vals*np.log2(b_vals))
    c_ent = -1*np.sum(c_vals*np.log2(c_vals))

    cond_entropy = (a_ent + b_ent + c_ent)/3
    cond_arr[i] = cond_entropy
    marg_arr[i] = marg_entropy


mi_hst = marg_arr - cond_arr
mi_hst = np.clip(mi_hst,0,None)

####################################################################
#compute mutual information with class label using k-neighbor method
####################################################################

mi_kn = mutual_info_regression(arr,labels,discrete_features=False)
mi_kn_idx = np.flip(np.argsort(mi_kn)) #descending information
ordered_labels = cols[mi_kn_idx]
ordered_info = mi_kn[mi_kn_idx]

############################################
#compute redundancy for each feature
############################################

# n = arr.shape[1]
# info_mat = np.zeros((n,n))
#
# for i in range(n):
#     for j in range(n):
#
#         #compute marginal entropy
#         vals, edges = np.histogram(arr[:,i],bins=bins)
#         vals = vals/np.sum(vals)
#         vals = vals[np.argwhere(vals > eps)]
#         marg_entropy = np.sum(vals*np.log2(1/vals)) #nats
#
#         #compute joint entropy
#         vals, xedges, yedges = np.histogram2d(arr[:,i],arr[:,j],bins=bins)
#         vals = vals/np.sum(vals)
#         vals = vals.flatten()
#         vals = vals[np.argwhere(vals > eps)]
#         jont_entropy = np.sum(vals*np.log2(1/vals)) #nats
#         cond_entropy = jont_entropy - marg_entropy
#         info_mat[i,j] = marg_entropy - cond_entropy

fig, ax = plt.subplots(1,2)
ax[0].scatter(cond_arr,marg_arr,color='black',s=2)
ax[0].set_xlabel('H(X|Y)',fontsize=12)
ax[0].set_ylabel('H(X)',fontsize=12)

ax[1].hist(mi_kn,bins=10,color='black')
ax[1].set_xlabel('Information (bits)',fontsize=12)

plt.tight_layout()
plt.show()
