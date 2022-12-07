import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA
from fdtd import FDTDSolver

dir = '/home/cwseitz/Desktop/temp/'
Nx = 100
Nt = 50000
t = 1
dt = 0.1

######################
# Infinite square well
######################

print('Simulating the infinite square well...\n')
time = np.arange(0,Nt)*dt
V = np.zeros((Nx,Nt))
H = np.zeros((Nx,Nx)) #Hamiltonian at t = 0
H += np.diag(2*t + V[:,0],k=0) #main diagonal
H += np.diag(-t*np.ones((Nx-1,)),k=1) #upper diagonal
H += np.diag(-t*np.ones((Nx-1,)),k=-1) #lower diagonal

###########################################
# Find eigenvectors and eigenvalues of H0
###########################################

vals, vecs = LA.eig(H)
idx = np.argsort(vals)
vecs1 = vecs[:,idx]
vals1 = vals[idx]

#################################################
# Simulate time evolution in a infinite square well
#################################################

V = np.pad(V, ((1,1),(0,0)))
psi_r0 = (vecs1[:,0] + vecs1[:,1])/np.sqrt(2)
psi_i0 = np.zeros_like(psi_r0)
solver1 = FDTDSolver(Nx,Nt,V,psi_r0,psi_i0,dir,plot_iter_num=100,plot=False,dt=dt)
solver1.forward()

######################
# Finite square well
######################

print('Simulating the finite square well...\n')
time = np.arange(0,Nt)*dt
Vl = 2
Vr = 2
V = np.zeros((Nx,Nt))
V[:30,:] = Vl
V[70:,:] = Vr
H = np.zeros((Nx,Nx)) #Hamiltonian at t = 0
H += np.diag(2*t + V[:,0],k=0) #main diagonal
H += np.diag(-t*np.ones((Nx-1,)),k=1) #upper diagonal
H += np.diag(-t*np.ones((Nx-1,)),k=-1) #lower diagonal

###########################################
# Find eigenvectors and eigenvalues of H0
###########################################

vals, vecs = LA.eig(H)
idx = np.argsort(vals)
vecs2 = vecs[:,idx]
vals2 = vals[idx]

#################################################
# Simulate time evolution in a finite square well
#################################################

V = np.pad(V, ((1,1),(0,0)))
psi_r0 = (vecs2[:,0] + vecs2[:,1])/np.sqrt(2)
psi_i0 = np.zeros_like(psi_r0)
solver2 = FDTDSolver(Nx,Nt,V,psi_r0,psi_i0,dir,plot_iter_num=100,plot=False,dt=dt)
solver2.forward()

#################################################
# Plot expectation values of scaled position
#################################################

fig, ax = plt.subplots(1,3,figsize=(6,2))
X_avg = solver1.prob.T * np.arange(0,Nx)
X_avg = np.sum(X_avg,axis=1)
ax[0].plot(time,X_avg,color='black')
ax[0].set_xlabel(r'$\tau$')
ax[0].set_ylabel(r'$\langle x/L\rangle$')
ax[0].set_ylim([30,70])
X_avg = solver2.prob.T * np.arange(0,Nx)
X_avg = np.sum(X_avg,axis=1)
ax[1].plot(time,X_avg,color='purple')
ax[1].set_xlabel(r'$\tau$')
ax[1].set_ylabel(r'$\langle x/L\rangle$')
ax[1].set_ylim([30,70])
ax[2].plot(vals1,color='red',label='ISW')
ax[2].plot(vals2,color='blue',label='FSW')
ax[2].set_label('n')
ax[2].set_ylabel(r'$\epsilon_{n}$')
ax[2].legend(fontsize=8)
plt.tight_layout()
plt.show()
