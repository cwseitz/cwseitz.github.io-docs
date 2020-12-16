```python
from IPython.core.display import display, HTML
display(HTML("<style>.container { width:50% !important; }</style>"))
```


<style>.container { width:50% !important; }</style>


### Error rate vs. Loss

I need to make an important distinct before proceeding. The loss function, which we typically take to be the cross-entropy loss, is fundamentally distinct from the error-rate. The error-rate is the fraction of testing, validation, or testing samples that we correctly predict. This is an important metric for assessing the performance of a model and also things such as overfitting.

### Regularization

A major downfall of deep networks is that they often fail to generalize. Models can be trained to perform quite well on a batch of test data but their performance dwindles when using the same model to predict a validation or test sample. This is often called overfitting. We would like a better way to train our models so that we can bring the validation error rate closer to the testing error rate i.e. to prevent overfitting. One way to achieve this is through *regularization* which defines the search for an optimum model $\Phi^{*}$ such that not all models have equal probability. This is made possible by first making the following observations

\begin{eqnarray*}
\DeclareMathOperator*{\argmin}{argmin}
\DeclareMathOperator*{\argmax}{argmax}
\Phi^* & = & \argmax_\Phi\;p(\Phi | (x_1,y_1),\ldots,(x_n,y_n)) \\
\\
 & = & \argmax_\Phi\;p(\Phi,\;(x_1,y_1),\ldots,(x_n,y_n)) \\
 \\
  & = & \argmax_\Phi\;p(\Phi)P((x_1,y_1),\ldots,(x_n,y_n)\;|\;\Phi) \\
 \\
 & = & \argmax_\Phi \; p(\Phi)\;\prod_i \mathcal{Pop}(x_i)P_\Phi(y_i|x_i) \\
 \\
  & = & \argmax_\Phi \; p(\Phi)\;\prod_i P_\Phi(y_i|x_i)
 \end{eqnarray*}

where we refer to $p(\Phi)$ as the model-prior probability and constraints on that probability define the following different forms of regularization.

### L1 Regularization

L1 regularization gets its name from the fact that we use the L1 norm of the parameter vector $\Phi$ to define our model-prior. For L1 regularization, we define the prior to be Poisson and plug it into the last expression we derived above

\begin{eqnarray*}
\DeclareMathOperator*{\argmin}{argmin}
\DeclareMathOperator*{\argmax}{argmax}
p(\Phi) & \propto & e^{-\lambda ||\Phi||_1} \;\;\;\;\;\;\;\;||\Phi||_1 = \sum_i |\Phi_i| \\
\\
\Phi^* & = & \argmax_\Phi \; \;\;p(\Phi) \prod_i P_\Phi(y_i|x_i) \\
\\
\Phi^* & = & \argmin_\Phi \; \;\;\left(\sum_i\; -\ln P_\Phi(y_i|x_i)\right) \;+ \; \;\lambda||\Phi||_1 \\
\\
\Phi^* & = & \argmin_\Phi \; \;\;\hat{\cal L}(\Phi) \;+ \; \;\frac{\lambda}{N_{\mathrm{Train}}}||\Phi||_1
\end{eqnarray*}

Notice that we take a negative log and divided by $N$ to transform it into something that looks like an average cross-entropy loss over the training set $\hat{\mathcal{L}}$ with an extra term to give us our new objective which is optimized as follows 

\begin{eqnarray*}
\Phi_i & = & \Phi_i - \eta \left(\hat{g}_i + \frac{\lambda}{N_{\mathrm{Train}}}\;\mathrm{sign}(\Phi_i)\right)
\end{eqnarray*}

For such an objective, $\Phi^*_i = 0 $ when $|g_i| <  \lambda/N_{\mathrm{Train}}$ and $g_i = -(\lambda/N_{\mathrm{Train}}) \mathrm{sign}(\Phi_i)$ otherwise.

### L2 Regularization

For L2 regularization, which is often called shrinkage, we define the model-prior to be Gaussian and use the L2 norm of the parameter vector. The argument is very similar to above and it can be shown that the objective and update equation under a Gaussian prior is 

\begin{eqnarray*}
\DeclareMathOperator*{\argmin}{argmin}
\DeclareMathOperator*{\argmax}{argmax}
\Phi^* & = & \argmin_\Phi \; \;\;\hat{\cal L}(\Phi) \;+ \; \;\frac{1}{2N\sigma^2} ||\Phi||^2
\end{eqnarray*}

$$\Phi_{i+1} = \Phi_i - \eta\hat{g}_i  - \frac{\eta}{N\sigma^2}\Phi$$

Now we can see why this is called shrinkage

$${ \Phi_{i+1}} = \Phi_i - \eta\hat{g} - \frac{\eta}{N\sigma^2}\Phi_i\;\;\;\; = {\Phi_i - \eta\hat{g} - \gamma\Phi_i}$$


```python

```
