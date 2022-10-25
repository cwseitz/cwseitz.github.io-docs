import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

###########################################
# Define the Hamiltonian
###########################################

N = 100
Vl = 2
Vr = 3
t = 1
V = np.zeros((N,))
V[:30] = Vl; V[70:] = Vr
H = np.zeros((N,N))
H += np.diag(2*t + V,k=0) #main diagonal
H += np.diag(-t*np.ones((N-1,)),k=1) #upper diagonal
H += np.diag(-t*np.ones((N-1,)),k=-1) #lower diagonal


###########################################
# Find eigenvectors and eigenvalues of H
###########################################

vals, vecs = LA.eig(H)
idx = np.argsort(vals)
vecs = vecs[:,idx]
vals = vals[idx]

###########################################
# Show the Hamiltonian matrix
###########################################

fig, ax = plt.subplots(1,2)
ax[0].imshow(H,cmap='coolwarm')
ax[1].imshow(H[:10,:10],cmap='coolwarm')
plt.show()

###########################################
# Show eigenvectors form an orthonormal set
###########################################

fig, ax = plt.subplots()
ax.imshow(vecs.T @ vecs, cmap='coolwarm')
plt.show()

###########################################
# Plot the eigenvalues as a function of n
###########################################

fig, ax = plt.subplots()
ax.plot(vals, color='blue')
ax.set_xlabel('n')
ax.set_ylabel(r'$\epsilon_{0,n}$',fontsize=14)
plt.show()

###########################################
# Plot a few representative prob dists
###########################################

pdf1 = vecs[:,0]**2
pdf2 = vecs[:,24]**2
pdf3 = vecs[:,25]**2
pdf4 = vecs[:,34]**2
pdf5 = vecs[:,38]**2
pdf6 = vecs[:,40]**2
pdf7 = vecs[:,54]**2
pdf8 = vecs[:,55]**2

fig, ax = plt.subplots(2,4,sharex=True,figsize=(12,4))
ax[0,0].plot(pdf1, color='red',label='m=0')
ax1 = ax[0,0].twinx()
ax1.plot(V,color='black',label='V(x)')
ax[0,1].plot(pdf2, color='blue',label='m=24')
ax1 = ax[0,1].twinx()
ax1.plot(V,color='black',label='V(x)')
ax[0,2].plot(pdf3, color='purple',label='m=25')
ax1 = ax[0,2].twinx()
ax1.plot(V,color='black',label='V(x)')
ax[0,3].plot(pdf4, color='purple',label='m=34')
ax1 = ax[0,3].twinx()
ax1.plot(V,color='black',label='V(x)')
ax[1,0].plot(pdf5, color='purple',label='m=38')
ax1 = ax[1,0].twinx()
ax1.plot(V,color='black',label='V(x)')
ax[1,1].plot(pdf6, color='purple',label='m=40')
ax1 = ax[1,1].twinx()
ax1.plot(V,color='black',label='V(x)')
ax[1,2].plot(pdf7, color='purple',label='m=54')
ax1 = ax[1,2].twinx()
ax1.plot(V,color='black',label='V(x)')
ax[1,3].plot(pdf8, color='purple',label='m=55')
ax1 = ax[1,3].twinx()
ax1.plot(V,color='black',label='V(x)')
ax[1,0].set_xlabel('n')
ax[1,1].set_xlabel('n')
ax[1,2].set_xlabel('n')
ax[1,3].set_xlabel('n')
ax[0,0].set_ylabel(r'$|\phi_{m,n}|^{2}$',fontsize=14)
ax[1,0].set_ylabel(r'$|\phi_{m,n}|^{2}$',fontsize=14)
#ax1.set_ylabel(r'$V_{n}$')
for _ax in ax.ravel():
    _ax.legend(loc='upper left')
plt.tight_layout()
plt.show()

###########################################
# Find projection operator to energy basis
###########################################

U = LA.inv(vecs)
plt.imshow(U)
plt.show()

###########################################
# Diagonalize the Hamiltonian
###########################################

Hd = LA.inv(vecs) @ H @ vecs
fig, ax = plt.subplots(1,2)
ax[0].imshow(Hd,cmap='coolwarm')
ax[1].imshow(Hd[:10,:10],cmap='coolwarm')
plt.show()

###########################################
# Find eigenvectors and eigenvalues of H
###########################################

dvals, dvecs = LA.eig(Hd)
idx = np.argsort(dvals)
dvecs = dvecs[:,idx]
dvals = dvals[idx]

###########################################
# Plot the eigenvalues as a function of n
###########################################

fig, ax = plt.subplots()
ax.plot(dvals, color='blue')
ax.set_xlabel('n')
ax.set_ylabel(r'$\epsilon_{0,n}$',fontsize=14)
plt.show()

###########################################
# Plot a few representative prob dists
###########################################

pdf1 = dvecs[:,0]**2
pdf2 = dvecs[:,10]**2
pdf3 = dvecs[:,50]**2

fig, ax = plt.subplots()
ax.plot(V,color='black',label='V(x)')
ax.plot(pdf1, color='red',label='m=0')
ax.plot(pdf2, color='blue',label='m=10')
ax.plot(pdf3, color='purple',label='m=50')
ax.set_xlabel('m')
ax.set_ylabel(r'$|\phi_{m,n}|^{2}$',fontsize=14)
ax.legend()
plt.show()



