import cv2 
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    frame = cv2.cvtColor(cap.read()[1],cv2.COLOR_BGR2GRAY)
    frame2 = cv2.cvtColor(cap.read()[1],cv2.COLOR_BGR2GRAY)
    
    #
    #new_image = 
    new_frame= frame - frame2
    #c2.
    cv2.imshow('Difference',new_frame)
    #cv2.imshow('Tennis',frame)
    key = cv2.waitKey(50)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()

'''
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

im = Image.open('image.jpeg').convert('L')
print(dir(im))
#im.histogram()
#plt.hist(im.histogram(), bins=100)

#plt.imshow(im)
#plt._show()

contours(im,)
'''