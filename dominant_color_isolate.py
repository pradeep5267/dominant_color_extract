#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'dominant_colors_isolate'))
	print(os.getcwd())
except:
	pass

#%%
# import the necessary packages
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
import cv2
from collections import Counter
from skimage.color import rgb2lab, deltaE_cie76
import os


#%%
def RGB2HEX(color):
    return "#{:02x}{:02x}{:02x}".format(int(color[0]), int(color[1]), int(color[2]))


#%%
path = './test.jpg'

# load the image and convert it from BGR to RGB so that
# we can dispaly it with matplotlib
image = cv2.imread(path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


#%%
# show our image
plt.figure()
plt.axis("off")
plt.imshow(image)


#%%
# reshape the image to be a list of pixels
image = image.reshape((image.shape[0] * image.shape[1], 3))


#%%
# cluster the pixel intensities
clt = KMeans(n_clusters = 15)
labels = clt.fit_predict(image)


#%%
center_colors = clt.cluster_centers_
counts = Counter(labels)


#%%
ordered_colors = [center_colors[i]/255 for i in counts.keys()]
hex_colors = [RGB2HEX(ordered_colors[i]*255) for i in counts.keys()]
rgb_colors = [ordered_colors[i]*255 for i in counts.keys()]

#FOR DEBUGGING
print(hex_colors)
print(rgb_colors)
print(len(hex_colors))
print(len(rgb_colors))
#%%
neutral_colors_list = []
neutral_colors_path = './neutral_colors.txt'
ffile = open(neutral_colors_path,'r')
for lines in ffile:
    lines = lines.strip().lower()
    neutral_colors_list.append(lines)


#%%
mod_hex = hex_colors
for i in range (len(mod_hex)):
    if (mod_hex[i] in neutral_colors_list):
        mod_hex[i] = None
print(mod_hex)
        


