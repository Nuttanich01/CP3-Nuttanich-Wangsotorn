import numpy as np
from cv2 import boundingRect, cvtColor, COLOR_BGR2RGB, imwrite, inRange, COLOR_BGR2HSV, CHAIN_APPROX_SIMPLE, mean, \
    imread, resize, rectangle, RETR_TREE, findContours,imshow,waitKey

from matplotlib import pyplot as plt
path_img = '/Users/Nut_NTCH/Desktop/11.jpg'
img = imread(path_img)
img = resize(img, (400, 400))

hsvR = cvtColor(img, COLOR_BGR2HSV)
hsvG = cvtColor(img, COLOR_BGR2HSV)
rgb = cvtColor(img, COLOR_BGR2RGB)


lowerR = np.array([0, 234, 200])#0,234,98
lowerG = np.array([31,142,169]) #30,74,70
upperR = np.array([180,255,255])
upperG = np.array([180, 255, 255])

maskR = inRange(hsvR, lowerR, upperR)
maskG = inRange(hsvG, lowerG, upperG)
contours ,_ = findContours(maskR, RETR_TREE, CHAIN_APPROX_SIMPLE)
contours2,_ = findContours(maskG, RETR_TREE, CHAIN_APPROX_SIMPLE)

for c in contours:
    x1,y1,w1,h1  = boundingRect(c)
    area = w1 * h1
    a1 = int(x1 * 2)
    b1 = int(y1 * 2)
    c1 = int((x1 + w1) * 0.8)
    d1 = int((y1 + h1) * 0.8)
    if area > 10000:
        rectangle(img, (x1, y1), (x1 + w1, y1 + h1), (0, 0, 255), 2)
        rectangle(img, (a1, b1), (c1, d1), (0, 0, 255), 2)
        area_crop1 = rgb[a1:c1,b1:d1]
        meanRGB = mean(area_crop1)
        print("1")
        #print(meanRGB)
        rgb0 = list(meanRGB)
        if rgb0.index(max(rgb0))+1 == 1 : print(meanRGB)

for c in contours2:
    x2,y2,w2,h2  = boundingRect(c)
    area2 = w2 * h2
    a2 = int(x2 * 2)
    b2 = int(y2 * 2)
    c2 = int((x2 + w2) * 0.8)
    d2 = int((y2 + h2) * 0.8)

    if area2 > 10000:
        rectangle(img, (x2, y2), (x2 + w2, y2 + h2), (0, 255, 0), 2)
        rectangle(img, (a2, b2), (c2, d2), (0, 255, 0), 2)
        area_crop2 = rgb[a2:c2,b2:d2]
        meanRGB2 = mean(area_crop2)
        print("2")
        rgb0 = list(meanRGB)
        if rgb0.index(max(rgb0)) + 1 == 2: print(meanRGB)

imwrite('/Users/Nut_NTCH/Desktop/test2.png', img)

#plt.subplot(2,2,1);plt.imshow(img[:,:,::-1])
#plt.show()
#cv2.imshow('vdo',vdo)
#imshow('maskR',maskR)
#imshow('maskG', maskG)
waitKey(0)