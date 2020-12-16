```python
from IPython.core.display import display, HTML
display(HTML("<style>.container { width:50% !important; }</style>"))
```


<style>.container { width:50% !important; }</style>


### Sequence to sequence learning

One method developed by Sutskever et al in 2015 is a sequence to sequence (seq2seq) method for machine translation. As will all seq2seq translation tasks, we want to estimate distribution over the output sequence given the input sequence

\begin{eqnarray}
P_{\Phi}(w_{1},..,w_{T_{in}}|w_{1},..,w_{T_{in}})
\end{eqnarray}

We usually estimate this probability distribution by using autoregression which is realized with a RNN 

\begin{eqnarray}
P_{\Phi}(w_{1},..,w_{T_{in}}|w_{1},..,w_{T_{in}}) = \Pi_{t=0}^{T} P_{\Phi}(w_{t}|\overset\leftarrow{h_{in}}[1,J],w_{0}...w_{t-1})
\end{eqnarray}

Notice there is an unfamiliar term $\overset\leftarrow{h_{in}}[1,J]$ we are conditioning on. This brings us to the **encoder**.

#### The encoder

Before we can compute the distribution above via autoregression, we encode the sentence into a **thought-vector**. The thought-vector is a vector of numbers meant to represent the meaning of a sequence of words. We assume that it is possible to encode the essence of a sentence - something that is invariant from language to language. 

For this architecture, the thought vector representation is computed right-to-left or the last word comes first in the thought vector. As you can see in the equation above we typically represent such a thought vector as $\overset\leftarrow{h_{in}}[1,J]$ and it is the final hidden state in our encoding network.

#### Computing probabilties

Now that we have established what the thought-vector is and its role, we can move on to actually doing the autoregression. As mentioned above, the autoregression is implemented as an RNN from which we read out probabilities $ P_{\Phi}(w_{t}|\overset\leftarrow{h_{in}}[1,J],w_{0}...w_{t-1})$ according to

\begin{equation*}
\DeclareMathOperator*{\softmax}{softmax}
P(w_{t_{out}}|\overset\leftarrow{h_{in}}[1,J], w_{1},..,w_{t_{out}-1}) = \underset{w_{t_{out}}}{\softmax} e[w_{t_{out}},J]h_{out}[t_{out}-1,J] 
\end{equation*}

where $e$ is the encoding for a particular word and $h$ is the hidden state at that point in the network. 

#### The decoder

For each element of the sequence, we now have a probability distribution over the possible output words. The output sequence we get depends on how we utilize these probabilities for decoding. One way is called the **greedy-decoder** which is an autoregression conditioned on the thought-vector that selects each word $w_{t}$ in the translation that has the maximum probability. 

\begin{eqnarray}
\DeclareMathOperator*{\argmax}{argmax}
w_{t} = \underset{w_{t}}{\argmax}P(w_{t}|\overset\leftarrow{h_{in}}[1,J], w_{1},..,w_{t-1})
\end{eqnarray}

This is distinct from a decoder that would find the sentence with a *globally* maximum probability.


### Learning to align and translate

In another method, the model above is modified such that the output sequences are *aligned* with input sequences by a form of **attention**. In the context of alignment, the attention computes the strength of the connection between a word in the output $w_{t_{out}}$ and a word in the input $w_{t_{in}}$. This is especially useful because order is not always preserved from language to language.

#### The encoder

The model bares similarity in its structure to the one presented above except that the encoder is changed to a bi-directional RNN. In a bi-directional RNN, we run the network left-to-right and right-to-left and concatenate the hidden vectors produced at every $t$ to produce $\overset\leftrightarrow{h_{in}}[t_{in},J]$. 

Then, we begin the autoregression by concatenating $\overset\rightarrow{h_{in}}[T_{in},J/2]$ and $\overset\leftarrow{h_{in}}[0,J/2]$ to produce $\overset\rightarrow{h_{in}}[t_{in},J]$ which is fed into the left-to-right RNN similar to the previous model

