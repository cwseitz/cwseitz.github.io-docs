import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

###########################################
# Define the Hamiltonian H0
###########################################

N = 100 #Number of samples
V = np.zeros((N,)) #Potential
H0 = np.zeros((N,N)) #Hamiltonian matrix H0
H0 += np.diag(2 + V,k=0) #main diagonal
H0 += np.diag(-1*np.ones((N-1,)),k=1) #upper diagonal
H0 += np.diag(-1*np.ones((N-1,)),k=-1) #lower diagonal

###########################################
# Find eigenvectors and eigenvalues of H0
###########################################

vals, vecs = LA.eig(H0)
idx = np.argsort(vals)
vecs = vecs[:,idx]
vals = vals[idx]

###########################################
# Show H0
###########################################

fig, ax = plt.subplots(2,2) #Figure 1
x = ax[0,0].imshow(H0,cmap='coolwarm')
axin1 = ax[0,0].inset_axes([0.575, 0.575, 0.4, 0.4])
y = axin1.imshow(H0[:10,:10],cmap='coolwarm')
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
ax[1,1].set_ylabel(r'$\epsilon_{n}$',fontsize=14)
plt.tight_layout()
ax[0,0].text(-0.1, 1.1, 'A', transform=ax[0,0].transAxes, 
            size=10, weight='bold')
ax[0,1].text(-0.1, 1.1, 'B', transform=ax[0,1].transAxes, 
            size=10, weight='bold')
ax[1,0].text(-0.1, 1.1, 'C', transform=ax[1,0].transAxes, 
            size=10, weight='bold')
ax[1,1].text(-0.1, 1.1, 'D', transform=ax[1,1].transAxes, 
            size=10, weight='bold')
plt.show()

###########################################
# Plot a few representative prob dists
###########################################

fig, ax = plt.subplots() #Figure 2
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

U0 = LA.inv(vecs)

###########################################
# Diagonalize H0
###########################################

Hd = U0 @ H0 @ LA.inv(U0)

fig, ax = plt.subplots(2,2) #Figure 3
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
ax[0,0].text(-0.1, 1.1, 'A', transform=ax[0,0].transAxes, 
            size=10, weight='bold')
ax[0,1].text(-0.1, 1.1, 'B', transform=ax[0,1].transAxes, 
            size=10, weight='bold')
ax[1,0].text(-0.1, 1.1, 'C', transform=ax[1,0].transAxes, 
            size=10, weight='bold')
ax[1,1].text(-0.1, 1.1, 'D', transform=ax[1,1].transAxes, 
            size=10, weight='bold')
plt.show()

###########################################
# Define the Hamiltonian H
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

fig, ax = plt.subplots(2,2) #Figure 4
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
ax[1,1].set_ylabel(r'$\epsilon_{n}$',fontsize=14)
ax[1,1].set_aspect(15)
ax[0,0].text(-0.1, 1.1, 'A', transform=ax[0,0].transAxes, 
            size=10, weight='bold')
ax[0,1].text(-0.1, 1.1, 'B', transform=ax[0,1].transAxes, 
            size=10, weight='bold')
ax[1,0].text(-0.1, 1.1, 'C', transform=ax[1,0].transAxes, 
            size=10, weight='bold')
ax[1,1].text(-0.1, 1.1, 'D', transform=ax[1,1].transAxes, 
            size=10, weight='bold')
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

