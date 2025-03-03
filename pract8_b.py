#8_b Write a program to implement Liang - Barsky Line Clipping Algorithm 
def liang_barsky(xmin, xmax, ymin, ymax, x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    p = [-dx, dx, -dy, dy]
    q = [x1 - xmin, xmax - x1, y1 - ymin, ymax - y1]

    t0, t1 = 0.0, 1.0  

    for i in range(4):
        if p[i] == 0:
            if q[i] < 0:
                return None  
        else:
            t = q[i] / p[i]
            if p[i] < 0:
                t0 = max(t0, t)
            else:
                t1 = min(t1, t)

        if t0 > t1:
            return None  

    clipped_x1 = x1 + t0 * dx
    clipped_y1 = y1 + t0 * dy
    clipped_x2 = x1 + t1 * dx
    clipped_y2 = y1 + t1 * dy

    return (clipped_x1, clipped_y1, clipped_x2, clipped_y2)

xmin, xmax, ymin, ymax = 15, 25, 15, 25 
x1, y1, x2, y2 = 10, 10, 60, 30  

clipped_line = liang_barsky(xmin, xmax, ymin, ymax, x1, y1, x2, y2)

if clipped_line:
    print(f"Clipped Line: {clipped_line}")
else:
    print("Line is completely outside the clipping window.")
