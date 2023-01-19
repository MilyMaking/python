import matplotlib
import matplotlib.pyplot as plt
import math

global x 
global y 
xa = []
ya = []

for i in range(1,721):
    x = i
    y = x/180*math.pi
    y = math.sin(y)
    xa.append(x)
    ya.append(y)
   
plt.plot(xa,ya)
plt.title('Sin Wave')
plt.ylabel('Y-axis')
plt.xlabel('X-axis')
plt.show()
    



    