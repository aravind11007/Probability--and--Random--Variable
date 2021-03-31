#!/usr/bin/env python
# coding: utf-8

# In[59]:


from random import randint
import matplotlib.pyplot as plt


# In[67]:


#Entering the number of digits to be counted
k=int(input('Enter the number of digits to be considered:'))
dup_k=k


# In[68]:


#simulated value
simu_list=[]
while k>0:
    z=0
    count=0
    while z<100000:
        list1=[]
        for i in range(0,k):
            num=randint(0,9)
            list1.append(num)
        if 0 not in list1 and 5 not in list1 and 9 not in list1:
            count+=1
        z+=1
    simu_list.append(count/z)
    simu_list.sort(reverse=True)
    k-=1


# In[69]:


#Theoretical value
theo_list=[]
for i in range(1,dup_k+1):
    theo_list.append(.7**i)


# In[70]:


x=list(range(1,len(simu_list)+1))
plt.xlabel("Number of digits")
plt.ylabel("probability")
plt.title("simulated vs theoretical")
plt.stem(x,simu_list)
plt.plot(x,theo_list,color='red',linestyle="--")
plt.legend(['Theoretical','simulated'])
plt.savefig("theoretical vs simulated")


# In[ ]:





# In[ ]:




