import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA
from plt2array import plt2array
from skimage.io import imsave

class FDTDSolver:
    def __init__(self,Nx,Nt,V,psi_r0,psi_i0,dir,plot=True,plot_iter_num=10,dt=0.1):
        self.Nt = Nt
        self.Nx = Nx
        self.V = V
        self.psi_r = psi_r0
        self.psi_i = psi_i0
        self.psi_r = np.pad(self.psi_r, (1,1))
        self.psi_i = np.pad(self.psi_i, (1,1))
        self.prob = np.zeros((Nx,Nt))
        self.prob[:,0] = self.psi_r[1:-1]**2 + self.psi_i[1:-1]**2
        self.c1 = dt
        self.c2 = 2*dt
        self.dir = dir
        self.plot_iter_num = plot_iter_num
        self.plot = plot

    def plot_iter(self,t):
        fig, ax = plt.subplots()
        ax1 = ax.twinx()
        ax.set_ylim([-0.5,0.5])
        ax1.set_ylim([-5,5])
        ax.plot(self.psi_r,color='red')
        ax.plot(self.psi_i,color='blue')
        ax.plot(self.psi_i**2 + self.psi_r**2,color='purple')
        ax1.plot(self.V[:,t],color='black')
        ax1.set_ylabel('V(x)')
        plt.tight_layout()
        rgb_array = plt2array(fig)
        imsave(self.dir+f'{t}.tif',rgb_array)
        plt.close()

    def update_r(self,t):
        for n in range(1,self.Nx+1):
            self.psi_r[n] = self.psi_r[n]-\
            self.c1*(self.psi_i[n+1] - 2*self.psi_i[n] + self.psi_i[n-1]) +\
            self.c2*self.V[n,t]*self.psi_i[n]
    def update_i(self,t):
        for n in range(1,self.Nx+1):
            self.psi_i[n] = self.psi_i[n] + \
                    self.c1*(self.psi_r[n+1] - 2*self.psi_r[n] + self.psi_r[n-1])\
                    - self.c2*self.V[n,t]*self.psi_r[n]
    def forward(self):
        if self.plot:
            self.plot_iter(0)
        for t in range(1,self.Nt):
            print(f'Time step: {t}')
            self.update_r(t)
            self.update_i(t)
            self.prob[:,t] = self.psi_r[1:-1]**2 + self.psi_i[1:-1]**2
            if t % self.plot_iter_num == 0:
                if self.plot:
                    self.plot_iter(t)


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
vecs = vecs[:,idx]
vals1 = vals[idx]

#################################################
# Simulate time evolution in a finite square well
#################################################

V = np.pad(V, ((1,1),(0,0)))
psi_r0 = (vecs[:,0] + vecs[:,1])/np.sqrt(2)
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
vecs = vecs[:,idx]
vals2 = vals[idx]

#################################################
# Simulate time evolution in a finite square well
#################################################

V = np.pad(V, ((1,1),(0,0)))
psi_r0 = (vecs[:,0] + vecs[:,1])/np.sqrt(2)
psi_i0 = np.zeros_like(psi_r0)
solver2 = FDTDSolver(Nx,Nt,V,psi_r0,psi_i0,dir,plot_iter_num=100,plot=False,dt=dt)
solver2.forward()

#################################################
# Plot expectation values of scaled position
#################################################


fig, ax = plt.subplots(1,3)
X_avg = solver1.prob.T * np.arange(0,Nx)
X_avg = np.sum(X_avg,axis=1)
ax[0].plot(time,X_avg,color='black')
ax[0].set_xlabel(r'$\tau$')
ax[0].set_ylabel(r'$\langle x/L\rangle$')
X_avg = solver2.prob.T * np.arange(0,Nx)
X_avg = np.sum(X_avg,axis=1)
ax[1].plot(time,X_avg,color='purple')
ax[1].set_xlabel(r'$\tau$')
ax[1].set_ylabel(r'$\langle x/L\rangle$')
ax[2].plot(vals1,color='red',label='ISW')
ax[2].plot(vals2,color='blue',label='FSW')
ax[2].set_label('n')
ax[2].legend(fontsize=8)
plt.tight_layout()
plt.show()

##################################################################
# Simulate time evolution in a time-dependent finite square well
##################################################################

# Vl = 2
# Vr = 2
# V = np.zeros((Nx,Nt))
# V[:30,:] = Vl
# V[70:,:] = Vr
# V = np.pad(V, ((1,1),(0,0)))
# time = np.arange(0,Nt,1)*dt
# tau = 0
# lam = 0.1
# X = lam*(1-np.exp(-time/tau))
# V = V * X
# psi_r0 = (vecs[:,0] + vecs[:,1])/np.sqrt(2)
# psi_i0 = np.zeros_like(psi_r0)
# solver = FDTDSolver(Nx,Nt,V,psi_r0,psi_i0,dir,plot_iter_num=100)
# solver.forward()
