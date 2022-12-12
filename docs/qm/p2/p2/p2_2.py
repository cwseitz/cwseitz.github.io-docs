import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA
from fdtd import FDTDSolver

dir = '/home/cwseitz/Desktop/temp/'
Nx = 100
Nt = 50000
eta = 1 #hopping parameter
dtau = 0.1

######################
# Infinite square well
######################

V = np.zeros((Nx,Nt))
H = np.zeros((Nx,Nx)) #Hamiltonian at t = 0
H += np.diag(2*eta + V[:,0],k=0) #main diagonal
H += np.diag(-eta*np.ones((Nx-1,)),k=1) #upper diagonal
H += np.diag(-eta*np.ones((Nx-1,)),k=-1) #lower diagonal

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
lam = 5 * 10**-4
V *= lam

#############################################
# Transform the perturbation to energy basis
#############################################

Hp = np.zeros((Nx,Nx)) #perturbation Hamiltonian
Hp += np.diag(V[:,0],k=0) #main diagonal
U0 = LA.inv(vecs1) #unitary operator
Hp_e = U0 @ Hp @ LA.inv(U0) #perturbation in energy basis
P_0n = Hp_e[0,1:]**2
E0 = vals1[0]
P_0n /= (vals1[1:]-E0)**2

#############################################
# Compute transition probability for n=1,2,3
#############################################

tau = np.arange(0,Nt*3)*dtau
v_11 = Hp_e[0,0]
v_12 = Hp_e[0,1]
v_13 = Hp_e[0,2]
c_11_msq = (tau*v_11)**2
c_12_msq = ((4*v_12**2)/((vals1[1]-vals1[0]))**2)*np.sin(tau*(vals1[1]-vals1[0])/2)**2
c_13_msq = ((4*v_13**2)/((vals1[2]-vals1[0]))**2)*np.sin(tau*(vals1[2]-vals1[0])/2)**2
Z = c_11_msq + c_12_msq + c_13_msq
c_11_msq /= Z
c_12_msq /= Z
c_13_msq /= Z
Ebar = c_11_msq*vals1[0] + c_12_msq*vals1[1] + c_13_msq*vals1[2]

fig, ax = plt.subplots(2,2,figsize=(4,3))
ax[0,0].plot(tau,c_11_msq,color='red',label=r'$|c_{11}|^{2}$')
ax[0,1].plot(tau,c_12_msq,color='blue',label=r'$|c_{12}|^{2}$')
ax[1,0].plot(tau,c_13_msq,color='purple',label=r'$|c_{13}|^{2}$')
ax[1,1].plot(tau,Ebar,color='cyan')
ax[0,0].set_xlabel(r'$\tau$')
ax[0,1].set_xlabel(r'$\tau$')
ax[1,0].set_xlabel(r'$\tau$')
ax[1,1].set_xlabel(r'$\tau$')
ax[0,0].set_ylabel(r'$P(1\rightarrow 1)$')
ax[1,0].set_ylabel(r'$P(1\rightarrow 2)$')
ax[0,1].set_ylabel(r'$P(1\rightarrow 3)$')
ax[1,1].set_ylabel(r'$\langle H \rangle$')
plt.tight_layout()
plt.show()

##################################################################
# Simulate time evolution for a time dependent Hamiltonian
##################################################################

# V = np.pad(V, ((1,1),(0,0)))
# psi_r0 = -1*vecs1[:,0] #pure ground state
# psi_i0 = np.zeros_like(psi_r0)
# solver = FDTDSolver(Nx,Nt,V,psi_r0,psi_i0,dir,plot_iter_num=5000,plot=True,dt=dtau,H=H+Hp)
# solver.forward()

##################################################################
# Construction time evolution analytically
##################################################################

probt = np.zeros((Nx,Nt))
probt[:,0] = vecs1[:,0]**2
for t in range(1,Nt):
    psi = c_11_msq[t]*vecs1[:,0] + c_12_msq[t]*vecs1[:,1] + c_12_msq[t]*vecs1[:,2]
    probt[:,t] = psi**2

X_avg = probt.T * np.arange(0,Nx)
X_avg = np.sum(X_avg,axis=1)
plt.plot(X_avg)
plt.show()

##################################################################
# Position/Energy expectation value for time-dependent Hamiltonian
##################################################################

X_avg = solver.prob.T * np.arange(0,Nx)
X_avg = np.sum(X_avg,axis=1)
tau = np.arange(0,Nt)*dtau
fig, ax = plt.subplots()
ax.plot(tau,X_avg,color='black')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$\langle x/L\rangle$')
plt.tight_layout()
plt.show()
