
import random
import math
import matplotlib.pyplot as plt
import numpy as np
c_list=[]
error_list=[]
from math import exp,pi,sin
def func(x):
    return exp(-x)*(sin(pi*x))**2
n=int(input('enter number:'))
for k in range (n):
    c=2**k
    x=np.zeros(c)
    c_list.append(math.log(c))
    for j in range(len(x)):
        x[j]=random.uniform(0,10)
    area=0
    for i in range(c):
        area+=func(x[i])
    value=10/float(c) * area

    error=0.4876477384840712-value
    error_list.append(math.log(abs(error)))
print('area:',value)
plt.scatter(c_list,error_list)
plt.show()