#!/usr/bin/env python
# coding: utf-8

# In[24]:


import random
import matplotlib.pyplot as plt


# In[22]:


z=0
count=0
while z<1000000:
    list1=[]
    X=random.uniform(-1,1)
    list1.append(X)
    Y=random.uniform(-1,1)
    list1.append(Y)
    list2=sorted(list1)
    if list2[-1]<.5:
        count+=1
    z+=1


# In[23]:


print(f'Probability that max(X and Y)<.5 is {count/z}')


# In[32]:


x=['simulated','theoretical']
y=[count/z,9/16]
plt.ylim(0,.6)
plt.title('simulated vs theoretical')
plt.ylabel('probability')
plt.bar(x,y,color=['red','blue'])
plt.savefig('simulated vs theoretical.png')


# In[19]:


y


# In[ ]:




