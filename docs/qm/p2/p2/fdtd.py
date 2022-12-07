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
        self.psi_r0 = psi_r0
        self.psi_i0 = psi_i0
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

    def plot_init_(self):
        fig, ax = plt.subplots(figsize=(3,1))
        ax.plot(self.psi_r0,color='red')
        ax.plot(self.psi_i0,color='blue')
        plt.tight_layout()
        plt.show()

    def plot_iter(self,t):
        fig, ax = plt.subplots()
        ax1 = ax.twinx()
        ax.set_ylim([-0.5,0.5])
        ax1.set_ylim([-2*self.V.max(),2*self.V.max()])
        #ax.plot(self.psi_r,color='red')
        #ax.plot(self.psi_i,color='blue')
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
        self.plot_init_()
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