#### The decoder

The decoder is where the main differences are because we need a way to implement an attention mechanism that facilitates alignment of the input and output sequence. But first, I will write the general procedure executed by the decoding RNN

\begin{eqnarray}
\DeclareMathOperator*{\RNN}{RNN}
\overset\rightarrow{h_{out}}[t_{out},J] = \RNN(\overset\rightarrow{h_{out}}[t_{out},J], e[w_{t_{out}},I], \color{red}{\hat{h}_{in}[t_{out},J]})
\end{eqnarray}


where $\hat{h}_{in}[t_{out},J]$ is added to provide information for the alignment. To get that information, we construct the following $\alpha$

\begin{eqnarray}
\DeclareMathOperator*{\softmax}{softmax}
\alpha[t_{in},t_{out}] = \underset{w_{t_{in}}}{\softmax} e[w_{t_{out}},J]\overset\leftrightarrow{h_{in}}[t_{in},J]
\end{eqnarray}

In words, we compute the softmax of the inner product of the embedding of the word we most recently produced $w_{t_{out}}$ and the encoding at all input positions. In effect, this gives us a probability distribution over input positions for each word that we produce at $t_{out}$. Basically that tells us where to look in the input when generating $w_{t_{out}}$.

We then multiply each slice $t_{out}$ of the association matrix with the entire matrix $\overset\leftrightarrow{h_{in}}[T_{in},J]$ from the encoder step to give us a new matrix $\hat{h}_{in}[T_{out},J]$. This is done for every $t_{out}$ giving us the relevant parts of the encoder to produce  $w_{t_{out}}$. 

\begin{eqnarray}
\color{red}{\hat{h}_{in}[t_{out},J]} = \alpha[t_{out},T_{in}]\overset\leftrightarrow{h_{in}}[T_{in},J]
\end{eqnarray}


### Attention is all you need

In the paper *Attention is all you need* published by researchers at Google Brain in 2017, a new architecture called the **transformer** was developed based on this idea of attention. This architecture outperforms LSTMs, recurrent networks, and gated recurrent networks. The primary pitfall of these methods is that they rely on sequential computation lacking any form of a parallelization. On the other hand, the transformer completely scraps the recurrence, relying on attention alone, and allowing for parallelization and improved computation time.

### Transformer heads & self-attention

For each position $t$ or position in the sentence, we construct an **attention** between that position and the other positions in the sentence. You can think of this as a weighted graph between the positions in the sentence. We store this information in the tensor $\alpha[k,t_{1},t_{2}]$ - which contains the weight of attention from words $t_{1}$ to $t_{2}$ with **head label** $k$. The head is just a label that describes their relationship.

### The encoder

Each layer in the transformer has the same shape $L[T,J]$ which contains a time index which could be a particular word in a sentence and for each word we have the vector $L[t,J]$. It is pretty efficient on a modern machine because the transfomer can compute layer $L_{l+1}[T,J]$ from $L_{l}[T,J]$ in $O(\ln(TI))$ time by using a tree of additions.  

### The decoder

Each layer in the transformer has the same shape $L[T,J]$ which contains a time index which could be a particular word in a sentence and for each word we have the vector $L[t,J]$. It is pretty efficient on a modern machine because the transfomer can compute layer $L_{l+1}[T,J]$ from $L_{l}[T,J]$ in $O(\ln(TI))$ time by using a tree of additions.  

### Query-key attention 

With query-key attention, for each of our words $t$ and each of its heads $k$, we compute

\begin{eqnarray}
\DeclareMathOperator*{\Query}{Query}
\DeclareMathOperator*{\Key}{Key}
\Query_{l+1}[k,t,i] &=& W_{\mathcal{l}+1}^{Q}[k,i,J]L_{l}[t,J] \\
\Key_{l+1}[k,t,i] &=& W_{l+1}^{K}[k,i,J]L_{l}[t,J] \\
\end{eqnarray}



```python

```
