import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA
from plt2array import plt2array
from skimage.io import imsave

class FDTDSolver:
    def __init__(self,Nx,Nt,V,psi_r0,psi_i0,dir,plot_iter_num=10,dt=0.1):
        self.Nt = Nt
        self.Nx = Nx
        self.V = V
        self.psi_r = psi_r0
        self.psi_i = psi_i0
        self.psi_r = np.pad(self.psi_r, (1,1))
        self.psi_i = np.pad(self.psi_i, (1,1))
        self.c1 = dt
        self.c2 = 2*dt
        self.dir = dir
        self.plot_iter_num = plot_iter_num

    def plot_iter(self,t):
        fig, ax = plt.subplots()
        ax1 = ax.twinx()
        ax.set_ylim([-0.5,0.5])
        ax1.set_ylim([-5,5])
        ax.plot(self.psi_r,color='red')
        ax.plot(self.psi_i,color='blue')
        ax.plot(self.psi_i**2 + self.psi_r**2,color='purple')
        ax1.plot(self.V,color='black')
        ax1.set_ylabel('V(x)')
        plt.tight_layout()
        rgb_array = plt2array(fig)
        imsave(self.dir+f'{t}.tif',rgb_array)
        plt.close()

    def update_r(self):
        for n in range(1,self.Nx+1):
            self.psi_r[n] = self.psi_r[n]-\
            self.c1*(self.psi_i[n+1] - 2*self.psi_i[n] + self.psi_i[n-1]) +\
            self.c2*self.V[n]*self.psi_i[n]
    def update_i(self):
        for n in range(1,self.Nx+1):
            self.psi_i[n] = self.psi_i[n] + \
                    self.c1*(self.psi_r[n+1] - 2*self.psi_r[n] + self.psi_r[n-1])\
                    - self.c2*self.V[n]*self.psi_r[n]
    def forward(self):
        self.plot_iter(0)
        for t in range(1,self.Nt):
            self.update_r()
            self.update_i()
            if t % self.plot_iter_num == 0:
                self.plot_iter(t)



#####################
# Set the parameters
#####################

dir = '/home/cwseitz/Desktop/temp/'
Nx = 100
Nt = 1000
Vl = 2
Vr = 2
t = 1
V = np.zeros((Nx,))
V[:30] = Vl; V[70:] = Vr
H = np.zeros((Nx,Nx))
H += np.diag(2*t + V,k=0) #main diagonal
H += np.diag(-t*np.ones((Nx-1,)),k=1) #upper diagonal
H += np.diag(-t*np.ones((Nx-1,)),k=-1) #lower diagonal

###########################################
# Find eigenvectors and eigenvalues of H0
###########################################

vals, vecs = LA.eig(H)
idx = np.argsort(vals)
vecs = vecs[:,idx]
vals = vals[idx]

###########################################
# Simulate the ground state wavefunction
###########################################

V = np.pad(V, (1,1))
psi_r0 = vecs[:,0] #ground state
psi_i0 = np.zeros_like(psi_r0)
solver = FDTDSolver(Nx,Nt,V,psi_r0,psi_i0,dir,plot_iter_num=10)
solver.forward()
