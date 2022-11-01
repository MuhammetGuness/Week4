#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np

resim1 = cv2.imread("pythondeneme.jpeg")
cv2.imshow("Dağ",resim1)
print(resim1.size)
print(resim1.dtype)
print(resim1.shape)

cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:




