#1_b Draw a co-ordinate axis at the center of the screen. 
import numpy as np
import matplotlib.pyplot as plt 
x1=-10 #——Δx=150
x2=90
y1=90 #—-Δy=100
y2=-10
plt.axis([x1,x2,y1,y2])

plt.axis('on')
plt.grid(True)
plt.title('Coordinate Axis on the center of Screen')

dx=5
dy=-5
for x in np.arange(x1,x2,dx):
    for y in np.arange(y1,y2,dy):
        plt.scatter(x,y,s=1,color='lightgray')
plt.arrow(30,30,20,0,head_length=4,head_width=3,color='k')
plt.arrow(30,30,0,20,head_length=4,head_width=3,color='k')
plt.show()