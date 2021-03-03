#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random 


# In[5]:


#1 represents the person is right handed and 0 represents the person is left handed
#i will generating a list with 10 elements with 1 and 0 in such way that the randomly generated number between 1 and 0
# if it is less that .9(probability that person is right handed) it will be assigned as 1 and 0 for number greater than .9
# and i will be doing this z=1000000 times .After each iteration if count of ones is less than or equal to 6 i will be 
#counting that 
z=0
count1=0
while z<1000000:
    num=[]
    for i in range(0,10):
        value=random.uniform(0,1)
        if value<=.9:
            num.append(1)
        elif value>9:
            num.append(0)
    if num.count(1)<=6:
        count1+=1
    z=z+1


# In[7]:


print(f'probability that at most 6 of a random sample of 10 are right-handed is:{count1/z}')


# In[ ]:




