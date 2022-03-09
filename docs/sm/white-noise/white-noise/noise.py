import matplotlib.pyplot as plt
import numpy as np

sigma1 = 10
x = np.random.normal(0,sigma1,size=(10000,))

sigma2 = 100
y = np.random.normal(0,sigma2,size=(10000,))

sigma3 = 1000
z = np.random.normal(0,sigma3,size=(10000,))

x_corr = np.correlate(x,x,mode='same')
y_corr = np.correlate(y,y,mode='same')
z_corr = np.correlate(z,z,mode='same')

fig, ax = plt.subplots(2,2)

xvals, xbins = np.histogram(x,bins=10)
yvals, ybins = np.histogram(y,bins=10)
zvals, zbins = np.histogram(z,bins=10)

ax[1,1].plot(xbins[:-1],xvals,color='red')
ax[1,1].plot(ybins[:-1],yvals,color='blue')
ax[1,1].plot(zbins[:-1],zvals,color='purple')

ax[1,0].plot(x_corr/x_corr.max(), color='red',alpha=0.3)
ax[1,0].plot(y_corr/y_corr.max(), color='blue',alpha=0.3)
ax[1,0].plot(z_corr/z_corr.max(), color='purple',alpha=0.3)

ax[0,0].plot(x,color='red',alpha=0.3)
ax[0,0].plot(y,color='blue',alpha=0.3)
ax[0,0].plot(z,color='purple',alpha=0.3)

xt = np.fft.fft(x)
yt = np.fft.fft(y)
zt = np.fft.fft(z)

N = x.shape[0]
ax[0,1].plot(np.log(np.abs(xt[:N//2])),color='red',alpha=0.3)
ax[0,1].plot(np.log(np.abs(yt[:N//2])),color='blue',alpha=0.3)
ax[0,1].plot(np.log(np.abs(zt[:N//2])),color='purple',alpha=0.3)

plt.show()
