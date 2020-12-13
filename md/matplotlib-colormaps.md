---
layout: post
title: "Matplotlib colormaps"
date: 2020-11-17
categories: [python, matplotlib]
---

# Choosing a colormap in Matplotlib

1. **Sequential**: change in lightness and often saturation of color incrementally, often using a single hue; should be used for representing information that has ordering.

2. **Diverging**: change in lightness and possibly saturation of two different colors that meet in the middle at an unsaturated color; should be used when the information being plotted has a critical middle value, such as topography or when the data deviates around zero

3. **Cyclic**: change in lightness of two different colors that meet in the middle and beginning/end at an unsaturated color; should be used for values that wrap around at the endpoints, such as phase angle, wind direction, or time of day.

4. **Qualitative**: often are miscellaneous colors; should be used to represent information which does not have ordering or relationships.

**Note: The above paragraph and code snippets below were derived from [here](https://matplotlib.org/3.1.0/tutorials/colors/colormaps.html)


```code
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import cm
from collections import OrderedDict

cmaps = OrderedDict()
def plot_color_gradients(cmap_category, cmap_list, nrows):
    fig, axes = plt.subplots(nrows=nrows)
    fig.subplots_adjust(top=0.95, bottom=0.01, left=0.2, right=0.99)
    axes[0].set_title(cmap_category + ' colormaps', fontsize=14)

    for ax, name in zip(axes, cmap_list):
        ax.imshow(gradient, aspect='auto', cmap=plt.get_cmap(name))
        pos = list(ax.get_position().bounds)
        x_text = pos[0] - 0.01
        y_text = pos[1] + pos[3]/2.
        fig.text(x_text, y_text, name, va='center', ha='right', fontsize=10)

    # Turn off *all* ticks & spines, not just the ones with colormaps.
    for ax in axes:
        ax.set_axis_off()

```

# Sequential Colormaps


```code
cmaps['Sequential'] = [
                        'Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds',
                        'YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu',
                        'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn'
                      ]
```


```code
nrows = max(len(cmap_list) for cmap_category, cmap_list in cmaps.items())
gradient = np.linspace(0, 1, 256)
gradient = np.vstack((gradient, gradient))

for cmap_category, cmap_list in cmaps.items():
    plot_color_gradients(cmap_category, cmap_list, nrows)
```


![png](matplotlib-colormaps_files/matplotlib-colormaps_4_0.png)


# More Sequential Colormaps


```code
cmaps = OrderedDict()
cmaps['Sequential (2)'] = [
                        'binary', 'gist_yarg', 'gist_gray', 'gray', 'bone', 'pink',
                        'spring', 'summer', 'autumn', 'winter', 'cool', 'Wistia',
                        'hot', 'afmhot', 'gist_heat', 'copper'
                          ]

nrows = max(len(cmap_list) for cmap_category, cmap_list in cmaps.items())
gradient = np.linspace(0, 1, 256)
gradient = np.vstack((gradient, gradient))

for cmap_category, cmap_list in cmaps.items():
    plot_color_gradients(cmap_category, cmap_list, nrows)
```


![png](matplotlib-colormaps_files/matplotlib-colormaps_6_0.png)


# Diverging Colormaps


```code
cmaps = OrderedDict()
cmaps['Diverging'] = [
                        'PiYG', 'PRGn', 'BrBG', 'PuOr', 'RdGy', 'RdBu',
                        'RdYlBu', 'RdYlGn', 'Spectral', 'coolwarm', 'bwr', 'seismic'
                     ]

nrows = max(len(cmap_list) for cmap_category, cmap_list in cmaps.items())
gradient = np.linspace(0, 1, 256)
gradient = np.vstack((gradient, gradient))

for cmap_category, cmap_list in cmaps.items():
    plot_color_gradients(cmap_category, cmap_list, nrows)
```


![png](matplotlib-colormaps_files/matplotlib-colormaps_8_0.png)


# Cyclic Colormaps


```code
cmaps = OrderedDict()
cmaps['Cyclic'] = ['twilight', 'twilight_shifted', 'hsv']

nrows = max(len(cmap_list) for cmap_category, cmap_list in cmaps.items())
gradient = np.linspace(0, 1, 256)
gradient = np.vstack((gradient, gradient))

for cmap_category, cmap_list in cmaps.items():
    plot_color_gradients(cmap_category, cmap_list, nrows)
```


![png](matplotlib-colormaps_files/matplotlib-colormaps_10_0.png)


# Qualitative Colormaps


```code
cmaps = OrderedDict()
cmaps['Qualitative'] = [
                        'Pastel1', 'Pastel2', 'Paired', 'Accent',
                        'Dark2', 'Set1', 'Set2', 'Set3',
                        'tab10', 'tab20', 'tab20b', 'tab20c'
                       ]

nrows = max(len(cmap_list) for cmap_category, cmap_list in cmaps.items())
gradient = np.linspace(0, 1, 256)
gradient = np.vstack((gradient, gradient))

for cmap_category, cmap_list in cmaps.items():
    plot_color_gradients(cmap_category, cmap_list, nrows)
```


![png](matplotlib-colormaps_files/matplotlib-colormaps_12_0.png)


# Miscellaneous Colormaps


```code
cmaps = OrderedDict()
cmaps['Miscellaneous'] = [
                        'flag', 'prism', 'ocean', 'gist_earth', 'terrain', 'gist_stern',
                        'gnuplot', 'gnuplot2', 'CMRmap', 'cubehelix', 'brg',
                        'gist_rainbow', 'rainbow', 'jet', 'nipy_spectral', 'gist_ncar'
                         ]

nrows = max(len(cmap_list) for cmap_category, cmap_list in cmaps.items())
gradient = np.linspace(0, 1, 256)
gradient = np.vstack((gradient, gradient))

for cmap_category, cmap_list in cmaps.items():
    plot_color_gradients(cmap_category, cmap_list, nrows)
```


![png](matplotlib-colormaps_files/matplotlib-colormaps_14_0.png)


To make use of one of the above colormaps, we can create a numpy linspace object with min_color, max_color and num_color parameters. This allows to slice the colormap and choose how many colors to choose in the slice.


```code
fig, ax = plt.subplots()
viridis = cm.get_cmap('rainbow', 12)
color_ind = np.linspace(0, 0.5, 3)
min_color = 0; max_color = 1; num_color = 5
x = np.linspace(min_color, max_color, num_color)
y = [x, 2*x, 3*x]

viridis = viridis(color_ind)
for i,j in enumerate(y):
    ax.plot(x,j, color=viridis[i])
plt.show()
```


![png](matplotlib-colormaps_files/matplotlib-colormaps_16_0.png)



```code

```
