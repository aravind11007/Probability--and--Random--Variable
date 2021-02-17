#!/usr/bin/env python
# coding: utf-8

# In[1]:


from random import randint


# In[14]:


#Here i will be creating a list'num' which consist of 6 element using randint function(which used for obtaining number from
#1 to 6 with equal probability) ,i will be repeating this process for 100000 times and will be counting the lists which statisfy
# 2 condition 1)list last number should be 6 2) count of total 6 in the list should be 3.The list which statisfy the above 
#criteria will be counted and will be divided with 100000
z=0
count=0
while z<100000:
    num=[]
    for i in range(0,6):
        num.append(randint(1,6))
    if num[-1]==6 and num.count(6)==3:
        count=count+1
    z=z+1


# In[17]:


print(f"probability of obtaining third six in the sixth throw of the die,{count/100000}")


# In[ ]:




