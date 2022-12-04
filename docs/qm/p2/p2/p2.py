import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

class FDTDSolver:
    def __init__(self,Nx,Nt,V,psi_r0,psi_i0):
        self.Nt = Nt
        self.Nx = Nx
        self.V = V
        self.psi_r = np.zeros((2*Nt,Nx))
        self.psi_i = np.zeros((2*Nt,Nx))
        self.psi_r[0,:] = np.squeeze(psi_r0)
        self.psi_i[0,:] = np.squeeze(psi_i0)
    def forward(self):
        for i in range(2*self.Nt-1):
            for j in range(self.Nx-1):
                self.psi_i[i+1,j] = self.psi_r[i,j+1] - 2*self.psi_r[i,j] +\
                                  self.psi_r[i,j-1] - self.V[j]*self.psi_r[i,j]\
                                  + self.psi_i[i,j]
                self.psi_r[i+1,j] = -1*(self.psi_i[i+1,j+1] - 2*self.psi_i[i+1,j] +\
                                  self.psi_r[i+1,j-1]) + self.V[j]*self.psi_i[i+1,j]\
                                  + self.psi_r[i,j]

#####################
# Set the parameters
#####################

Nx = 100
Nt = 100

N = Nx
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
# Simulate the ground state wavefunction
###########################################

psi_r0 = vecs[:,5] #ground state
psi_i0 = np.zeros((Nx,1))
solver = FDTDSolver(Nx,Nt,V,psi_r0,psi_i0)
solver.forward()

fig, ax = plt.subplots()
ax.plot(solver.psi_r[0,:],color='red')
ax.plot(solver.psi_i[0,:],color='blue')
plt.show()

fig, ax = plt.subplots()
ax.plot(solver.psi_r[2,:],color='red')
ax.plot(solver.psi_i[2,:],color='blue')
plt.show()
