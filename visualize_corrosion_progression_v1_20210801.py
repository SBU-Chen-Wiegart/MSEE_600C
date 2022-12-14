# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 16:27:02 2021

@author: xiaoy
"""

from skimage import io
import numpy as np
import matplotlib.pyplot as plt
import glob
from scipy.signal import find_peaks
import os
from scipy import ndimage

#folder = 'D://Xiaoyin//600C_MLseg_Xiaoyang//3phase_cleaned_cut//'
#files = sorted(glob.glob(folder+'*.tiff'))
assignvalue = np.arange(20,200,2)
xy_index_list = []
img = io.imread('D://Xiaoyin//600C_MLseg_Xiaoyang//quantification_result//img_z100_changepixelvalue.tif') #img is all the insitu data at z=100
material = np.argwhere(img[0]==150) #150 is the pixel value for corroded Ni-20Cr
z = img.shape[0]
y = img.shape[1]
x = img.shape[2]
newimg = np.zeros([y,x])
for m in material: #make the output image corroded Ni-20Cr pixel value at 150
    newimg[m[0],m[1]] = 150
for yi in range(y):
    for xi in range(x):
        xy_index_list.append((yi,xi))
for zi in range(z-1): #compare the consecutive image to check if noncorroded Ni-20Cr beomes pore and assign a pixel value
    for xy in xy_index_list:
        
        if img[zi+1,xy[0],xy[1]] != img[zi,xy[0],xy[1]]:
            newimg[xy[0],xy[1]] = assignvalue[zi]
            xy_index_list.remove(xy)
            print(str(zi)+str(xy))
        else:
            print('done'+str(zi)+str(xy))
        '''
        if img[zi+2,xy[0],xy[1]] == 1 and img[zi+1,xy[0],xy[1]] == 1 and img[zi,xy[0],xy[1]] == 150:
            newimg[xy[0],xy[1]] = assignvalue[zi]
            xy_index_list.remove(xy)
            print(str(zi)+str(xy))
        else:
            print('done'+str(zi)+str(xy))
            '''