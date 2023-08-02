#!/usr/bin/env python
# coding: utf-8

# In[1]:


def findasci(c):
    return ord(c)
def findstring(c):
    return chr(c)


# In[2]:


str =  input("enter the string")


# In[28]:


l=[]
for i in range(0,len(str)):
    asc = findasci(str[i])
    l.append(asc)
print(l)
ind1 = 0
ind2 = 0
for i in range(0,len(l)):
    if l[i]%2==0 and (i+1)!=ind1 and (i+1)!=ind2 and i<len(l)-1:
        l[i+1]= l[i+1]+( l[i]%7)
        if  l[i+1]>127:
            l[i+1]=83
        ind1=i+1
    elif l[i]%2!=0 and (i-1)!=ind2 and (i-1)!=ind1:
        l[i-1]= l[i-1]-( l[i]%5)
        if  l[i-1]<0:
            l[i-1]=83
        ind2=i-1
s=[]
for i in l:
    s.append(findstring(i))
print("".join(s))
                                
                                
    
    


# In[ ]:





# In[ ]:




