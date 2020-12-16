```python
from IPython.core.display import display, HTML
display(HTML("<style>.container { width:50% !important; }</style>"))
```


<style>.container { width:50% !important; }</style>


# Introduction

In this post I would like to model the interaction of a particle with its environment. In principle, if we could specify all the forces on a particle by its environment in a deterministic way, we could just add up all the components of the forces and write Newton's law of motion and solve. In the real world, we have no way of predicted those forces and have to use a stochastic variant of Newton's law of motion called the **Langevin equation**.


# The Langevin Equation

The Langevin equation is a first-order differential equation which predicts the diffusion of a particle experiencing friction as well as a stochastic driving force. As stated above, it is a modified form of Newton's equation of motion:

\begin{align}
m\frac{dv}{dt} = \xi (t) - \gamma v(t)
\end{align}

The first term in the Langevin equation $\xi(t)$ is a stochastic force (which will be shown to be normally distributed) and the second term $\gamma v(t)$ is a damping force proportional to the velocity of the particle. To better understand it, let's subject it to different conditions and take a look at its solution. 

# The Damped Solution

First, we consider the the simplest possible case by setting $\xi (t) = 0$ for all $t$. This reduces the Langevin equation to a form for which the solution is already known:

\begin{equation*}
\frac{dv}{dt} = \frac{\gamma}{m} v(t) \rightarrow v(t) = v(0)  e^{-\frac{t}{\tau_{B}}}
\end{equation*}

It is common to refer the ratio $\frac{m}{\gamma}$ as the Brownian timescale for relaxation, $\tau_{B}$. From our solution, we see that, in the presence of damping, $v \rightarrow 0$ as $t \rightarrow \infty$. Short and sweet!


# The Damped/Driven Solution

Our satisfaction from the damped solution may be premature if we want to consider a realistic scenario. If our particle is in thermal equilibium with some kind of bath at non-zero temperature, it should be occasionally be kicked around by other particles. From thermodynamics, we know that the average velocity of a particle as a function of temperature is given by the equipartition theorem: 

\begin{equation*}
\langle v^{2}(t) \rangle \propto \frac{k_{B}T}{m}
\end{equation*}

But when we average the square of our solution to the Langevin equation:

\begin{equation*}
\langle v^{2}(t) \rangle = \frac{1}{t} \int_{0}^{t} v^{2}(0)  e^{-2\frac{t}{\tau_{B}}}dt = \frac{\tau_{B}v_{0}^{2}}{2t}(1 - e^{-2\frac{t}{\tau_{B}}})
\end{equation*}

which goes to zero at long times. We can speculate that $\xi (t)$, which we have ignored in this case, is what reconciles this conflict by representing the interaction of the particle with a thermal bath. So, we proceed by lifting our constraint that $\xi(t) = 0$ but we still need more information about it. We can usually make the following assumptions: 

1. $\langle \xi(t) \rangle = 0$
2. It is independent of position - the iteraction with its environment is the same everywhere
3. $\xi(t)$ is not correlated with itself at very short time-spans.

We can find the driven-damped solution by adding to the damped solution a series of infinitesimal kicks, each of which then decays with time. An integral sums over all those kicks, weighting each one by an exponential factor based on the time t−s that has passed since it occurred.


\begin{equation*}
v(t) = v(0)  e^{-\frac{t}{\tau_{B}}} + \frac{1}{m}\int_{0}^{t} \xi(s)e^{-(t-s)/\tau_{B}}ds
\end{equation*}

As before, we can use the equipartition theorem but we first need $\langle v^{2}(t) \rangle$: 


\begin{equation*}
\langle v^{2}(t) \rangle = \frac{1}{m}\int_{0}^{t} \xi(s)e^{-(t-s)/\tau_{B}}ds
\end{equation*}

\begin{equation*}
lim_{t \to \infty} \langle v^2(t) \rangle = \frac{1}{m^2} \int_0^{\infty} \int_0^{\infty} e^{-\frac{\gamma}{m}(2t-t'-t'')} \langle \xi(t')\xi(t'') \rangle dt' dt''
\end{equation*}

\begin{split}\begin{array}{rcl}
lim_{t \to \infty} \langle v^2(t) \rangle &=& \frac{1}{m^2} \int_{r=0}^{\infty} \int_{s=-\infty}^{\infty} e^{-\frac{\gamma}{m}(2r+s)} \langle \xi(0)\xi(s) \rangle dr ds \\
&=& \frac{1}{m^2} \left( \int_0^{\infty} e^{-\frac{\gamma}{m}2r} dr \right) \left( \int_{-\infty}^{\infty} e^{-\frac{\gamma}{m}s} \langle \xi(0)\xi(s) \rangle ds \right) \\
&=& \frac{1}{2 \gamma m} \int_{-\infty}^{\infty} e^{-\frac{\gamma}{m}s} \langle \xi(0)\xi(s) \rangle ds
\end{array}\end{split}

If we make the additional assumption that the timescale over which the random force is correlated with itself is much smaller than $\tau_{B}$ - the timescale on which friction operates, then we can make a further simplification:

\begin{equation*}
2 \gamma kT = \int_{-\infty}^{\infty} \langle R(0)R(s) \rangle ds
\end{equation*}

This result is called the *fluctuation-dissipation theorem* which relates $T, \gamma, and \xi$. Any system in contact with a heat bath will experience both a stochastic force and friction - you cannot have one without the other.


```python

```
