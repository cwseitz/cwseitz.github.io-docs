import numpy as np
import matplotlib.pyplot as plt

"""
Toy implementation of the Metropolis MCMC algorithm
to search the 2D parameter space of a 1D Gaussian
"""

class Metropolis:

    def __init__(self,samples,theta0,sigma,iters=1000):
        self.x0 = x0
        self.samples
        self.iters = iters
        self.mu0 = theta0[0]
        self.sg0 = theta0[1]
        self.mu = np.zeros((iters,))
        self.sg = np.zeros((iters,))

    def prior(mu,sg):
        pass

    def likelihood(mu,sigma):
        return np.prod(np.exp(-((self.samples-mu)**2)/2*sigma**2))

    def run():
        for i in range(iters):
            if i == 0:
                mu = self.mu0
                sg = self.sg0
            dmu = np.random.normal(mu,sigma_mu)
            dsg = np.random.normal(sg,sigma_sg)
            f = self.prior(mu,sg)*self.likelihood(mu,sg)
            g = self.prior(mu,sg)*self.likelihood(mu+dmu,sg+dsg)
            a = np.max(1,f/g)
            u = np.random.uniform(0,1)
            if a > u:
                mu += dmu
                sg += dsg
            self.mu[i] = mu
            self.sg[i] = sg

#Generate some samples from a 1D Gaussian
samples = np.random.normal(mu,sigma,size=(1000,))
