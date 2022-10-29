import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

###########################################
# Define the Hamiltonian
###########################################

N = 100
#a = hbar/np.sqrt(2*m)
#L = (N-1)*a
V = np.zeros((N,))
H = np.zeros((N,N))
H += np.diag(2 + V,k=0) #main diagonal
H += np.diag(-1*np.ones((N-1,)),k=1) #upper diagonal
H += np.diag(-1*np.ones((N-1,)),k=-1) #lower diagonal

###########################################
# Find eigenvectors and eigenvalues of H
###########################################

vals, vecs = LA.eig(H)
idx = np.argsort(vals)
vecs = vecs[:,idx]
vals = vals[idx]

###########################################
# Show the Hamiltonian
###########################################

fig, ax = plt.subplots(2,2)
x = ax[0,0].imshow(H,cmap='coolwarm')
axin1 = ax[0,0].inset_axes([0.575, 0.575, 0.4, 0.4])
y = axin1.imshow(H[:10,:10],cmap='coolwarm')
plt.colorbar(x,ax=ax[0,0])

###########################################
# Show eigenvectors form an orthonormal set
###########################################

x = ax[0,1].imshow(vecs.T, cmap='coolwarm')
plt.colorbar(x,ax=ax[0,1])
ax[0,1].set_title(r'$T$')
X = vecs.T @ vecs
x = ax[1,0].imshow(X, cmap='coolwarm')
axin1 = ax[1,0].inset_axes([0.575, 0.575, 0.4, 0.4])
y = axin1.imshow(X[:10,:10],cmap='coolwarm')
plt.colorbar(x,ax=ax[1,0])
ax[1,0].set_title(r'$T^{T}T$')

###########################################
# Plot the eigenvalues as a function of n
###########################################


ax[1,1].plot(vals, color='blue')
ax[1,1].set_xlabel('n')
ax[1,1].set_ylabel(r'$\epsilon_{0,n}$',fontsize=14)
ax[1,1].set_aspect(25)
plt.tight_layout()
plt.show()

###########################################
# Plot a few representative prob dists
###########################################

fig, ax = plt.subplots()
pdf1 = vecs[:,0]**2
pdf2 = vecs[:,10]**2
pdf3 = vecs[:,50]**2

ax.plot(pdf1, color='red',label='n=0')
ax.plot(pdf2, color='blue',label='n=10')
ax.plot(pdf3, color='purple',label='n=50')
ax.set_xlabel('x')
ax.set_ylabel(r'$|\phi_{n}|^{2}$',fontsize=14)
ax.legend(loc='upper right')
plt.show()

###########################################
# Find projection operator to energy basis
###########################################

U = LA.inv(vecs)
plt.imshow(U,cmap='coolwarm')
plt.show()

###########################################
# Diagonalize the Hamiltonian
###########################################

Hd = LA.inv(vecs) @ H @ vecs

fig, ax = plt.subplots(2,2)
x = ax[0,0].imshow(Hd,cmap='coolwarm')
axin1 = ax[0,0].inset_axes([0.575, 0.575, 0.4, 0.4])
y = axin1.imshow(Hd[:10,:10],cmap='coolwarm')
plt.colorbar(x,ax=ax[0,0])


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

x = ax[1,0].imshow(dvecs,cmap='coolwarm')
ax[0,1].plot(dvals, color='blue')
ax[0,1].set_xlabel('n')
ax[0,1].set_ylabel(r'$\epsilon_{n}$',fontsize=14)
plt.colorbar(x,ax=ax[1,0])


###########################################
# Plot a few representative prob dists
###########################################

pdf1 = dvecs[:,10]**2
pdf2 = dvecs[:,20]**2
pdf3 = dvecs[:,50]**2

ax[1,1].plot(pdf1, color='red',label='n=10')
ax[1,1].plot(pdf2, color='blue',label='n=20')
ax[1,1].plot(pdf3, color='purple',label='n=50')
ax[1,1].set_xlabel('n')
ax[1,1].set_ylabel(r'$|\phi_{n}|^{2}$',fontsize=14)
ax[1,1].legend()
plt.show()



