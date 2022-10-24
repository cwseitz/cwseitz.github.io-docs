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
H += np.diag(np.ones((N-1,)),k=1) #upper diagonal
H += np.diag(np.ones((N-1,)),k=-1) #lower diagonal

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

pdf1 = vecs[0]**2
pdf2 = vecs[10]**2
pdf3 = vecs[50]**2

fig, ax = plt.subplots()
ax.plot(pdf1, color='red',label='m=0')
ax.plot(pdf2, color='blue',label='m=10')
ax.plot(pdf3, color='purple',label='m=50')
ax.set_xlabel('x')
ax.set_ylabel(r'$|\phi_{m,n}|^{2}$',fontsize=14)
ax.legend()
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

pdf1 = dvecs[0]**2
pdf2 = dvecs[10]**2
pdf3 = dvecs[50]**2

fig, ax = plt.subplots()
ax.plot(pdf1, color='red',label='m=0')
ax.plot(pdf2, color='blue',label='m=10')
ax.plot(pdf3, color='purple',label='m=50')
ax.set_xlabel('m')
ax.set_ylabel(r'$|\phi_{m,n}|^{2}$',fontsize=14)
ax.legend()
plt.show()



