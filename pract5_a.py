#5_a Develop the program for the mid-point circle drawing algorithm. 
import matplotlib.pyplot as plt

def midpoint_circle(radius):
    points = []
    
    x = 0
    y = radius
    
    d = 1.25 - radius
    points.append((x, y))
    points.append((y, x))
    points.append((x, -y))
    points.append((y, -x))
    points.append((-x, y))
    points.append((-y, x))
    points.append((-x, -y))
    points.append((-y, -x))
    
    while x < y:
        x += 1
        
        if d < 0:
            d += 2 * x + 1
        else:
            y -= 1
            d += 2 * x - 2 * y + 1
    
        points.append((x, y))
        points.append((y, x))
        points.append((x, -y))
        points.append((y, -x))
        points.append((-x, y))
        points.append((-y, x))
        points.append((-x, -y))
        points.append((-y, -x))
    
    return points

radius = 10
circle_points = midpoint_circle(radius)

fig, ax = plt.subplots()

for point in circle_points:
    ax.plot(point[0], point[1], 'bo')

ax.set_xlim(-radius - 1, radius + 1)
ax.set_ylim(-radius - 1, radius + 1)
ax.set_aspect('equal', 'box')
ax.set_title('Midpoint Circle Drawing Algorithm')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.grid(True)
plt.show()
