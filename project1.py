#!/usr/bin/env python
# coding: utf-8

# Double-click to insert team members' names here:

# In[ ]:


from sympy import *
from sympy.plotting import (plot, plot_parametric)


# #1a Evaluate expression

# In[ ]:

x = 6.5
y = 3.2
z = (x**2 + y**2)**(1/2) + (x*y)/(y-x)
print(f"The answer to 1a is {z}")

# #1b Evaluate expression

# In[ ]:





# #1c Equality and implications

# In[ ]:





# #2 Comparing interest compounding

# In[ ]:
P = 80000
r = 0.03
m = 1
t = 1

A = P * (1 + (r / m))**(m * t)
print(f"The balance after 1 year while compounded annually is {A}")

m = 365
A = P * (1 + (r / m))**(m * t)
print(f"The balance after 1 year while compounded daily is {A}")

# #3a Trig value at pi/6

# In[ ]:





# #3b Trig value at 1.25

# In[ ]:





# #4a length of triangle sides

# In[ ]:





# #4b angle BAC

# In[ ]:





# #4c angle BAC using dot product

# In[ ]:




