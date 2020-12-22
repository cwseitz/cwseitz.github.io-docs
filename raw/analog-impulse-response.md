### Impulse response

In signal processing, the impulse response, or impulse response function (IRF), of a dynamic system is its output when presented with a brief input signal, called an impulse. By definition, the output for an arbitrary input sinal is equivalent to the convolution of the input with the IRF. If we let $h(t)$ be the IRF then we can predict the output as


\begin{align}
V_{out}(t) = V_{in}(t) * h(t) = \int_{0}^{T} V_{in}(t)h(t)dt 
\end{align}


Another useful property of the IRF is that its Fourier transform is the frequency reponse of the system - the transfer function. 

\begin{align}
H(\omega) = \int_{-\infty}^{\infty} h(t)\exp -i\omega t dt
\end{align}

This property can be very useful if we already know the impulse response and would like to find the transfer function.

### A toy example

The following differential equation describes the relationship between input and output signals for an RC circuit with time constant $\tau$

\begin{align}
V_{in} = \tau\frac{dV_{out}}{dt} + V_{out}
\end{align}

You can solve this equation by first finding the homogeneous solution when $V_{in} = 0$.

\begin{align}
\tau\frac{dV_{out}}{dt} = - V_{out}
\end{align}

\begin{align}
V_{out} = A(t)e^{\frac{-t}{\tau}}
\end{align}

Plugging that back into our original differential equation we have: 

\begin{align}
V_{in} = \tau[A'(t)e^{\frac{-t}{\tau}} - \frac{A(t)}{\tau}e^{\frac{-t}{\tau}}]  + A(t)e^{\frac{-t}{\tau}} = \tau A'(t)e^{\frac{-t}{\tau}}
\end{align}

If our input is an impulse, we substitute a delta function $\delta(0)$ for $V_{in}$: 

\begin{align}
A(t) = \frac{1}{\tau}\int \delta(0)e^\frac{t}{\tau}dt = \frac{1}{\tau}
\end{align}

\begin{align}
h(t) = \frac{1}{\tau}e^{\frac{-t}{\tau}}
\end{align}

So we see that the impulse response of an RC circuit is a decaying expontential. Now we can derive the transfer function by taking the fourier transform of the impulse response:

\begin{align}
\mathcal{F}[h(t)] = \frac{1}{\tau}\int_{-\infty}^{\infty}e^{-t(i\omega + 1/\tau)}dt = \frac{1}{-(1 + i\omega\tau)}
\end{align}
