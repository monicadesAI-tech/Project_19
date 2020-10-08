#!/usr/bin/env python
# coding: utf-8

# In[1]:


import keras
import cv2
import numpy as np
import matplotlib
print (cv2.__version__)


# In[18]:


import cv2
import numpy as np

# Our sketch generating function
def sketch(image):
    # Convert image to grayscale
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Clean up image using Guassian Blur
    img_gray_blur = cv2.GaussianBlur(img_gray, (5,5), 0)
    
    # Extract edges
    canny_edges = cv2.Canny(img_gray_blur, 30, 60)
    
    # Do an invert binarize the image 
    ret, mask = cv2.threshold(canny_edges, 240, 255, cv2.THRESH_BINARY_INV)
    
    return mask


# Initialize webcam, cap is the object provided by VideoCapture
# It contains a boolean indicating if it was sucessful (ret)
# It also contains the images collected from the webcam (frame)
cap = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(1)
# Get the Default resolutions
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

while True:
    ret, frame = cap.read()
    ret1, frame1 = cap2.read()
    cv2.imshow('Original', (frame))
    cv2.imshow('Our Live Sketcher', sketch(frame))
    if cv2.waitKey(1) == 13: #13 is the Enter Key
        break
        
# Release camera and close windows
cap.release()
cap2.release()
cv2.destroyAllWindows()      


# In[ ]:




