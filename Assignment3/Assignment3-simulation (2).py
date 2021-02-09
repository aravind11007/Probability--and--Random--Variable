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


# consider box A with 250 elements in the ratio as per the question.In boxA i will be considering 250 balls consisting 
#of red ,white,black ball in the ratio 1:6:3 ie if we have 250 balls 25 will be red,150 will be white and 75 will be black
A=[]
for i in range(0,250):
    if i<25:
        A.append(0)
    elif i>24 and i<150:
        A.append(1)
    elif i>=150:
        A.append(2)
random.shuffle(A)
# now i have box A with 250 elements in the ratio 1:6:3


# In[128]:


# consider box B with 250 elements in the ratio as per the question.In boxB i will be considering 250 balls consisting 
#of red ,white,black ball in the ratio 6:2:2
B=[]
for i in range(0,250):
    if i<150:
        B.append(0)
    elif i>=150 and i<200:
        B.append(1)
    elif i>=200:
        B.append(2)
random.shuffle(B)
# now i have box B with 250 elements in the ratio 6:2:2


# In[129]:


# consider box C with 250 elements in the ratio as per the question.In boxC i will be considering 250 balls consisting 
#of red ,white,black ball in the ratio 8:1:1
C=[]
for i in range(0,250):
    if i<200:
        C.append(0)
    elif i>=200 and i<225:
        C.append(1)
    elif i>=225:
        C.append(2)
random.shuffle(C)
# now i have box C with 250 elements in the ratio 8:1:1


# In[130]:


# consider box D with 250 elements in the ratio as per the question.In boxD i will be considering 250 balls consisting 
#of red ,white,black ball in the ratio 0:6:4
D=[]
for i in range(0,250):
    if i<150:
        D.append(1)
    elif i>=150 and i<250:
        D.append(2)
random.shuffle(D)
# now i have box D with 250 elements in the ratio 0:6:4


# LET,
# P(A)=probA ,P(B)=probB
# ,P(C)=probC 
# and P(D)=probD
# 
# 

# P(X=0/A)=probR1,P(X=0/B)=probR2,P(X=0/C)=probR3 and P(X=0/D)=probR4

# In[131]:


# Next i will be calculating the number of zeros(redballs) in BoxA,BoxB,BoxC,BoxD respectively and divide it by 250 so that,
# i will be getting the probability of red ball given it is from boxA,boxB etc
probR1=A.count(0)/250
probR2=B.count(0)/250
probR3=C.count(0)/250
probR4=D.count(0)/250


# In[132]:


#Probability that box A,box B,box c ,box D will be selected
probA=.25
probB=.25
probC=.25
probD=.25


# P(x=0)=probR

# In[133]:


# probability of getting a red ball
probR=(probA*probR1)+(probB*probR2)+(probC*probR3)+(probD*probR4)


# # PART1

# P(A/X=0)=probA1,
# P(B/X=0)=probA2 and
# P(C/X=0)=probA3

# In[134]:


#probability that marble is drawn from box A given it is Red marble
probA1=(probR1*probA)/probR
print(f'probability that marble is drawn from box A given it is Red marble={probA1}')


# # PART 2

# In[135]:


#probability that marble is drawn from box B given it is Red marble
probA2=(probR2*probB)/probR
print(f'probability that marble is drawn from box B given it is Red marble={probA2}')


# # PART 3

# In[136]:


#probability that marble is drawn from box C given it is Red marble
probA3=(probR3*probC)/probR
print(f'probability that marble is drawn from box C given it is Red marble={probA3}')


# In[ ]:




