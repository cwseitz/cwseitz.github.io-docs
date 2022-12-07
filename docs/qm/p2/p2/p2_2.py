import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA
from fdtd import FDTDSolver

dir = '/home/cwseitz/Desktop/temp/'
Nx = 100
Nt = 100000
t = 1
dt = 0.1

######################
# Infinite square well
######################

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

######################################
# Define the perturbation Hamiltonian
######################################

Vl = 2
Vr = 3
V = np.zeros((Nx,Nt))
V[:30,:] = Vl
V[70:,:] = Vr
lam = 5e-4
V *= lam

#############################################
# Transform the perturbation to energy basis
#############################################

Hp = np.zeros((Nx,Nx)) #perturbation Hamiltonian
Hp += np.diag(V[:,0],k=0) #main diagonal
U0 = LA.inv(vecs1) #unitary operator
Hp_e = U0 @ Hp @ LA.inv(U0) #perturbation in energy basis

#############################################
# Compute transition probability for n=1,2,3
#############################################

time = np.arange(0,100000)*dt
v_11 = Hp_e[0,0]
v_12 = Hp_e[0,1]
v_13 = Hp_e[0,2]
c_11_msq = 1 + (time*v_11)**2
c_12_msq = ((4*v_12**2)/((vals1[1]-vals1[0]))**2)*np.sin(time*(vals1[1]-vals1[0])/2)**2
c_13_msq = ((4*v_13**2)/((vals1[2]-vals1[0]))**2)*np.sin(time*(vals1[2]-vals1[0])/2)**2

fig, ax = plt.subplots(1,3,figsize=(7,2))
ax[0].plot(time,c_11_msq,color='red',label=r'$|c_{11}|^{2}$')
ax[1].plot(time,c_12_msq,color='blue',label=r'$|c_{12}|^{2}$')
ax[2].plot(time,c_13_msq,color='purple',label=r'$|c_{13}|^{2}$')
ax[0].set_xlabel(r'$\tau$')
ax[1].set_xlabel(r'$\tau$')
ax[2].set_xlabel(r'$\tau$')
ax[0].set_ylabel(r'$|c_{11}|^{2}(\tau)$')
ax[1].set_ylabel(r'$|c_{12}|^{2}(\tau)$')
ax[2].set_ylabel(r'$|c_{13}|^{2}(\tau)$')
plt.tight_layout()
plt.show()

##################################################################
# Simulate time evolution for a time dependent Hamiltonian
##################################################################

V = np.pad(V, ((1,1),(0,0)))
time = np.arange(0,Nt,1)*dt
psi_r0 = vecs1[:,0]
psi_i0 = np.zeros_like(psi_r0)
solver = FDTDSolver(Nx,Nt,V,psi_r0,psi_i0,dir,plot_iter_num=5000,plot=True,dt=dt)
solver.forward()

##################################################################
# Position expectation value for time-dependent Hamiltonian
##################################################################

fig, ax = plt.subplots()
X_avg = solver.prob.T * np.arange(0,Nx)
X_avg = np.sum(X_avg,axis=1)
ax.plot(time,X_avg,color='black')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$\langle x/L\rangle$')
plt.tight_layout()
plt.show()
