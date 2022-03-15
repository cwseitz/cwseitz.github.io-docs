import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import itertools

label_path = '/home/cwseitz/Desktop/labels.npy'
labels = np.load(label_path)
a_idx = np.where(labels == 0)
b_idx = np.where(labels == 1)
c_idx = np.where(labels == 2)

#print(f'{a_idx[0].shape[0]} entries of type 0')
#print(f'{b_idx[0].shape[0]} entries of type 1')
#print(f'{c_idx[0].shape[0]} entries of type 2')

feature_path = '/home/cwseitz/Desktop/features.csv'
df = pd.read_csv(feature_path)
cols = df.columns
arr = df.to_numpy()
eps = 1e-10

######################################################################
#Compute the symmetric KL-divergence between conditional distributions
######################################################################

def SymmetricKL(x,y,bins=10,eps=1e-10):

    xvals,xbins = np.histogram(x,bins=bins)
    yvals,ybins = np.histogram(y,bins=xbins)
    xvals = xvals/np.sum(xvals)
    yvals = yvals/np.sum(yvals)
    xidx = np.argwhere(xvals > eps)
    yidx = np.argwhere(yvals > eps)
    idx = np.intersect1d(xidx,yidx)
    xvals = xvals[idx]; yvals = yvals[idx]
    kl_xy = np.sum(xvals*np.log2(xvals/yvals))
    kl_yx = np.sum(yvals*np.log2(yvals/xvals))
    kl = kl_xy + kl_yx

    return kl

num_top = 10
out = np.zeros((arr.shape[1],3))
for i in range(arr.shape[1]):
    a = arr[a_idx,i]
    b = arr[b_idx,i]
    c = arr[c_idx,i]
    ab = SymmetricKL(a,b,eps=eps)
    bc = SymmetricKL(b,c,eps=eps)
    ac = SymmetricKL(a,c,eps=eps)
    out[i,:] = np.array([ab,bc,ac])

out_ab_idx = np.flip(np.argsort(out[:,0]))
out_bc_idx = np.flip(np.argsort(out[:,1]))
out_ac_idx = np.flip(np.argsort(out[:,2]))

out_ab_sorted = out[out_ab_idx,0]
out_bc_sorted = out[out_bc_idx,1]
out_ac_sorted = out[out_ac_idx,2]

fig, ax = plt.subplots()
ax.plot(out_ab_sorted,color='black',label=r'$\omega_{1},\omega_{2}$')
ax.plot(out_bc_sorted,color='blue',label=r'$\omega_{2},\omega_{3}$')
ax.plot(out_ac_sorted,color='cyan',label=r'$\omega_{1},\omega_{3}$')
ax.set_xlabel('Feature index (sorted)',fontsize=12)
ax.set_ylabel(r'$S_{ij}$',fontsize=12)
ax.legend(loc='lower right')

# inset axes....
axins = ax.inset_axes([0.5, 0.5, 0.47, 0.47])
x1, x2, y1, y2 = 0, num_top-1, 0, 1
axins.set_xlim(x1, x2)
axins.set_ylim(y1, y2)
ax.indicate_inset_zoom(axins, edgecolor='gray',alpha=0.5)
axins.plot(out_ab_sorted[:num_top],color='black',label=r'$\omega_{1},\omega_{2}$')
axins.plot(out_bc_sorted[:num_top],color='blue',label=r'$\omega_{2},\omega_{3}$')
axins.plot(out_ac_sorted[:num_top],color='cyan',label=r'$\omega_{1},\omega_{3}$')
axins.set_xlabel('Feature index (sorted)',fontsize=12)
axins.set_ylabel(r'$S_{ij}$',fontsize=12)
plt.show()

######################################################################
#Visualize some of the conditional distributions for top features
######################################################################


import csv
f = open('top.csv', 'w', newline='')
writer = csv.writer(f)
writer.writerow(['pair','feature_idx','skld','feature_name'])
fig, ax = plt.subplots(3,num_top)

