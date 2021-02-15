#!/usr/bin/env python
# coding: utf-8

# In[47]:


from random import random
from random import seed
import matplotlib.pyplot as plt


# In[39]:


#Here p=.05 which is the probability that the bulb is defective,so i will generate 5 random numbers between 0 and 1 if the
#generated number is below .05 i will assign it as 1 and if it is above .05 i will assign it as 0 so i will have a list with 5
#elements .I will repeat this experiment z=1000000 times and will count sum of the list each time .Based on the number of ones 
# i will store it in different variable like prob0 ,prob1,prob2 etc
seed(1)
z=0
prob0=0
prob1=0
prob2=0
prob3=0
prob4=0
prob5=0
while z<1000000:
#Based on the probability of .05 i will generate a list consisting of 5 numbers
    num=[]
    for i in range(0,5):
        x=random()
        if x<.05:
            num.append(1)
        else:
            num.append(0)
#based on the number of ones sorting is happening
    if sum(num)==0:
        prob0=prob0+1
    elif sum(num)==1:
        prob1=prob1+1
    elif sum(num)==2:
        prob2=prob2+1
    elif sum(num)==3:
        prob3=prob3+1
    elif sum(num)==4:
        prob4=prob4+1
    elif sum(num)==5:
        prob5=prob5+1
    z=z+1


# # P(NONE)

# In[43]:


#To calculate P(none),i will be counting the number of list in which sum=0,therefore
print(f"Probability of getting zero defective bulb is,{prob0/z}")


# # P(not more than one)
# 

# In[44]:


#To calculate P(not more than one),i will be counting the number of list in which sum=0 and sum=1,therefore
print(f"Probability of getting not more than one defective bulb is,{(prob0+prob1)/z}")


# # P(more than one)

# In[45]:


#To calculate P( more than one),i will be counting the number of list in which sum=2,sum=3,sum=4 and sum=5,therefore
print(f"Probability of getting  more than one defective bulb is,{(prob2+prob3+prob4+prob5)/z}")


# # P(atleast one)

# In[46]:


#To calculate P( atleast),i will be counting the number of list in whichsum=1, sum=2,sum=3,sum=4 and sum=5,therefore
print(f"Probability of getting  more than one defective bulb is,{(prob1+prob2+prob3+prob4+prob5)/z}")


# # plotting CDF
# 

# In[54]:


y=[prob0,prob0+prob1,prob0+prob1+prob2,prob0+prob1+prob2+prob3,prob0+prob1+prob2+prob3+prob4,prob0+prob1+prob2+prob3+prob4+prob5]
x=[0,1,2,3,4,5]
plt.bar(x,y,width=.8)
plt.title('CDF')
plt.xlabel("Number of defective bulb")
plt.ylabel("Cumulative probability")


# # plotting PMF

# In[55]:


y=[prob0/z,prob1/z,prob2/z,prob3/z,prob4/z,prob5/z]
x=[0,1,2,3,4,5]
plt.bar(x,y,width=.8,color='red')
plt.title('PMF')
plt.xlabel("Number of defective bulb")
plt.ylabel(" probability")


# In[ ]:




