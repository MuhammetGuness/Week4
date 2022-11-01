#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np
import matplotlib.pyplot as plt
row = 100
col = 100
img = np.zeros((row,col))
img[20:25, :] = 0.5
img[:, 20:25] = 1
plt.figure(figsize=(10,4))
plt.imshow(img)
plt.show()


# In[ ]:




