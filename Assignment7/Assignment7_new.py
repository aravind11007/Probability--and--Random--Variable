#!/usr/bin/env python
# coding: utf-8

# In[11]:


import random
import matplotlib.pyplot as plt


# In[12]:


#Here i will be generating a random number between 0 and 1,if it is greater than .5 i will be assigning it as 1(head occured)
# if it is less than .5 i will assign it as 0(tail happenend).I will be repeating this 3 times as the coin is tossed 3 times.
#this experiment is repeated z=5000000
z=0
list1=[]
while z<5000000:
    num1=random.random()
    if num1>.5:
        x0=2
    else:
        x0=-1.5
    num2=random.random()
    if num2>.5:
        x1=x0+2
    else:
        x1=x0-1.5
    num3=random.random()
    if num3>.5:
        x2=x1+2
    else:
        x2=x1-1.5
    list1.append(x2)
    z+=1
list2=list(set(list1))    
list2.sort()


# In[13]:


print(f'The sample space of random varible X2 will be{list2}')


# In[14]:


# A=6,B=2.5,C=-1.0,D=-4.5


# In[24]:


A=list1.count(6)/z
B=list1.count(2.5)/z
C=list1.count(-1)/z
D=list1.count(-4.5)/z


# In[27]:


x=[-4.5,-1,2.5,6.0]
y1=[A,B,C,D]
y2=[1/8,3/8,3/8,1/8]
plt.bar(x,y1,color='green')
plt.plot(x,y2,marker="*",color='red')
plt.legend(['theoretical PMF','simulated PMF'])
plt.title('theoretical PMF vs simulated PMF')
plt.xlabel('outcome')
plt.ylabel('probability')


# In[26]:


x=[-4.5,-1,2.5,6.0]
y1=[A,B+A,C+B+A,D+C+B+A]
y2=[1/8,3/8+1/8,3/8+3/8+1/8,1/8+3/8+3/8+1/8]
plt.plot(x,y2,marker="*",color='red')
plt.bar(x,y1,color='Green')
plt.legend(['theoretical CDF','simulated CDF'])
plt.title('theoretical CDF vs simulated CDF')
plt.xlabel('outcome')
plt.ylabel('Cumulative probability')


# In[ ]:




