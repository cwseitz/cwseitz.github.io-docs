import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import itertools

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

############################################
#compute mutual information with class label
############################################

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

############################################
#compute redundancy for each feature
############################################

n = arr.shape[1]
info_mat = np.zeros((n,n))

for i in range(n):
    for j in range(n):

        #compute marginal entropy
        vals, edges = np.histogram(arr[:,i],bins=bins)
        vals = vals/np.sum(vals)
        vals = vals[np.argwhere(vals > eps)]
        marg_entropy = np.sum(vals*np.log2(1/vals)) #nats

        #compute joint entropy
        vals, xedges, yedges = np.histogram2d(arr[:,i],arr[:,j],bins=bins)
        vals = vals/np.sum(vals)
        vals = vals.flatten()
        vals = vals[np.argwhere(vals > eps)]
        jont_entropy = np.sum(vals*np.log2(1/vals)) #nats
        cond_entropy = jont_entropy - marg_entropy
        info_mat[i,j] = marg_entropy - cond_entropy

fig, ax = plt.subplots(1,2)
ax[0].scatter(cond_arr,marg_arr,color='black',s=2)
ax[0].set_xlabel('H(X|Y)',weight='bold')
ax[0].set_ylabel('H(X)', weight='bold')
ax[0].set_title('Feature, Class Information')

im = ax[1].imshow(info_mat,cmap='hot')
ax[1].set_title('Feature, Feature Information')
ax[1].set_xlabel('Feature Index')
ax[1].set_ylabel('Feature Index')
plt.colorbar(im, ax=ax[1], label='Information (bits)')
plt.tight_layout()
plt.show()
