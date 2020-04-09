#!/usr/bin/env python
# coding: utf-8

# In[3]:


a=int(input("enter the elements for list 1:"))
list1=[]
print("enter the values")
for i in range(0,a):
    g=input()
    list1.append(g)
    
b=int(input("enter the elements for list 2:"))
list2=[]
for j in range(0,b):
    n=input()
    list2.append(n)
print("the lists are:")
print(list1)
print(list2)


# In[2]:


a=('python')
print(a)
print("enter the letter to be accessed:")
ch=int(input( ))
print(a[ch-1])


# In[4]:


a={'Hello':15,'Hi':10,'Hola':22,'Hey':9}
print(a)
result=a.pop('Hi')
print("deleted item is: ",result)
print("updated dictionary is : ",a)


# In[ ]:




