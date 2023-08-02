#!/usr/bin/env python
# coding: utf-8

# In[1]:


m=[]
str = input(" eny\ter the string")
x= int(input("enter the number"))
i= 0
val =str
while i<len(str):
    j= i+x-1
    while j<len(str):
        if str[i]==str[j]:
            value = str[i:j+1]
            m.append(value)
        j= j+1
    i=i+1  
shortest = len(min(m,key=len))
for i in m :
    if len(i)==shortest:
        print(i)


# In[ ]:




