---
layout: post
title: "Installing the C kernel in jupyter"
date: 2020-11-17
categories: [c-programming]
---

First, we need to install the C kernel into the version of jupyter notebook that shipped with anaconda. To do that, we activate the environment, install jupyter-c-kernel via pip, change directory permissions so that it is installed within our virtual environment, then issue install_c_kernel.


```code
conda activate XXX
pip install jupyter-c-kernel
sudo mkdir /usr/local/share/jupyter
chmod -R 777 /usr/local/share/jupyter
install_c_kernel
```
