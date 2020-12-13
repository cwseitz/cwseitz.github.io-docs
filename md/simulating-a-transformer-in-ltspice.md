---
layout: post
title: "Simulating a transformer in LT-spice"
date: 2020-11-17
categories: [electronics]
---

# Simulating a transformer in LTSpice

In LTSpice, there is no transformer component per say; however, a transformer is really just a pair of inductors. This means that we can simulate a transformer in spice by creating two or more inductors and specifying their mutual inductance via a spice directive. Before we do that, recall that the voltage ratio of the primary and secondary windings of a transformer is given by:

\begin{align}
\frac{V_{2}}{V_{1}} = \frac{N_{2}}{N_{1}}
\end{align}

where $N_{i}$ is the number of turns of that winding. But in LTSpice, we control the inductance $L$, so we have to use the relation of inductance to the number of turns:

\begin{align}
L = \frac{N^{2}\mu A}{I}
\end{align}

This means that, for a given voltage ratio, we need an inductance ratio that satisfies:

\begin{align}
\frac{V_{2}}{V_{1}} \propto \sqrt{\frac{L_{2}}{L_{1}}}
\end{align}

Let's say we want a step-up transformer with a voltage ratio of 10 i.e. an inductance ratio of 100. We can realize this with a pair of 1mH and 100mH inductors. We will drive the primary winding of this transformer with a $10V$ AC signal with frequency 60Hz through a resistance $R_{2} = 10\Omega$. The secondary also has a series resistance $R_{1} = 100\Omega$. The primary winding of the transformer is really just an RL circuit with total impedance:

\begin{align}
|Z| = \sqrt{R^{2} + (\omega L)^{2}} = 10\Omega
\end{align}

The impedance of the inductor alone is:

\begin{align}
X_{L} = \omega L = 3.75 \Omega
\end{align}

Knowing the current through the primary winding:

\begin{align}
I = \frac{V}{|Z|} = 1A
\end{align}

so the voltage across the inductor is $375mV$ which is roughly what we observe in the plot below. Now, since we have chosen inductances for a voltage ratio of 100, we should have an output voltage of 3.75V, which is the case. The last thing to note is the half-cycle phase shift between the input and output voltages - food for thought.


 <img src="../../images/transformer-ex.png" width="600"/>


<img src="../../images/transformer-ex-plt.png" width="600"/>





```code

```
