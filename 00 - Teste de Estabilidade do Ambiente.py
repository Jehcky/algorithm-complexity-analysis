#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
import numpy as np
from matplotlib import pyplot as plt


# In[2]:


a = 0
n=200000
t=[]
rep=1000


# In[3]:


for j in range(rep):
    tic = time.time()
    #print("time1=",time.time())
    for i in range (n):
        a+=1
    t.append(time.time()-tic)    
    #print("time2",time.time()-tic)
    #print(t)
#print(np.mean(t))
#print(np.std(t))
media = np.mean(t)
d_p = np.std(t)

print(d_p/media)


# In[4]:


plt.hist(t,20)
plt.show()


# In[5]:


plt.plot(t)
plt.show()

