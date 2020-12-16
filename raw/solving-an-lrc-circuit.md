# The LRC Circuit

Kirchoff's voltage rule written for an LRC circuit driven at angular frequency $\omega$: 

\begin{align}
L\frac{dI}{dt} + IR + \frac{1}{C}\int I dt = Ve^{i\omega t}
\end{align}

which can be differentiated to give: 

\begin{align}
LI'' + RI' + \frac{1}{C}I = Ve^{i\omega t}
\end{align}

which is second-order differential equation with constant coefficient driven by a complex exponential. The general solution for an equation of this form is: 

\begin{align}
I(t) = We^{i\omega t}
\end{align}

Plugging $I(t)$ in an rearranging gives the following value for W: 

\begin{align}
W = \frac{V}{R + j\omega L + \frac{1}{j\omega C}}
\end{align}

The term in the denomenator is a complex number called the *impedance*. Basically, the impedance is a generalized resistance that applies to capacitors and inductors as well as resistors. We might as well write out the impedance and find its magnitude and phase: 

\begin{align}
Z = {R + j(\omega L - \frac{1}{\omega C})}
\end{align}

\begin{align}
|Z|^{2} = R^{2} + (\omega L - \frac{1}{\omega C})^{2}
\end{align}

\begin{align}
\phi = \arctan{\frac{\omega L - \frac{1}{\omega C}}{R}}
\end{align}



Given the magnitude of the impedance, we can find the current through our LRC circuit:

\begin{align}
I = \frac{ Ve^{i\omega t + \phi}}{\sqrt{R^{2} + (\omega L - \frac{1}{\omega C})^{2}}}
\end{align}

notice the phase shift $\phi$. Finally, we can find the voltage drop across each of the components. The resistor is easy, the voltage drop is simply $IR$. However, the inductor and capacitor are a little more complicated. The drop across the inductor can be found via the terms we put in our original differential equation: 

\begin{align}
V_{L} = L\frac{dI}{dt} = \frac{ i\omega VLe^{i\omega t + \phi}}{\sqrt{R^{2} + (\omega L - \frac{1}{\omega C})^{2}}}
\end{align}

\begin{align}
V_{C} = \frac{\int Idt}{C} = \frac{ -iVe^{i\omega t + \phi}}{\omega C\sqrt{R^{2} + (\omega L - \frac{1}{\omega C})^{2}}}
\end{align}


Notice the phase of these complex voltages. The voltage across the inductor leads the voltage on the resistor by 90 degrees since it is a purely real resistance. The voltage across the resistor then leads the capacitor by 90 degrees. Each of these voltages oscillates with an angular frequency $\omega$ with a phase shift $\phi$ relative to the source voltage. 


```python

```
