#!/usr/bin/env python
# coding: utf-8

# In[35]:


from random import randint
import matplotlib.pyplot as plt


# In[36]:


z=0
list1=[]
while z<100000:
    Z=randint(0,1)
    if Z==0:
        X0=-1.5
    elif Z==1:
        X0=2
    Z=randint(0,1)
    if Z==0:
        X1=X0+-1.5
    elif Z==1:
        X1=X0+2
    Z=randint(0,1)
    if Z==0:
        list1.append(X1+X0-1.5)
    elif Z==1:
        list1.append(X1+X0+2)
    z+=1
X2=list(set(list1))
X2.sort()
    


# In[37]:


print(f"Random values of X2 are,{X2}")


# In[38]:


#Pr(-6)=A,Pr(-2.5)=B,Pr(1)=C,Pr(4.5)=D,Pr(8)=E


# In[39]:


A=list1.count(-6)
B=list1.count(-2.5)
C=list1.count(1)
D=list1.count(4.5)
E=list1.count(8)


# In[40]:


print(f"Pr(X2=-6)={A/z}")
print(f"Pr(X2=-2.5)={B/z}")
print(f"Pr(X2=1)={C/z}")
print(f"Pr(X2=4.5)={D/z}")
print(f"Pr(X2=8)={E/z}")


# In[47]:


x=[-6,-2.5,1,4.5,8]
y1=[A/z,B/z,C/z,D/z,E/z]
y2=[1/8,2/8,2/8,2/8,1/8]
plt.bar(x,y1,color='green')
plt.plot(x,y2,marker="*",color='red')
plt.legend(['theoretical PMF','simulated PMF'])
plt.title('theoretical PMF vs simulated PMF')
plt.xlabel('outcome')
plt.ylabel('probability')
plt.savefig('pdfnew.png')


# In[48]:


x=[-6,-2.5,1,4.5,8]
y1=[A/z,A/z+B/z,A/z+B/z+C/z,A/z+B/z+C/z+D/z,A/z+B/z+C/z+D/z+E/z]
y2=[1/8,2/8+1/8,2/8+2/8+1/8,2/8+2/8+2/8+1/8,1/8+2/8+2/8+2/8+1/8]
plt.bar(x,y1,color='green')
plt.plot(x,y2,marker="*",color='red')
plt.legend(['theoretical PMF','simulated PMF'])
plt.title('theoretical PMF vs simulated PMF')
plt.xlabel('outcome')
plt.ylabel('probability')
plt.savefig('cdfnew.png')


# In[ ]:




