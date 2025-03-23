#Program to create a house like figure and perform the following operations. 
#i. Scaling about the origin followed by translation. 
#ii. Scaling with reference to an arbitrary point. 

import matplotlib.pyplot as plt
import numpy as np

house_coords = np.array([[0, 0], [4, 0], [2, 3], [0, 0],[0,-4],[4,-4],[4,0]])

def plot_house(coords, title):
    plt.figure(figsize=(6, 6))
    plt.plot(coords[:, 0], coords[:, 1], 'b-')
    plt.fill(coords[:, 0], coords[:, 1], 'b', alpha=0.3)
    plt.title(title)
    plt.grid(True)
    plt.xlim(-5, 10)
    plt.ylim(-5, 10)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

def scale_translate(coords, scale_factor, translate_vector):
    scaled_coords = coords * scale_factor
    translated_coords = scaled_coords + translate_vector
    return translated_coords

def scale_arbitrary(coords, scale_factor, arbitrary_point):
    translated_coords = coords - arbitrary_point
    scaled_coords = translated_coords * scale_factor
    final_coords = scaled_coords + arbitrary_point
    return final_coords

plot_house(house_coords, "Original House")

scaled_translated_coords = scale_translate(house_coords, 2, np.array([3, 3]))
plot_house(scaled_translated_coords, "Scaled and Translated House")

arbitrary_point = np.array([2, 2])
scaled_arbitrary_coords = scale_arbitrary(house_coords, 1.5, arbitrary_point)
plot_house(scaled_arbitrary_coords, "Scaled About Arbitrary Point")

