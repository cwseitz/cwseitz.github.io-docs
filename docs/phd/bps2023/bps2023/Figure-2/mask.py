from glob import glob
from skimage.io import imread, imsave
from skimage.measure import regionprops
from skimage.filters import gaussian
import matplotlib.pyplot as plt

files = glob('*.tif')
for file in files:
	im = imread(file)
	ls = file.split('.')
	ls[0] = ls[0] + '-mask'
	maskfile = 'masks/' + '.'.join(ls)
	print(maskfile)
	mask = imread(maskfile)
	regions = regionprops(mask)
	x,y = regions[0].centroid
	x = int(x); y = int(y)
	mask = mask/mask.max()
	bbox = 100
	patch = im[x-bbox:x+bbox,y-bbox:y+bbox]
	patch = gaussian(patch,sigma=1)
	imsave('out/'+file,patch)