print('\n#############\na,b\n#############\n')
for i in range(num_top):
    if i == 0:
        ax[0,0].set_ylabel(r'$(\omega_{1},\omega_{2})$')
    name = cols[out_ab_idx[i]]
    print(out_ab_idx[i],name)
    writer.writerow(['ab',out_ab_idx[i], out[out_ab_idx[i],0], name])
    xvals,xbins = np.histogram(arr[a_idx,out_ab_idx[i]],bins=10)
    yvals,ybins = np.histogram(arr[b_idx,out_ab_idx[i]],bins=xbins)
    xvals = xvals/np.sum(xvals)
    yvals = yvals/np.sum(yvals)
    ax[0,i].plot(xbins[:-1],xvals,color='red',label=r'$\omega_{1}$')
    ax[0,i].plot(ybins[:-1],yvals,color='blue',label=r'$\omega_{2}$')
    ax[0,i].legend(prop={'size': 6})
    ax[0,i].set_title(name,fontsize=8)


print('\n#############\nb,c\n#############\n')
for i in range(num_top):
    if i == 0:
        ax[1,0].set_ylabel(r'$(\omega_{2},\omega_{3})$',weight='bold')
    name = cols[out_bc_idx[i]]
    print(out_bc_idx[i],name) 
    writer.writerow(['bc',out_bc_idx[i], out[out_bc_idx[i],1], name])
    xvals,xbins = np.histogram(arr[a_idx,out_ab_idx[i]],bins=10)
    xvals,xbins = np.histogram(arr[a_idx,out_ab_idx[i]],bins=10)
    xvals,xbins = np.histogram(arr[b_idx,out_bc_idx[i]],bins=10)
    yvals,ybins = np.histogram(arr[c_idx,out_bc_idx[i]],bins=xbins)
    xvals = xvals/np.sum(xvals)
    yvals = yvals/np.sum(yvals)
    ax[1,i].plot(xbins[:-1],xvals,color='red',label=r'$\omega_{2}$')
    ax[1,i].plot(ybins[:-1],yvals,color='blue',label=r'$\omega_{3}$')
    ax[1,i].set_title(name,fontsize=8)
    ax[1,i].legend(prop={'size': 6})


print('\n#############\na,c\n#############\n')
for i in range(num_top):
    if i == 0:
        ax[2,0].set_ylabel(r'$(\omega_{1},\omega_{3})$')
    name = cols[out_ac_idx[i]]
    print(out_ac_idx[i],name)  
    writer.writerow(['ac',out_ac_idx[i], out[out_ac_idx[i],2], name])
    xvals,xbins = np.histogram(arr[a_idx,out_ab_idx[i]],bins=10)
    xvals,xbins = np.histogram(arr[a_idx,out_ab_idx[i]],bins=10)
    xvals,xbins = np.histogram(arr[a_idx,out_ac_idx[i]],bins=10)
    yvals,ybins = np.histogram(arr[c_idx,out_ac_idx[i]],bins=xbins)
    xvals = xvals/np.sum(xvals)
    yvals = yvals/np.sum(yvals)
    ax[2,i].plot(xbins[:-1],xvals,color='red',label=r'$\omega_{1}$')
    ax[2,i].plot(ybins[:-1],yvals,color='blue',label=r'$\omega_{3}$')
    ax[2,i].set_title(name,fontsize=8)
    ax[2,i].legend(prop={'size': 6})

plt.tight_layout()
plt.show()
f.close()

"""
#############################################################################
#Plot the covariance matrices for each sample type 
#############################################################################

pd.plotting.scatter_matrix(df[cols[1:20]], alpha = 0.2, figsize = (6, 6), diagonal = 'kde')
plt.show()

#rescale the data to zero mean unit variance

mu = np.mean(arr, axis=0)
std = np.mean(arr, axis=0)

for i in range(arr.shape[1]):
    arr[:,i] -= mu[i]
    arr[:,i] /= std[i]

a_cov = np.corrcoef(arr[a_idx].T)
b_cov = np.corrcoef(arr[b_idx].T)
c_cov = np.corrcoef(arr[c_idx].T)

fig, ax = plt.subplots(1,3)
ax[0].imshow(a_cov,cmap='hot')
ax[1].imshow(b_cov,cmap='hot')
ax[2].imshow(c_cov,cmap='hot')
plt.tight_layout()
plt.show()
"""
