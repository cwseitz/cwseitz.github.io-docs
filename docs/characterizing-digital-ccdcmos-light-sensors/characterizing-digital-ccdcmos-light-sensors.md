### Introduction

This post is dedicated to covering the theoretical characterization of digital light sensors and their impact on scientific experiments. Sensors operate by exposing a pixel array to an incoming light signal during the *exposure time* and accumulating charge units at each pixel proportional to the total photo irradiance during exposure. Charge units are then converted into a voltage, amplified, and ultimately converted to a digital signal by an analog to digital converter (ADC).

Three factors limit the accuracy of any imaging experiment: pixel size (spatial resolution), exposure time (temporal resolution), and the signal-to-noise ratio (SNR). Here, we will discuss how a pixel array spatially downsamples the incoming light signal as well as the relation between time resolution and the signal-to-noise ratio (SNR). Ultimately, we will be left with the language necessary to characterize the accuracy of a given measurement by a particular sensor.

### Spatial Resolution

In classical optics, we speak of continuous intensity profiles and sometimes can write down analytical functions that describe those profiles. Digital sensors are by definition discrete and only sample those continuous profiles at a well defined spatial frequency - the pixel size. I want to begin by considering the best possible sensor we can imagine: one with an infinitely small pixel area i.e. infinite resolution. This kind of sensor could reproduce an intensity profile exactly and because of the infinitely small pixel size, the intensity $W$ is constant over the area of the pixel. From the perspective of quantum optics, the intensity at a particular pixel is:

\begin{equation*}
W = \mu_{p}\frac{\hbar\omega}{At_{exp}}
\end{equation*}

where $\mu_{p}$ is the number of photons which have arrived at the pixel, $A$ is the area of the pixel and $t_{exp}$ is the exposure time. If we write down $W$ for all space then we exactly reproduced the incoming light signal. However, we know it's impossible to build this kind of sensor and real sensors have a relatively large finite pixel area $A$. This means that the intensity profile is not constant over the pixel and $W$ is the calculated via the integral:

\begin{equation*}
W = \int I(x,y)dA 
\end{equation*}

Now we must replace $W$ in our first equation with the integral

\begin{equation*}
\mu_{p} = W\frac{At_{exp}}{\hbar\omega} \rightarrow \mu_{p} = \frac{t_{exp}}{\hbar\omega}\int I(x,y)dA 
\end{equation*}

This mean number of photons would then produce a number of charge units which would be converted to a voltage and quantized by the ADC. The need for this integral over the pixel is exactly why spatial information is lost in the imaging process. Intensity gradients over the pixel area are not captured: only the *sum* of the intensity is captured. For example, a particle displacing a distance $\epsilon << a$ where $a$ is the pixel dimension, would result in little to no change in the intensity profile of the image. Also, low spatial resolution results in the inability to distinguish objects smaller than the pixel size; however, that topic is covered in more detail in **this** post on diffraction limited optics.


### Temporal Resolution and the SNR

In the above paragraphs the exposure time was used to calculate the intensity a light signal at a particular pixel. As a rule of thumb, low exposure times allow increased frame rates so faster processes can be captured but also decrease the amount of light that can be captured during exposure. This is clear from the last expression: the number of photons is proportional to the exposure time. At first, it might seem like this just results is dimmer images; however, the real reason short exposure times are a problem stem from the resulting signal-to-noise ratio (SNR). To see why that is so, we need to discuss the presence of noise in a digital CCD/CMOS sensor.


### Noise Model 

We have already mentioned that the charge units accumulated by the photo irradiance are converted into a voltage, amplified, and lastly converted to a digital signal. What we have not addressed, however, is how noise enters into the picture during this process (pun intended). There are three types of noise to consider: dark noise, shot noise, and quantization noise. Shot noise is nothing more than photon statistics - the number of photons detected will be poisson distributed. Quantization noise can be modeled via a normal distribution with zero mean. In the presence of noise, the mean number of photons at a pixel is modified to: 

\begin{equation*}
\mu = K(\mu_{dark} + \eta \mu_{p})
\end{equation*}

where $\eta$ is the *quantum efficiency* and $K$ is called the *overall system gain* and $\mu_{dark}$ is a shift in the mean due to dark noise. Dark noise stems from dark current which is a small electric current that flows through the sensor even in the absence of light. The quantum efficiency represents the fact that only a fraction of photons will be detected due to the laws of quantum mechanics. Next, we consider the variance of photon numbers arriving at a pixel. Fluctuations from the mean value come from all three noise sources:

\begin{equation*}
\sigma^{2} = K^{2}(\sigma_{d}^{2} + \sigma_{s}^{2}) + \sigma_{q}^{2}
\end{equation*}

The SNR is commonly defined as the ratio of the mean signal to its standard deviation. Therefore, after subtracting the shift in the mean due to dark noise we have: 

\begin{equation*}
SNR = \frac{\mu - K\mu_{dark}}{\sigma} = \frac{\eta\mu_{p}}{\sigma_{d}^{2} + \sigma_{q}^{2}/K^{2} + \eta\mu_{p}}
\end{equation*}

We already know that the mean number of photons detected is directly proportional to the exposure time. Let's look at the limits of this expression with low and high photon numbers:

\begin{equation*}
SNR = \begin{cases}
    \sqrt{\eta \mu_{p}}, & \eta \mu_{p} >> \sigma_{d}^{2} + \sigma_{q}^{2}/K^{2} \\
    \frac{\eta\mu_{p}}{\sigma_{d}^{2} + \sigma_{q}^{2}/K^{2}}, & \eta \mu_{p} << \sigma_{d}^{2} + \sigma_{q}^{2}/K^{2}
\end{cases}
\end{equation*}

We see that at low photon numbers the SNR increases linearly with mean photon number and at high photon numbers it increases as the square root of mean photon number. Since, $\mu_{p}$ is linearly dependent on $t_{exp}$, the same can be said of the exposure time.
