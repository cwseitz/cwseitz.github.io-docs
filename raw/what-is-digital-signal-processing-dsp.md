# Digital Signal Processing (DSP)
 
Digital Signal processing or DSP is difficult to define precisely but a working definition might read: DSP is the use of discrete algorithms to modify the information contained within digital signals or to extract valuable features of a digital signal. A digital signal in itself is just a variable that can take on a discrete set of values and can be displayed or manipulated. Digital signals are very common in the modern age and play a central role in telecommunications, biomedical signals, music, video/image, and so on. 


# Key DSP Operations

Most DSP algorithms are based off of four fundamental operations: 

1. Convolution
2. Correlation
3. Filtering
4. Discrete Transformations

The next four sections are dedicated to the demonstration of these four operations so that they can be used as building blocks for more complex operations. 


# Convolution and Filtering


For a discrete time sequence $x(t)$, its convolution with another discrete time sequence $h(t)$ is defined as:

\begin{equation*}
y(t) = x(t)*h(t) = \sum_{k=-\infty}^{\infty}x(k)\cdot h(t-k)
\end{equation*}

At first glance, this seems like an arbitrary mathematical operation, but it is very useful in signal processing applications provided we carefully choose the function $h(t)$. Indeed, the function $h(t)$ can be designed so that it acts as a *filter*, eliminating undesirable signal components. There is an interesting theorem in mathematics called the *convolution theorem* that states that the convolution in the time domain is equivalent to multiplication in the frequency domain. In fact, this relationship between the convolution and frequency domain is why I have merged two seemingly distinct sections on convolution and filtering. We will see that we can filter a digital signal in the time domain by convolution or we can transform to the frequency domain, perform multiplication and transform back to the time domain. 

# Correlation

There are two main types of correlations: autocorrelations and cross-correlations. The former describes the correlation of a digital signal with itself while the latter describes the correlation of two independent signals. 

