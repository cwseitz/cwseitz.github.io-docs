When designing electrical circuits that process input signals, we are always concerned with obtaining an output that suits the purpose of the circuit. In the time domain, we are usually interested in voltage at the output as a function of time. In the frequency domain, we are concerned with the frequency response or transfer function of the circuit.

<img src="../../images/lpf-hpf.png" width="600"/>

There are cases where you can write down differential equations for the circuit in the time domain and solve those equations to find the output of your circuit. However, perhaps a more useful approach is to find the *impulse reponse* of the system first. The impulse response is the voltage at the output when the input is an impulse or delta function with known amplitude. Once the impulse response $h(t)$ is known, we can convolve the input in the time domain with the impulse function to obtain the output.

\begin{align}
V_{out} = \int h(t)V_{in}dt
\end{align}


Another interesting property of the impulse response is that its fourier transform is the frequency reponse of the system i.e. the transfer function.

\begin{align}
H(\omega) = \mathcal{F}[h(t)]
\end{align}

This property can be very useful if we already know the impulse response and would like to find the transfer function. Ultimately, if we know the impulse response we know pretty much everything we need to know - practically speaking. Let's begin with an RC circuit. If we are probing the RC circuit's capcitor, then the general prescription begins with writing down KVL and KCL:

\begin{align}
V_{in} = IR + \frac{Q}{C}
\end{align}

\begin{align}
I = C\frac{dV_{out}}{dt}
\end{align}

which can be combined to give

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

At this point, we have to specify our input to move forward. If our input is an impulse, we substitute a delta function $\delta(0)$ for $V_{in}$:

\begin{align}
A(t) = \frac{1}{\tau}\int \delta(0)e^\frac{t}{\tau}dt = \frac{1}{\tau}
\end{align}

\begin{align}
h(t) = \frac{1}{\tau}e^{\frac{-t}{\tau}}
\end{align}

From a previous post on RC frequency response, we already know that the transfer function is:

\begin{align}
H(\omega) = \frac{1}{1 + i\omega RC}
\end{align}

Which we should be able to verify by taking the fourier transform of the impulse response:

\begin{align}
\mathcal{F}[h(t)] = \frac{1}{\tau}\int_{-\infty}^{\infty}e^{-t(i\omega + 1/\tau)}dt = \frac{1}{-(1 + i\omega\tau)}
\end{align}

which only differs by a phase from our original solution. Another route to finding the impulse response would involve taking the inverse fourier transform of the previously found transfer function. This path is rocky however, the integral faced usually requires a table lookup of some kind.
