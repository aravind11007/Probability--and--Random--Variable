#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random 


# In[17]:


#here 0 represents the red ball,1 represent white and 2 represent black
# i will be generating a list 'BOXA' with z=1000000 elements in such a way that randomly generated number between 0 and 1 will
#be assigned with 0,1,2 values based on the condition given below
BOXA=[]
z=0
while z<1000000:
    val=random.uniform(0,1)
    if val<=.1:
        BOXA.append(0)
    elif val>.1 and val<=.7:
        BOXA.append(1)
    elif val>.7:
        BOXA.append(2)
    z=z+1


# In[18]:


# i will be generating a list 'BOXB' with z=1000000 elements in such a way that randomly generated number between 0 and 1 will
#be assigned with 0,1,2 values based on the condition given below
BOXB=[]
z=0
while z<1000000:
    val=random.uniform(0,1)
    if val<=.6:
        BOXB.append(0)
    elif val>.6 and val<=.8:
        BOXB.append(1)
    elif val>.8:
        BOXB.append(2)
    z=z+1


# In[19]:


# i will be generating a list 'BOXC' with z=1000000 elements in such a way that randomly generated number between 0 and 1 will
#be assigned with 0,1,2 values based on the condition given below
BOXC=[]
z=0
while z<1000000:
    val=random.uniform(0,1)
    if val<=.8:
        BOXC.append(0)
    elif val>.8 and val<=.9:
        BOXC.append(1)
    elif val>.9:
        BOXC.append(2)
    z=z+1


# In[20]:


# i will be generating a list 'BOXD' with z=1000000 elements in such a way that randomly generated number between 0 and 1 will
#be assigned with 0,1,2 values based on the condition given below
BOXD=[]
z=0
while z<1000000:
    val=random.uniform(0,1)
    if val<=.6:
        BOXD.append(1)
    elif val>.6:
        BOXD.append(2)
    z=z+1


# In[22]:


# next i will be calculating the total number of red balls
total_redball=BOXA.count(0)+BOXB.count(0)+BOXC.count(0)+BOXD.count(0)


# In[27]:


print(f'probability that marble is drawn from box A given it is Red marble={BOXA.count(0)/total_redball}')


# In[28]:


print(f'probability that marble is drawn from box B given it is Red marble={BOXB.count(0)/total_redball}')


# In[29]:


print(f'probability that marble is drawn from box C given it is Red marble={BOXC.count(0)/total_redball}')


# In[ ]:




