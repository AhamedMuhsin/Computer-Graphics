#7_a Perform 2D Rotation on a given object. 
import numpy as np 
import matplotlib.pyplot as plt
def rotate_point(point, theta): 
    theta_rad = np.radians(theta) 
    rotation_matrix = np.array([[np.cos(theta_rad), -np.sin(theta_rad)], 
                                [np.sin(theta_rad), np.cos(theta_rad)]]) 
    rotated_point = np.dot(rotation_matrix, point) 
    return rotated_point
 
def rotate_shape(shape, angle):
    rotated_shape = [rotate_point(point, angle) for point in shape]
    return np.array(rotated_shape)

def plot_shape(shape, title):
    plt.figure(figsize=(6, 6))
    plt.plot(shape[:, 0], shape[:, 1], marker='o')
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.axhline(0, color='black', linewidth=0.5, ls='--')
    plt.axvline(0, color='black', linewidth=0.5, ls='--')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title(title)
    plt.grid()
    plt.show()

def main():
    shape = np.array([[0, 0], [2, 0], [1, 2]])
    plot_shape(shape, 'Original Shape')
    angle = 45
    rotated_shape = rotate_shape(shape, angle)
    plot_shape(rotated_shape, f'Rotated Shape by {angle} Degrees')
    print(rotate_shape)
if __name__ == "__main__":
    main()