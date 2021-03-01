#!/usr/bin/env python
# coding: utf-8

# In[1]:


from random import randint


# In[6]:


# here 0 indicate that tails has occured and 1 for head,so i will be generating a list with 3 three random integers
#containing 1 and 0 s only.Then i will be counting the total number of ones and zeros from that list .After that i will be
#muiltpying the total number of zeros with -1.5 and total number of ones with 2,then will be adding the two totals.The added
#sum will be placed in a list and this process will again be repeated for z=100000 times and will be obtaining the values.
#set values of list will be obtained so that repeated values will be eliminated.
z=0
values=[]
while z<100000:
    count0=0
    count1=0
    num=[]
    for i in range(0,3):
        num.append(randint(0,1))
    count0=num.count(0)
    count1=num.count(1)
    values.append(count0*-1.5+count1*2)
    z=z+1
randomvar=list(set(values))
randomvar.sort()


# In[8]:


print(f'The sample space of random varible X will be{randomvar}')


# In[ ]:




