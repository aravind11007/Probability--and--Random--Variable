#!/usr/bin/env python
# coding: utf-8

# In[11]:


from random import randint
import matplotlib.pyplot as plt


# In[7]:


# here 0 indicate that tails has occured and 1 for head,so i will be generating a list with 3 three random integers
#containing 1 and 0 s only.Then i will be counting the total number of ones and zeros from that list .After that i will be
#muiltpying the total number of zeros with -1.5 and total number of ones with 2,then will be adding the two totals.The added
#sum will be placed in a list and this process will again be repeated for z=100000 times and will be obtaining the values.
#set values of list will be obtained so that repeated values will be eliminated.
z=0
values=[]
while z<1000000:
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


# A=6,B=2.5,C=-1.0,D=-4.5


# In[10]:


A=values.count(6)/z
B=values.count(2.5)/z
C=values.count(-1)/z
D=values.count(-4.5)/z


# In[28]:


x=[-4.5,-1,2.5,6.0]
y1=[A,B,C,D]
y2=[1/8,3/8,3/8,1/8]
plt.plot(x,y2,marker="*",color='red')
plt.bar(x,y1,color='Green')
plt.legend(['theoretical PMF','simulated PMF'])
plt.title('theoretical PMF vs simulated PMF')
plt.xlabel('outcome')
plt.ylabel('probability')
plt.savefig('pmf.png')


# In[30]:


x=[-4.5,-1,2.5,6.0]
y1=[A,B+A,C+B+A,D+C+B+A]
y2=[1/8,3/8+1/8,3/8+3/8+1/8,1/8+3/8+3/8+1/8]
plt.plot(x,y2,marker="*",color='red')
plt.bar(x,y1,color='Green')
plt.legend(['theoretical CDF','simulated CDF'])
plt.title('theoretical CDF vs simulated CDF')
plt.xlabel('outcome')
plt.ylabel('Cumulative probability')
plt.savefig('cdf.png')


# In[ ]:




