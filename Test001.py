import numpy as np
import cv2

path_img = '/Users/Nut_NTCH/Desktop/8.jpg'
img = cv2.imread(path_img)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
rgb = cv2.cvtColor(img,cv2.COLOR_Luv2LRGB)

# define range of blue color in HSV
lower= np.array([26,74,58])
upper = np.array([180,255,255])


# Threshold the HSV image to get only blue colors
mask = cv2.inRange(hsv, lower, upper)

contours ,_ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for c in contours:
   #x,y,w,h = cv2.boundingRect(c)
   #area = w*h
   #if area > 200000 :
      #cv2.rectangle(img , (x,y) , (x+y , y+h),(0,0,255),2)
   rect = cv2.boundingRect(c)
   x,y,w,h = rect
   area = w * h

   epsilon = 0.08 * cv2.arcLength(c, True)
   approx = cv2.approxPolyDP(c, epsilon, True)

   if area > 1000:
      #cv2.drawContours(img, [approx], -1, (0, 0, 255), 5)
      cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 5)
      area_crop = rgb[x:x+w,y:y+h]
      meanRGB = cv2.mean(area_crop)
      print(meanRGB)
      #print('approx', approx)
      #for x in range(0, len(approx)):
         #cv2.circle(img, (approx[x][0][0], approx[x][0][1]), 30, (0,0,255), -1)
# cv2.drawContours(img, contours, -1, (0,255,0), 5)

cv2.imwrite('/Users/Nut_NTCH/Desktop/test2.png',img)

# cv2.imshow('image',img)
# cv2.imshow('hsv',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()