#Draw the following basic shapes in the center of the screen : 
# i. Circle ii. Rectangle iii. Square iv. Concentric Circles v. Ellipse vi. Line 
import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots(figsize=(8, 8))

ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_aspect('equal', 'box')

circle = patches.Circle((0, 0), 1, fill=False, edgecolor='blue', linewidth=2, label='Circle')
ax.add_patch(circle)

rectangle = patches.Rectangle((-1.5, -0.5), 3, 1, fill=False, edgecolor='green', linewidth=2, label='Rectangle')
ax.add_patch(rectangle)

square = patches.Rectangle((-1, -1), 2, 2, fill=False, edgecolor='red', linewidth=2, label='Square')
ax.add_patch(square)
num_circles = 5
for i in range(1, num_circles + 1):
    concentric_circle = patches.Circle((0, 0), i * 0.5, fill=False, edgecolor='purple', linewidth=1)
    ax.add_patch(concentric_circle)

ellipse = patches.Ellipse((0, 0), 2, 1, fill=False, edgecolor='orange', linewidth=2, label='Ellipse')
ax.add_patch(ellipse)

ax.plot([-2, 2], [0, 0], color='black', linewidth=2, label='Line')
ax.set_title('Basic Shapes in the Center of the Screen')
ax.legend()
ax.grid(True)
plt.show()