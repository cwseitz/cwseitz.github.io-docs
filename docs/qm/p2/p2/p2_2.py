import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA
from fdtd import FDTDSolver
from plt2array import plt2array
from skimage.io import imsave

dir = '/home/cwseitz/Desktop/temp/'
Nx = 100
Nt = 100000
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
E0 = vals1[0]
E1 = vals1[1]
E2 = vals1[2]

#############################################
# Compute transition probability for n=1,2,3
#############################################

tau = np.arange(0,Nt)*dtau
v_11 = Hp_e[0,0]
v_12 = Hp_e[0,1]
v_13 = Hp_e[0,2]
c_1 = 1  - 1j*v_11*tau
omega_12 = vals1[1]-vals1[0]
c_2 = (v_12/omega_12)*(1-np.exp(1j*omega_12*tau))
omega_13 = vals1[2]-vals1[0]
c_3 = (v_13/omega_13)*(1-np.exp(1j*omega_13*tau))

fig, ax = plt.subplots(2,3,figsize=(9,2))
ax[0,0].plot(tau,np.real(c_1),color='red',label='Re')
ax[0,0].plot(tau,np.imag(c_1),color='blue',label='Im')
ax[0,0].set_ylabel(r'$c_{1}$')
ax1 = ax[1,0]
ax1.plot(tau, (c_1-1)*np.conj(c_1-1),color='purple')
ax1.set_ylabel(r'$|c_{1}|^{2}$')
ax[0,1].plot(tau,np.real(c_2),color='red',label='Re')
ax[0,1].plot(tau,np.imag(c_2),color='blue',label='Im')
ax[0,1].set_ylabel(r'$c_{2}$')
ax2 = ax[1,1]
ax2.plot(tau, c_2*np.conj(c_2),color='purple')
ax2.set_ylabel(r'$|c_{2}|^{2}$')
ax[0,2].plot(tau,np.real(c_3),color='red',label='Re')
ax[0,2].plot(tau,np.imag(c_3),color='blue',label='Im')
ax[0,2].set_ylabel(r'$c_{3}$')
ax3 = ax[1,2]
ax3.plot(tau, c_3*np.conj(c_3),color='purple')
ax3.set_ylabel(r'$|c_{3}|^{2}$')
plt.tight_layout()
plt.show()

########################################
# Construct time evolution analytically
########################################

probt = np.zeros((Nx,Nt))
probt[:,0] = vecs1[:,0]**2
Ht = np.zeros((Nt,))
Ht[0] = E0
for t in range(1,Nt):
    psi = c_1[t]*vecs1[:,0] + c_2[t]*vecs1[:,1] + c_3[t]*vecs1[:,2]
    prob = np.conj(psi)*psi
    A = np.sum(prob)
    prob = prob/A
    probt[:,t] = prob
    Z = c_1[t]*np.conj(c_1[t]) + c_2[t]*np.conj(c_2[t]) + c_3[t]*np.conj(c_3[t])
    Ht[t] = c_1[t]*np.conj(c_1[t])*E0 + c_2[t]*np.conj(c_2[t])*E1 + c_3[t]*np.conj(c_3[t])*E2
    Ht[t] = Ht[t]/Z
    if t % 1000 == 0:
        fig, ax = plt.subplots()
        ax.plot(prob,color='black')
        ax.set_ylim([0,0.05])
        ax.set_xlabel('x')
        ax.set_ylabel(r'$|\psi|^{2}$')
        rgb_array = plt2array(fig)
        imsave(dir+f'{t}_sim.tif',rgb_array)
        plt.close()

X_avg = probt.T * np.arange(0,Nx)
X_avg = np.sum(X_avg,axis=1)
fig, ax = plt.subplots(1,2)
ax[0].plot(tau,X_avg,color='black')
ax[0].set_xlabel(r'$\tau$')
ax[0].set_ylabel(r'$\langle x/L\rangle$')
ax[1].plot(tau,Ht,color='black')
ax[1].set_xlabel(r'$\tau$')
ax[1].set_ylabel(r'$\langle H \rangle$')
ax[1].hlines(E0,xmin=0,xmax=tau.max(),color='blue',label=r'$E_{0}$')
plt.legend()
plt.tight_layout()
plt.show()
