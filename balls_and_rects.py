# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 12:27:13 2020

@author: Anna Galsanova
"""

import matplotlib.pyplot as plt
import numpy as np
from skimage.measure import label, regionprops
from skimage import color

image = plt.imread("balls_and_rects.png")
binary = image.copy()[:, :, 0]
binary[binary > 0] = 1
image = color.rgb2hsv(image)[:, :, 0]

def centroid(lb, label=1):
    pos = np.where(lb == label)
    cy = np.mean(pos[0])
    cx = np.mean(pos[1])
    if cy == cx:
        return 1
    return 0

def find_colors(arr):
    c1 = 0
    c2 = 0
    c3 = 0
    c4 = 0
    c5 = 0
    
    for c in arr:
        if c < 0.06:
            c1 += 1
        if c > 0.06 and c < 0.2:
            c2 += 1
        if c > 0.2 and c < 0.42:
            c3 += 1
        if c > 0.42 and c < 0.62:
            c4 += 1
        if c > 0.62:
            c5 += 1
    print("Orange:", c1, "Yellow:", c2, "Green:", c3, "Blue:", c4, "Magenta:", c5)

labeled = label(binary)
print("All figures:", np.max(labeled))

colors = []
balls = []
rects = []

for region in regionprops(labeled):
    circ = region.perimeter ** 2 / region.area
    bb = region.bbox
    val = np.max(image[bb[0]:bb[2], bb[1]:bb[3]])
    colors.append(val)
    if centroid(region.image) == 0:
        rects.append(val)
    else:
        balls.append(val)

colors.sort()
rects.sort()
balls.sort()
# print(colors)

print("Balls:", len(balls))
find_colors(balls)
# print(balls)
print("Rects:", len(rects))
find_colors(rects)
# print(rects)

plt.figure()
plt.plot(np.diff(colors), 'o')
plt.figure()
plt.imshow(image)
plt.show()