### Stochastic gradient descent (SGD)

The purpose of stochastic gradient descent is to update the model parameters of a neural network so as to reduce a loss function. We do that by computing the gradient of that loss function, averaging over a batch, and tweaking model parameters proportional to that average gradient 

$$\Delta\Phi = - \eta \hat{g}$$

where $\hat{g}$ is defined to be the average gradient of the loss over the batch. We also define $g$ which is the ideal average gradient of the loss for the population distribution

$$\begin{align}
n^_{11} & = \frac{n_{1{\cdot}}\times n_{{\cdot}1}}{n} \\
         & = \frac{120 \times 120}{200}     \\
\text{avec} \quad \sum_{k=1}^{q} n^_{jk}  &  =  n_{j{\cdot}}
  \quad \text{et}  \quad   \sum_{j=1}^{p} n^_{jk}   = n_{.k}   \\
n^_{jk} & = \frac{120\times 120}{200}  \\
n^_{12} & = \frac{n_{1{\cdot}}\times n_{{\cdot}2}}{n} \\
         & = \frac{120\times 80}{200}  \\
n^_{21} & = \frac{n_{2{\cdot}}\times n_{{\cdot}1}}{n}  \\
n^_{21} & = \frac{60\times 120}{200}
\end{align}$$

$$\begin{eqnarray}
  \hat{g} &=& E_{(x,y) \sim \mathrm{Batch}}\;\nabla_\Phi\;\mathrm{\mathcal{L}}(\Phi,x,y)\\
  g &=& E_{(x,y) \sim \mathrm{Pop}}\;\nabla_\Phi\;\mathrm{\mathcal{L}}(\Phi,x,y)
\end{eqnarray}$$

### The thermodynamics of SGD

A common analogy used to explain SGD is that the model $\Phi$ is a particle bouncing around in a higher dimensional space where each parameter defines a dimension. In this model, that space is endowed with a landscape or *potential* which, in deep learning, is the loss function. SGD is then the process of moving the particle through that higher dimensional space stochastically until it approximately reaches a global minimum of the loss function. This brings us to the parameter $\eta$, called the **learning rate** which, in our particle analogy, determines proportionality of the step size of the particle in our higher dimensional space to the average gradient of the loss. 

### Learning rate as temperature

The learning rate can be interpreted as a temperature parameter. For larger learning rates the particle bounces around the higher dimensional space faster. If we run for a long time at a large learning rate we converge to a noisy (hot) stationary distribution with a high loss value. At a lower learning rate we converge to a cooler stationary distribution with a lower loss value.

It is common to train networks by starting hot and then reducing the learning rate so we converge to a lower loss value. This is often called the temperature schedule of the training. 

### Minibatching

SGD also has to take into account that training is typically done on batches of training points.

\begin{eqnarray*}
\Delta\Phi_{t+1} &=& -\eta \hat{g}_t
\\
\hat{g}_t &=& \frac{1}{B} \sum_b \hat{g}_{t,b}
\end{eqnarray*}

where $\hat{g}_{t,b}$ is the average gradient for a particular batch element at time $t$. We use minibatching because the gradients will be smoother after averaging. However, when we use the average gradient over the batch, the step size is proportional to $\frac{1}{B}$, thereby reducing the the effect learning rate or temperature. However, we can make the temperature independent of the batch size with the following observations when $B=1$

\begin{eqnarray*}
\Phi_{t+1} & = &  \Phi_{t} - \eta_0\;\nabla_\Phi {\cal L}(t,\Phi_{t}) \\
\\
\Phi_{t+B} & = &  \Phi_{t} - \sum_{b=0}^{B-1} \;\eta_0\;\nabla_\Phi {\cal L}(t+b,\Phi_{t+b-1}) \\
\\
& \approx & \Phi_t - \eta_0 \sum_b \nabla_\Phi {\cal L}(t+b,\Phi_t) \\
\\
& = & \Phi_t - B\eta_0\; \hat{g}_t
\end{eqnarray*}

so now we compute updates as $\Phi_t - B\eta_0\; \hat{g}_t$ for some learning rate $\eta_{0}$. 

### Momentum

The concept of momentum in deep learning was developed to incorporate more information than just the gradient of the loss for the most recent time step when determining how to adjust model parameters.

\begin{eqnarray*}
  {\color{red} v_t} & {\color{red} =} & {\color{red} \mu v_{t-1} + \eta * \hat{g}_t} \;\;\;\mbox{$\mu$ is typically .9 or .99}\\
  \\
  {\color{red} \Phi_{t+1}} & {\color{red} =} & {\color{red} \Phi_t -  v_t} \\
