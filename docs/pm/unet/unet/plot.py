import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from glob import glob

fig, ax = plt.subplots(2,3)

back_precision_train = 'back-precision-train.csv'
back_precision_valid = 'back-precision-valid.csv'
back_recall_train = 'back-recall-train.csv'
back_recall_valid = 'back-recall-valid.csv'

bound_precision_train = 'bound-precision-train.csv'
bound_precision_valid = 'bound-precision-valid.csv'
bound_recall_train = 'bound-recall-train.csv'
bound_recall_valid = 'bound-recall-valid.csv'

interior_precision_train = 'interior-precision-train.csv'
interior_precision_valid = 'interior-precision-valid.csv'
interior_recall_train = 'interior-recall-train.csv'
interior_recall_valid = 'interior-recall-valid.csv'

def func(series, spacing=32):
    arr = series.to_numpy()
    size = int(arr.shape[0]/spacing)
    out = np.zeros((size,))
    for i in range(1,size+1):
        start = (i-1)*spacing
        stop = i*spacing
        print(start,stop)
        out[i-1] = np.mean(arr[start:stop])
    print(out)
    return out
    

ax[0,0].plot(func(pd.read_csv(back_precision_train)['Value']), label='Precision', color='cyan')
ax[1,0].plot(func(pd.read_csv(back_precision_valid)['Value'], spacing=8), label='Precision', color='cyan')
ax[0,0].plot(func(pd.read_csv(back_recall_train)['Value']), label='Recall', color='blue')
ax[1,0].plot(func(pd.read_csv(back_recall_valid)['Value'], spacing=8), label='Recall', color='blue')
ax[1,0].set_xlabel('Epoch')
ax[1,1].set_xlabel('Epoch')
ax[1,2].set_xlabel('Epoch')
fontsize=10
ax[0,0].set_title('Background', fontsize=fontsize)
ax[0,1].set_title('Boundary', fontsize=fontsize)
ax[0,2].set_title('Interior', fontsize=fontsize)
ax[0,0].set_ylabel('Training', fontsize=fontsize)
ax[1,0].set_ylabel('Validation', fontsize=fontsize)


ax[0,1].plot(func(pd.read_csv(bound_precision_train)['Value']), label='Precision', color='cyan')
ax[1,1].plot(func(pd.read_csv(bound_precision_valid)['Value'], spacing=8), label='Precision', color='cyan')
ax[0,1].plot(func(pd.read_csv(bound_recall_train)['Value']), label='Recall', color='blue')
ax[1,1].plot(func(pd.read_csv(bound_recall_valid)['Value'], spacing=8), label='Recall', color='blue')

ax[0,2].plot(func(pd.read_csv(interior_precision_train)['Value']), label='Precision', color='cyan')
ax[1,2].plot(func(pd.read_csv(interior_precision_valid)['Value'], spacing=8), label='Precision', color='cyan')
ax[0,2].plot(func(pd.read_csv(interior_recall_train)['Value']), label='Recall', color='blue')
ax[1,2].plot(func(pd.read_csv(interior_recall_valid)['Value'], spacing=8), label='Recall', color='blue')


plt.tight_layout()
plt.legend()
plt.show()









