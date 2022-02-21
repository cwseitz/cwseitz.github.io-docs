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
eps = 1e-10
print(arr.shape)

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

out = np.zeros((arr.shape[1],3))
for i in range(arr.shape[1]):
    a = arr[a_idx,i]
    b = arr[b_idx,i]
    c = arr[c_idx,i]
    ab = SymmetricKL(a,b)
    bc = SymmetricKL(b,c)
    ac = SymmetricKL(a,c)
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
ax.set_ylabel(r'$D_{KL}(\omega_{x}||\omega_{y})$',fontsize=12)
ax.legend(loc='lower right')

# inset axes....
axins = ax.inset_axes([0.5, 0.5, 0.47, 0.47])
x1, x2, y1, y2 = 0, 10, 0, 1
axins.set_xlim(x1, x2)
axins.set_ylim(y1, y2)
ax.indicate_inset_zoom(axins, edgecolor='gray',alpha=0.5)
axins.plot(out_ab_sorted[:10],color='black',label=r'$\omega_{1},\omega_{2}$')
axins.plot(out_bc_sorted[:10],color='blue',label=r'$\omega_{2},\omega_{3}$')
axins.plot(out_ac_sorted[:10],color='cyan',label=r'$\omega_{1},\omega_{3}$')
axins.set_xlabel('Feature index (sorted)',fontsize=12)
axins.set_ylabel(r'$D_{KL}(\omega_{x}||\omega_{y})$',fontsize=12)
plt.show()

######################################################################
#Visualize some of the conditional distributions for top features
######################################################################

fig, ax = plt.subplots(3,5)

for i in range(5):
    if i == 0:
        ax[0,0].set_ylabel(r'$(\omega_{1},\omega_{2})$')
    name = cols[out_ab_idx[i]]
    xvals,xbins = np.histogram(arr[a_idx,out_ab_idx[i]],bins=10)
    yvals,ybins = np.histogram(arr[b_idx,out_ab_idx[i]],bins=xbins)
    xvals = xvals/np.sum(xvals)
    yvals = yvals/np.sum(yvals)
    ax[0,i].plot(xbins[:-1],xvals,color='red',label=r'$\omega_{1}$')
    ax[0,i].plot(ybins[:-1],yvals,color='blue',label=r'$\omega_{2}$')
    ax[0,i].legend(prop={'size': 6})
    ax[0,i].set_title(name,fontsize=8)

for i in range(5):
    if i == 0:
        ax[1,0].set_ylabel(r'$(\omega_{2},\omega_{3})$',weight='bold')
    name = cols[out_bc_idx[i]]
    xvals,xbins = np.histogram(arr[b_idx,out_bc_idx[i]],bins=10)
    yvals,ybins = np.histogram(arr[c_idx,out_bc_idx[i]],bins=xbins)
    xvals = xvals/np.sum(xvals)
    yvals = yvals/np.sum(yvals)
    ax[1,i].plot(xbins[:-1],xvals,color='red',label=r'$\omega_{2}$')
    ax[1,i].plot(ybins[:-1],yvals,color='blue',label=r'$\omega_{3}$')
    ax[1,i].set_title(name,fontsize=8)
    ax[1,i].legend(prop={'size': 6})

for i in range(5):
    if i == 0:
        ax[2,0].set_ylabel(r'$(\omega_{1},\omega_{3})$')
    name = cols[out_ac_idx[i]]
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
