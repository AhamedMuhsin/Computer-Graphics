#4_b Develop the program for Bresenham’s Line drawing algorithm
import matplotlib.pyplot as plt
def bresenham(x1,y1,x2,y2): 
    points = [] 
    dx=x2-x1
    dy=y2-y1
    e=2*dy-dx
    y=y1
    for x in range(x1, x2+1): 
        points.append((x,y)) 
        if (e>=0): 
            y=y+1
            e=e+2* (dy-dx) 
        else: 
            e=e+2*dy 
    return points 

def plot_line(points):
    plt.figure(figsize=(8,8))
    plt.plot(points,'ro-',label="line using Bresenhams")
    plt.title("Line Drawing using Bresenhams")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.legend()
    plt.show()

x1,y1 = 5,5
x2,y2 = 13,9
points = bresenham(x1,y1,x2,y2)
plot_line(points)
print(points)