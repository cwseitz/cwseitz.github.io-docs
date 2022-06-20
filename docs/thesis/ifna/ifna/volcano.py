import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from _format_ax import *

def volcano(ax,log2fc_1,log10p_1,labels_1,log2fc_2,log10p_2,labels_2,log10p_thres=130,log2fc_color_thres=0.58,log2fc_thres=0.58):

	ax.scatter(log2fc_1,log10p_1,color='red')
	ax.scatter(log2fc_2,log10p_2,color='blue')

	xmin, xmax = ax.get_xlim()
	ymin, ymax = ax.get_ylim()

	ax.vlines(log2fc_thres,ymin,ymax,color='gray',linestyle='--')
	ax.vlines(-log2fc_thres,ymin,ymax,color='gray',linestyle='--')
	ax.hlines(log10p_thres,xmin,xmax,color='gray',linestyle='--')

	for i, txt in enumerate(labels_1):
		if (log10p_1[i] >= log10p_thres) and (log2fc_1[i] >= log2fc_thres): 
			ax.annotate(txt, (log2fc_1[i], log10p_1[i]),fontsize=8)
		
	for i, txt in enumerate(labels_2):
		if (log10p_2[i] >= log10p_thres) and (log2fc_2[i] >= log2fc_thres): 
			ax.annotate(txt, (log2fc_2[i], log10p_2[i]),fontsize=8)

log10p_thres=130
log2fc_color_thres=0.58
log2fc_thres = 5

df_2h = pd.read_excel('RNASeq.xlsx',sheet_name='2h')
df_8h = pd.read_excel('RNASeq.xlsx',sheet_name='8h')
df_24h = pd.read_excel('RNASeq.xlsx',sheet_name='24h')
fig0, ax0 = plt.subplots(figsize=(8,6))
fig1, ax1 = plt.subplots(figsize=(8,6))
fig2, ax2 = plt.subplots(figsize=(8,6))


#2h
df1 = df_2h.loc[df_2h['log2FC_2h'] >= log2fc_color_thres]
df2 = df_2h.loc[df_2h['log2FC_2h'] <= -log2fc_color_thres]

log2fc_2h_1 = df1['log2FC_2h'].to_numpy()
log10p_2h_1 = -np.log10(df1['Pvalue_2h'].to_numpy())
labels_2h_1 = df1['gene_symbol'].to_list()

log2fc_2h_2 = df2['log2FC_2h'].to_numpy()
log10p_2h_2 = -np.log10(df2['Pvalue_2h'].to_numpy())
labels_2h_2 = df2['gene_symbol'].to_list()

#8h
df1 = df_8h.loc[df_8h['log2FC_8h'] >= log2fc_color_thres]
df2 = df_8h.loc[df_8h['log2FC_8h'] <= -log2fc_color_thres]

log2fc_8h_1 = df1['log2FC_8h'].to_numpy()
log10p_8h_1 = -np.log10(df1['Pvalue_8h'].to_numpy())
labels_8h_1 = df1['gene_symbol'].to_list()

log2fc_8h_2 = df2['log2FC_8h'].to_numpy()
log10p_8h_2 = -np.log10(df2['Pvalue_8h'].to_numpy())
labels_8h_2 = df2['gene_symbol'].to_list()

#24h
df1 = df_24h.loc[df_24h['log2FC_24h'] >= log2fc_color_thres]
df2 = df_24h.loc[df_24h['log2FC_24h'] <= -log2fc_color_thres]

log2fc_24h_1 = df1['log2FC_24h'].to_numpy()
log10p_24h_1 = -np.log10(df1['Pvalue_24h'].to_numpy())
labels_24h_1 = df1['gene_symbol'].to_list()

log2fc_24h_2 = df2['log2FC_24h'].to_numpy()
log10p_24h_2 = -np.log10(df2['Pvalue_24h'].to_numpy())
labels_24h_2 = df2['gene_symbol'].to_list()

volcano(ax0,log2fc_2h_1,log10p_2h_1,labels_2h_1,log2fc_2h_2,log10p_2h_2,labels_2h_2,log10p_thres=log10p_thres,log2fc_color_thres=log2fc_color_thres,log2fc_thres=log2fc_thres)
volcano(ax1,log2fc_8h_1,log10p_8h_1,labels_8h_1,log2fc_8h_2,log10p_8h_2,labels_8h_2,log10p_thres=log10p_thres,log2fc_color_thres=log2fc_color_thres,log2fc_thres=log2fc_thres)
volcano(ax2,log2fc_24h_1,log10p_24h_1,labels_24h_1,log2fc_24h_2,log10p_24h_2,labels_24h_2,log10p_thres=log10p_thres,log2fc_color_thres=log2fc_color_thres,log2fc_thres=log2fc_thres)

ax0.set_title('2h',fontsize=16)
ax1.set_title('8h',fontsize=16)
ax2.set_title('24h',fontsize=16)

format_ax(ax0,xlabel=r'$\log_{2}\; \mathrm{FC}$',ylabel=r'$-\log_{10}\;\mathrm{P}$',ax_is_box=False,label_fontsize='large')
format_ax(ax1,xlabel=r'$\log_{2}\; \mathrm{FC}$',ylabel=r'$-\log_{10}\;\mathrm{P}$',ax_is_box=False,label_fontsize='large')
format_ax(ax2,xlabel=r'$\log_{2}\; \mathrm{FC}$',ylabel=r'$-\log_{10}\;\mathrm{P}$',ax_is_box=False,label_fontsize='large')
plt.show()
