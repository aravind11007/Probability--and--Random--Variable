#!/usr/bin/env python
# coding: utf-8

# In[35]:


from random import randint
import matplotlib.pyplot as plt


# # P(Number greater than 4)

# In[36]:


#i will generating 2 random integers list between 1 and 6(including 1 and 6).Then if 5 and 6 are not included in the list
#then count0 will be increased by 1 .If 5 or 6 is in the list and sum of the list if less than 11,i will increase the
#count1 by 1 and if sum of the list is greater than 10 and number of times the 5 repeated is 2,then count2 will be increased
# by 1.This process will be repeated for z=1000000
z=0
count0=0
count1=0
count2=0
while z<1000000:
    num=[]
    for i in range(2):
        num.append(randint(1,6))
    if 5 not in num and 6 not in num:
        count0=count0+1
    elif (num.count(5)==1 or num.count(6)==1)and sum(num)<11:
        count1=count1+1
    elif sum(num)>10 or num.count(5)==2:
        count2=count2+1
    z=z+1
    


# In[37]:


x=[0,1,2]
y=[count0/z,count1/z+count0/z,count2/z+count0/z+count1/z]
plt.bar(x,y,color='red')
plt.title('Simulated CDF')
plt.xlabel("outcome")
plt.ylabel("cumulative probability")
plt.savefig("simulated CDF")


# In[38]:


x=[0,1,2]
y=[count0/z,count1/z,count2/z]
plt.bar(x,y,color='red')
plt.title('Simulated PMF')
plt.xlabel("outcome")
plt.ylabel("probability")
plt.savefig("simulated PMF")


# # Six appears one at-least one die

# In[39]:


#i will be generating 2 random integer list inbetween 1 and 6(including 1 and 6).Then if 6 is in the list atleast one time
#count1 will be increased by 1 and if 6 is not in the list count0 will be increased by 1
z=0
count0=0
count1=1
while z<1000000:
    num1=[]
    for i in range(0,2):
        num1.append(randint(1,6))
    if 6 in num1:
        count1+=1
    else:
        count0+=1
    z+=1


# In[40]:


x=[0,1]
y=[count0/z,count1/z+count0/z]
plt.bar(x,y,color='green')
plt.title('Simulated CDF')
plt.xlabel("outcome")
plt.ylabel("cumulative probability")
plt.savefig("simulated CDF(2)")


# In[41]:


x=[0,1]
y=[count0/z,count1/z]
plt.bar(x,y,color='brown')
plt.title('Simulated PMF')
plt.xlabel("outcome")
plt.ylabel("probability")
plt.savefig("simulated PMF(2)")


# In[ ]:





# In[ ]:




