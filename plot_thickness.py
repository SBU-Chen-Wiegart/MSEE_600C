# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 16:57:12 2022

@author: xiaoy
"""

from skimage import io
import numpy as np
import matplotlib.pyplot as plt
import os
from skimage.measure import profile_line
import matplotlib.patches as patches


path = 'C://Research//2020_xiaoyang//MoltenSalt//manuscript_prep//Second//data//surface_evo'
os.chdir(path)

'''
Start and end coordinate input
img imput
'''
start = (59,34)
end = (89,79)
img = io.imread('align_xy_z50_evo_forfig2.tif')

#X-ray attenuation plot
fig2, (ax1,ax2,ax3,ax4,ax5) = plt.subplots(1,5,figsize=(10,2),gridspec_kw={'width_ratios':[1,1,1,1,1]})
ax1.plot(profile_line(img[0],start,end))
ax2.plot(profile_line(img[1],start,end))
ax3.plot(profile_line(img[2],start,end))
ax4.plot(profile_line(img[3],start,end))
ax5.plot(profile_line(img[4],start,end))
fig2.tight_layout()

#image show
fig3,(ax1,ax2,ax3,ax4,ax5) = plt.subplots(1,5)
ax1.imshow(img[0],vmin=-0.5,vmax=4)
ax2.imshow(img[1],vmin=-0.5,vmax=4)
ax3.imshow(img[2],vmin=-0.5,vmax=4)
ax4.imshow(img[3],vmin=-0.5,vmax=4)
ax5.imshow(img[4],vmin=-0.5,vmax=4)
ax1.plot((34,79),(59,89),'r')
ax2.plot((34,79),(59,89),'r')
ax3.plot((34,79),(59,89),'r')
ax4.plot((34,79),(59,89),'r')
ax5.plot((34,79),(59,89),'r')
fig3.colorbar()



    #plt.plot((34,79),(59,89))
#-------for location -------
img = io.imread('C://Research//2020_xiaoyang//MoltenSalt//manuscript_prep//Second//data//600C_alignall_evo//align_xy_z50_evo.tif')
fig,ax = plt.subplots(1)
rec = patches.Rectangle((65,150),163,137,edgecolor='r',linewidth=1.5,fill=None)
ax.imshow(img[0],vmin=-0.5,vmax=4)
ax.add_patch(rec)

#------for images----------
#img = io.imread('C://Research//2020_xiaoyang//MoltenSalt//manuscript_prep//Second//data//surface_evo//align_xy_z50_evo_W163_H137_X65_Y150.tif')
#for i in range(len(img)):
 #   plt.imsave('C://Research//2020_xiaoyang//MoltenSalt//manuscript_prep//Second//data//surface_evo//2Dimag_SI//align_xy_z50_evo_W163_H137_X65_Y150_'+'sli'+str(i+1)+'.tiff',img[i])
    