\end{eqnarray*}

So you can see that the momentum has the original term proportional to the average gradient, but we have added a drag term $\mu v_{t-1}$ with frictional coefficient $\mu$. For $\mu$ close to 1, we retain almost all information from the previous steps allowing previous steps to *guide* future ones. This raises questions on how the parameters $\mu$ affects the effective learning rate but it turns out that we can make the learning rate independent 

\begin{eqnarray*}
\eta = (1-\mu)B\eta_0
\end{eqnarray*}

the temperature will be essentially determined by $\eta_0$ independent of the choice of the momentum parameter $\mu$ or the batch size $B$.

### Momentum as a running average

For $t \geq N$, consider the average of the $N$ most recent values.

\begin{eqnarray*}
\overline{x}_t &=& \frac{1}{N} \;\; \sum_{k = 0}^{N-1}\; x_{t-k}\\
&\approx& (1-\frac{1}{N})\hat{x}_{t-1} + (\frac{1}{N})x_t
\end{eqnarray*}

which is essentially forgetting an old term and bringing in a new one. Another interpretation is that the first term determines how much of the previous running average we remember and the second term is how to incorporate the newest value. But that's exactly we want out of the momentum so we use this to approximate the momentum as a running average

\begin{eqnarray*}
v_t & = & \mu v_{t-1} + {\eta \hat{g}_t}
\\
& = & \left(1-\frac{1}{N}\right) v_{t-1} + {\frac{1}{N}(N\eta \hat{g}_t)}
\end{eqnarray*}

which is just a running average of $N\eta \hat{g}_t$.Alternatively, we can consider a direct running average of the gradient.

$$\tilde{g}_t = \left(1-\frac{1}{N}\right)\tilde{g}_{t-1} + \left(\frac{1}{N}\right) \hat{g}_t$$

The running average of $N\eta\hat{g}$ is the same as $N\eta$ times the running average of $\hat{g}$.  Hence

$$v_t = N \eta \tilde{g}_t$$

So we can simply compute the running average of the gradient multiplied by these constants to obtain the momentum. Updates to the model parameters with momentum are then computed by

\begin{eqnarray*}
  \Phi_{t+1} & = & \Phi_t -  N \eta \tilde{g}_t
\end{eqnarray*}

### Gradient flow

In stochastic gradient descent, we have a model vector $\Phi$ in parameter space that is changing position in a non-deterministic way -- we can only predict a distribution for these changes. In gradient flow, we consider the limit where the learning rate goes to zero or the model changes infinitely slowly, which approximates a continuous change in $\Phi$. In that case, we can actually differentiate $\Phi$.

\begin{eqnarray*}
\frac{d\Phi}{dt} = -g(\Phi)
\end{eqnarray*}

### Langevin dynamics of SGD

In statistical mechanics, we often write down continuous time stochastic differential equations to describe the motion of a particle diffusing through a viscous medium at non-zero temperature. 

\begin{align}
m\frac{dv}{dt} = \xi (t) - \gamma v(t)
\end{align}

where there is a stochastic parameter defined by a stationary distribution. We can show that langevin dynamics apply when the stationary distribution follows a Boltzmann distribution. However, we will also show that, for stochastic gradient descent, the stationary distribution is not a Boltzmann distribution.

If we consider a learning rate $\eta$ that is constant but still very small so that we can work in continuous time where $\Delta t = N\eta$. Although we still want $N$ and therefore $\Delta t$ to be large so that we are averaging over a large set of updates. Assuming, at the same time, the mean gradient $g(\Phi)$ is approximately constant over the interval $\Delta t = N \eta$ we have

$$\Phi(t + \Delta t)  \approx \Phi(t) -g(\Phi)\Delta t + \eta \sum_{i=1}^N (g(\Phi) - \hat{g}_i)$$  

where we have added and subtracted the true gradient $g(\Phi)$. Applying the law of large numbers which says that when we average a big sum, the distribution of the average becomes gaussian, the last term is just a gaussian distribution

\begin{eqnarray*}
\Phi(t + \Delta t) & \approx & \Phi(t) -g(\Phi)\Delta t + \epsilon \sqrt{\Delta t}\;\;\;\;\;\; \epsilon \sim {\cal N}(0,{\color{red} \eta}\Sigma)
\end{eqnarray*}

The first is a **gradient flow** component while the second is a stochastic component arising from our estimates of the gradient or a kind of **diffusion flow**. 
