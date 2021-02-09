#!/usr/bin/env python
# coding: utf-8

# let X∈(0,1,2)
# where,
# X=0 be red marble,
# X=1 be white marble and
# X=2 be black marble
# 

# A,B,C,D be the four boxes

# In[126]:


import numpy as np
import random


# In[127]:


# consider box A with 250 elements in the ratio as per the question
A=[]
for i in range(0,250):
    if i<25:
        A.append(0)
    elif i>24 and i<150:
        A.append(1)
    elif i>=150:
        A.append(2)
random.shuffle(A)


# In[128]:


# consider box B with 250 elements in the ratio as per the question
B=[]
for i in range(0,250):
    if i<150:
        B.append(0)
    elif i>=150 and i<200:
        B.append(1)
    elif i>=200:
        B.append(2)
random.shuffle(B)


# In[129]:


# consider box C with 250 elements in the ratio as per the question
C=[]
for i in range(0,250):
    if i<200:
        C.append(0)
    elif i>=200 and i<225:
        C.append(1)
    elif i>=225:
        C.append(2)
random.shuffle(C)


# In[130]:


# consider box D with 250 elements in the ratio as per the question
D=[]
for i in range(0,250):
    if i<150:
        D.append(1)
    elif i>=150 and i<250:
        D.append(2)
random.shuffle(D)


# LET,
# P(A)=probA ,P(B)=probB
# ,P(C)=probC 
# and P(D)=probD
# 
# 

# P(X=0/A)=probR1,P(X=0/B)=probR2,P(X=0/C)=probR3 and P(X=0/D)=probR4

# In[131]:


probR1=A.count(0)/250
probR2=B.count(0)/250
probR3=C.count(0)/250
probR4=D.count(0)/250


# In[132]:


probA=.25
probB=.25
probC=.25
probD=.25


# P(x=0)=probR

# In[133]:


probR=(probA*probR1)+(probB*probR2)+(probC*probR3)+(probD*probR4)


# # PART1

# P(A/X=0)=probA1,
# P(B/X=0)=probA2 and
# P(C/X=0)=probA3

# In[134]:


probA1=(probR1*probA)/probR
print(f'probability that marble is drawn from box A given it is Red marble={probA1}')


# # PART 2

# In[135]:


probA2=(probR2*probB)/probR
print(f'probability that marble is drawn from box B given it is Red marble={probA2}')


# # PART 3

# In[136]:


probA3=(probR3*probC)/probR
print(f'probability that marble is drawn from box C given it is Red marble={probA3}')


# In[ ]:




