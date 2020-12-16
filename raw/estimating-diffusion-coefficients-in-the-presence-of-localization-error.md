# Introduction

Single particle tracking has become a popular tool in the biophysical sciences as it has the potential to describe molecular processes while concurrently providing a visual representation of those processes. Various studies have been done to illustrate the precision limits of single particle tracking; however, it remains an open question in a number of applications. Here, I will try to outline the sources of error in single particle tracking and how those errors propagate to commonly extracted dynamic quantities such as the Mean Squared Displacement (MSD).

# Origins of Uncertainty

Localization uncertainty is unavoidable in single particle tracking studies and should be always be taken into account before making experimental conclusions. Localization uncertainty typically stems from noise in CMOS/CCD camera sensors and blurring over the exposure time of a digital sensor to fluorescent emission. I will focus primarily on the effect of noise on single particle localization - blurring only becomes important at high diffusion rates.

# Localization Uncertainty

In a previous post, I discussed two of CCD/CMOS sensor noise: *shot noise* and *dark noise* and how they introduce uncertainty in the photon count at a particular pixel. When speaking of localization error, it is also important to take the *pixelation noise* into account. This form of noise arises from the discrete sampling of a continuous 2D space; we don't know where each photon arrived in the pixel. We can start with the localization uncertainty for an ideal scenario with no noise at all. The only source of uncertainty is due to the point spread function of the microscope. Under the assumption that the PSF is given by the following Gaussian expression: 


\begin{align}
I(I_{0}, \vec{r_{0}}) = I_{0}\exp[-\frac{(x-x_{0})^{2} + (y-y_{0})^{2}}{2s^{2}}]
\end{align}


the squared standard error in the particle position reads: 

\begin{align}
\langle (\delta x)^{2} \rangle = \frac{s^{2}}{N}
\end{align}

where $s$ is the standard deviation of the PSF and N is the number of photons collected. Next, we can introduce the pixelation noise. I will just introduce an additional term to the equation above with no justification: 

\begin{align}
\langle (\delta x)^{2} \rangle = \frac{s^{2} + \frac{a^{12}}{12}}{N}
\end{align}

where $a$ is the pixel size. Moving on, the only way to probe the contribution of shot noise and dark noise to localization uncertainty is to analyze the residual errors when fitting the theoretical point spread function.

\begin{align}
\chi^{2}(x) = \sum_{n=1}^{N} \frac{1}{\sigma_{n}^{2}}(I(n) - M(n))^{2}
\end{align}

where $M(x)$ is the raw photon counts measured, $I(x)$ is the photon count according to the model, and $\sigma$ is the expected uncertainty in the photon count. Of course, $\sigma$ is nonzero due to the presence of dark noise and shot noise: 

\begin{align}
\sigma_{n}^{2} = \sigma_{dark}^{2} + N_{n}
\end{align}

where we have substituted $N_{n}$ for the variance due to shot noise, assuming Poisson statistics. Optimal fitting requires that $d\chi^{2}/dx = 0$. Assuming that errors in counted photons are sufficiently small, the mean square error has been shown in [] to be: 

\begin{align}
\langle (\delta x)^{2} \rangle = \frac{1}{\sum (I_{i}^{'2}/\sigma_{i}^{2})}
\end{align}

However, it is much easier to approximate the sum with an integral:

\begin{align}
\langle (\delta x)^{2} \rangle = \frac{1}{\int (I_{i}^{'2}/\sigma_{i}^{2})}
\end{align}




```python

```
