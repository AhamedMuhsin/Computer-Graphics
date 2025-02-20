#4_a Develop the program for DDA Line drawing algorithm. 
import matplotlib.pyplot as plt

def dda_line(x1,y1,x2,y2):
    dx = x2-x1
    dy = y2-y1
    print(dx,dy)

    steps = max(abs(dx),abs(dy))
    x_inre = dx/steps
    y_inre = dy/steps
    x = x1
    y = y1
    x_points = []
    y_points = []
    for i in range(int(steps)+1):
        x_points.append(round(x))
        y_points.append(round(y))
        x = x + x_inre
        y = y + y_inre
    return(x_points,y_points)

def plot_line(x_points,y_points):
    plt.figure(figsize=(8,8))
    plt.plot(x_points,y_points,'ro-',label="line using DDA")
    plt.title("Line Drawing using DDA")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.legend()
    plt.show()

x1,y1 = 0,0
x2,y2 = 6,6
x_points,y_points = dda_line(x1,y1,x2,y2)
plot_line(x_points,y_points)
print(x_points,y_points)