#5_b Develop the program for the mid-point ellipse drawing algorithm. 
import matplotlib.pyplot as plt

def plot_point(x, y, h, k, points):
    points.append((h + x, k + y))
    points.append((h - x, k + y))
    points.append((h + x, k - y))
    points.append((h - x, k - y))

def draw_ellipse(h, k, a, b):
    points = []
    x = 0
    y = b
    a2 = a * a
    b2 = b * b
    fa2 = 4 * a2
    fb2 = 4 * b2
    p = round(b2 - (a2 * b) + (0.25 * a2))
    while (fa2 * y > fb2 * x):
        plot_point(x, y, h, k, points)
        if (p < 0):
            p = p + fb2 * x + b2
        else:
            y = y - 1
            p = p + fb2 * x - fa2 * y + b2
        x = x + 1
    p = round(b2 * (x + 0.5) * (x + 0.5) + a2 * (y - 1) * (y - 1) - a2 * b2)

    # Region 2
    while (y >= 0):
        plot_point(x, y, h, k, points)
        if (p > 0):
            p = p - fa2 * y + a2
        else:
            x = x + 1
            p = p + fb2 * x - fa2 * y + a2
        y = y - 1

    return points

def main():
    h = 0
    k = 0
    a = 5
    b = 3

    points = draw_ellipse(h, k, a, b)
    x_coords, y_coords = zip(*points)
    plt.figure(figsize=(6, 6))
    plt.scatter(x_coords, y_coords, color='blue')  
    plt.xlim(-a - 1, a + 1)
    plt.ylim(-b - 1, b + 1)
    plt.axhline(0, color='black',linewidth=0.5, ls='--')
    plt.axvline(0, color='black',linewidth=0.5, ls='--')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title('Midpoint Ellipse Drawing Algorithm')
    plt.grid()
    plt.show()

if __name__ == "__main__":
    main()