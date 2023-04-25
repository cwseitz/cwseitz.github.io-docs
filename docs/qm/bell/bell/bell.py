import numpy as np
import matplotlib.pyplot as plt

import numpy as np

def reduced_density_matrices(alpha, beta, gamma, delta):
    rho_A = np.array([[alpha*alpha.conj() + gamma*gamma.conj(), alpha*beta.conj() + gamma*delta.conj()],
                      [beta*alpha.conj() + delta*gamma.conj(), beta*beta.conj() + delta*delta.conj()]])

    rho_B = np.array([[alpha*alpha.conj() + beta*beta.conj(), alpha*gamma.conj() + beta*delta.conj()],
                      [gamma*alpha.conj() + delta*beta.conj(), gamma*gamma.conj() + delta*delta.conj()]])

    return rho_A, rho_B

def entanglement_entropy(rho_A):
    eigenvals = np.linalg.eigvals(rho_A)
    eigenvals = eigenvals[eigenvals > 1e-12]
    S = -np.sum(eigenvals * np.log2(eigenvals))
    return np.real(S)

def generate_random_state():
    tuples = np.random.uniform(size=(4,2))
    norms_squared = np.sum(tuples**2, axis=1)
    norm_factor = np.sqrt(np.sum(norms_squared))
    normalized_tuples = tuples / norm_factor
    state = np.zeros((4,), dtype=np.complex128)
    state[0] = normalized_tuples[0,0] + normalized_tuples[0,1]*1j
    state[1] = normalized_tuples[1,0] + normalized_tuples[1,1]*1j
    state[2] = normalized_tuples[2,0] + normalized_tuples[2,1]*1j
    state[3] = normalized_tuples[3,0] + normalized_tuples[3,1]*1j
    return state

def tsirelson(psi):
    sigma_y = np.array([[0, -1j], [1j, 0]])
    tbound = np.sqrt(4 - 4*psi.conj() @ np.kron(sigma_y, sigma_y) @ psi)
    return np.real(tbound)


nsamples = 10000
samples = np.zeros((nsamples,2))
for n in range(nsamples):
    psi = generate_random_state()
    rho_A, rho_B = reduced_density_matrices(*psi)
    ee = entanglement_entropy(rho_B)
    tbound = tsirelson(psi)
    samples[n,:] = ee,tbound
    
fig, ax = plt.subplots()
ax.scatter(samples[:,1],samples[:,0],color='blue',alpha=0.03)
ymin,ymax = ax.get_ylim()
ax.set_xlabel(r'Tsirelson Bound')
ax.set_ylabel(r'$S(\rho_{A})$')
ax.vlines(2*np.sqrt(2),ymin,ymax,color='red',linestyle='--',label=r'$2\sqrt{2}$')
ax.legend(loc='best')
plt.tight_layout()
plt.show()
