import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import re
from sklearn import preprocessing
from sklearn.decomposition import PCA
from matplotlib import cm


files = sorted(os.listdir('features'))

new_feature_names = {

    'feature 1': 'dist_to_outline',
    'feature 2': 'dist_to_cell_centroid',
    'feature 3': 'dist_to_nuc_centroid',
    'feature 4': 'rad_5',
    'feature 5': 'rad_10',
    'feature 6': 'rad_15',
    'feature 7': 'rad_25',
    'feature 8': 'rad_50',
    'feature 9': 'rad_75',
    'feature 10': 'frac_20',
    'feature 11': 'frac_40',
    'feature 12': 'frac_80',
    'feature 13': 'frac_120',
    'feature 14': 'mean_dist',
    'feature 15': 'std_dist',
    'feature 16': 'var_dist',

}

classes = {

'6015':'No diabetes',
'6028':'T2D',
'6030':'No diabetes',
'6060':'No diabetes',
'6110':'T2D',
'6197':'Autoab Pos',
'6234':'No diabetes',
'6252':'T2D',
'6267':'Autoab Pos',
'6319':'T1D',
'6324':'T1D',
'6362':'T1D',
'6438':'T1D',
'6456':'T1D'

}

df = pd.DataFrame([])

for file in files:

    this_df = pd.read_csv('features/' + file)
    this_df.rename(columns=new_feature_names, inplace=True)
    this_df = this_df.assign(group=classes[file[:4]])
    this_df = this_df.assign(file=file)
    this_df = this_df.loc[:, ~this_df.columns.str.contains('^Unnamed')]
    df = pd.concat([df, this_df])

"""
Print data summary
"""

df_t1d = df.loc[df['group'] == 'T1D']
df_ctrl = df.loc[df['group'] == 'No diabetes']

u = df_ctrl[['file', 'label']].drop_duplicates()
v = df_t1d[['file', 'label']].drop_duplicates()
print('Control cells: ', u.shape[0])
print('T1D cells: ', v.shape[0])

"""
Boxplot Sanity Check
"""

fig, ax = plt.subplots()


counts_t1d = df_t1d.groupby(['label', 'file', 'group']).size().reset_index(name='count')
counts_ctrl = df_ctrl.groupby(['label', 'file', 'group']).size().reset_index(name='count')

ax.boxplot([counts_ctrl['count'], counts_t1d['count']], labels=['CTRL', 'T1D'])
ax.set_ylabel('miRNA-146 Count')
plt.show()


# """
# PCA
# """
#
# #preprocessing
# def preprocess(df):
#
#     x = df.values
#     min_max_scaler = preprocessing.MinMaxScaler()
#     x_scaled = min_max_scaler.fit_transform(x)
#     df = pd.DataFrame(x_scaled)
#
#     return df
# k = list(new_feature_names.values())
#
# df_t1d = preprocess(df_t1d[k])
# df_ctrl = preprocess(df_ctrl[k])
# df_t1d.columns = k
# df_ctrl.columns = k
#
# t1d = df_t1d.to_numpy()
# t1d_pca = PCA(n_components=2)
# t1d_pca.fit(t1d)
# t1d = t1d_pca.transform(t1d)
#
# ctrl = df_ctrl.to_numpy()
# ctrl_pca = PCA(n_components=2)
# ctrl_pca.fit(ctrl)
# ctrl = ctrl_pca.transform(ctrl)
#
# plt.scatter(t1d[:,0], t1d[:,1], color='red')
# plt.scatter(ctrl[:,0], ctrl[:,1], color='blue')
# plt.show()
#
# fig, ax = plt.subplots()
# ax.plot(t1d_pca.components_[0], color='red', label='T1D PC1')
# ax.plot(ctrl_pca.components_[0], color='blue', label='CTRL PC1')
# ax.plot(t1d_pca.components_[1], linestyle='--', color='red', label='T1D PC2')
# ax.plot(ctrl_pca.components_[1], linestyle='--', color='blue', label='CTRL PC2')
# ax.xaxis.set_ticks(np.arange(0, len(k), 1))
# ax.set_xticklabels(k, rotation=90)
# plt.tight_layout()
# plt.legend()
# plt.show()
#
#
# fig, ax = plt.subplots()
# ax.hist(df_t1d['mean_dist'], color='red', label='T1D')
# ax.hist(df_ctrl['mean_dist'], color='blue', label='CTRL')
# plt.legend()
# plt.show()