fig, ax = plt.subplots(4,2,sharex=True,figsize=(12,4)) #Figure 5
ax[0,0].plot(pdf1, color='red',label='m=0')
ax1 = ax[0,0].twinx()
ax1.plot(V,color='black',label='V(x)')
ax[1,0].plot(pdf2, color='blue',label='m=24')
ax1 = ax[1,0].twinx()
ax1.plot(V,color='black',label='V(x)')
ax[2,0].plot(pdf3, color='purple',label='m=25')
ax1 = ax[2,0].twinx()
ax1.plot(V,color='black',label='V(x)')
ax[3,0].plot(pdf4, color='purple',label='m=34')
ax1 = ax[3,0].twinx()
ax1.plot(V,color='black',label='V(x)')
ax[0,1].plot(pdf5, color='purple',label='m=38')
ax1 = ax[0,1].twinx()
ax1.plot(V,color='black',label='V(x)')
ax[1,1].plot(pdf6, color='purple',label='m=40')
ax1 = ax[1,1].twinx()
ax1.plot(V,color='black',label='V(x)')
ax[2,1].plot(pdf7, color='purple',label='m=54')
ax1 = ax[2,1].twinx()
ax1.plot(V,color='black',label='V(x)')
ax[3,1].plot(pdf8, color='purple',label='m=55')
ax1 = ax[3,1].twinx()
ax1.plot(V,color='black',label='V(x)')
ax[0,1].set_xlabel('n')
ax[1,1].set_xlabel('n')
ax[2,1].set_xlabel('n')
ax[3,1].set_xlabel('n')
ax[0,0].set_ylabel(r'$|\phi_{0}|^{2}$',fontsize=14)
ax[0,1].set_ylabel(r'$|\phi_{38}|^{2}$',fontsize=14)
ax[1,0].set_ylabel(r'$|\phi_{24}|^{2}$',fontsize=14)
ax[1,1].set_ylabel(r'$|\phi_{40}|^{2}$',fontsize=14)
ax[2,0].set_ylabel(r'$|\phi_{25}|^{2}$',fontsize=14)
ax[2,1].set_ylabel(r'$|\phi_{54}|^{2}$',fontsize=14)
ax[3,0].set_ylabel(r'$|\phi_{34}|^{2}$',fontsize=14)
ax[3,1].set_ylabel(r'$|\phi_{55}|^{2}$',fontsize=14)

plt.tight_layout()
plt.show()


###########################################
# Apply U0 to H
###########################################

H_ = U0 @ H @ LA.inv(U0)

###########################################
# Show the result
###########################################

fig, ax = plt.subplots(1,3) #Figure 6
x = ax[0].imshow(H_,cmap='coolwarm')
axin1 = ax[0].inset_axes([0.575, 0.575, 0.4, 0.4])
y = axin1.imshow(H_[:10,:10],cmap='coolwarm')
plt.colorbar(x,ax=ax[0])


###########################################
# Find eigenvectors and eigenvalues of H
###########################################

vals, vecs = LA.eig(H_)
idx = np.argsort(vals)
vecs = vecs[:,idx]
vals = vals[idx]

###########################################
# Plot the eigenvalues as a function of n
###########################################

ax[1].plot(vals, color='blue')
ax[1].set_xlabel('n')
ax[1].set_ylabel(r'$\epsilon_{n}$',fontsize=14)
ax[2].imshow(vecs,cmap='coolwarm')
ax[0].text(-0.1, 1.1, 'A', transform=ax[0].transAxes, 
            size=10, weight='bold')
ax[1].text(-0.1, 1.1, 'B', transform=ax[1].transAxes, 
            size=10, weight='bold')
ax[2].text(-0.1, 1.1, 'C', transform=ax[2].transAxes, 
            size=10, weight='bold')
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

fig, ax = plt.subplots(4,2,sharex=True,figsize=(12,4)) #Figure 7
ax[0,0].plot(pdf1, color='red',label='m=0')
ax[1,0].plot(pdf2, color='blue',label='m=24')
ax[2,0].plot(pdf3, color='purple',label='m=25')
ax[3,0].plot(pdf4, color='purple',label='m=34')
ax[0,1].plot(pdf5, color='purple',label='m=38')
ax[1,1].plot(pdf6, color='purple',label='m=40')
ax[2,1].plot(pdf7, color='purple',label='m=54')
ax[3,1].plot(pdf8, color='purple',label='m=55')
ax[0,1].set_xlabel('n')
ax[1,1].set_xlabel('n')
ax[2,1].set_xlabel('n')
ax[3,1].set_xlabel('n')
ax[0,0].set_ylabel(r'$|\phi_{m}^{*}\phi_{0}|^{2}$',fontsize=14)
ax[0,1].set_ylabel(r'$|\phi_{m}^{*}\phi_{38}|^{2}$',fontsize=14)
ax[1,0].set_ylabel(r'$|\phi_{m}^{*}\phi_{24}|^{2}$',fontsize=14)
ax[1,1].set_ylabel(r'$|\phi_{m}^{*}\phi_{40}|^{2}$',fontsize=14)
ax[2,0].set_ylabel(r'$|\phi_{m}^{*}\phi_{25}|^{2}$',fontsize=14)
ax[2,1].set_ylabel(r'$|\phi_{m}^{*}\phi_{54}|^{2}$',fontsize=14)
ax[3,0].set_ylabel(r'$|\phi_{m}^{*}\phi_{34}|^{2}$',fontsize=14)
ax[3,1].set_ylabel(r'$|\phi_{m}^{*}\phi_{55}|^{2}$',fontsize=14)


plt.tight_layout()
plt.show()



