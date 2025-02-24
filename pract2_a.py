#2_a Divide your screen into four region, draw circle, rectangle, ellipse and half ellipse in each region with appropriate message.
import matplotlib.pyplot as plt 
import matplotlib.patches as patches 
def draw_shape (ax, shape, message):
    if shape=="circle": 
        circle = patches.Circle((0.5,0.5),0.4,color="blue", fill=False) 
        ax.add_patch (circle) 
    elif shape=="rectangle": 
        rect=patches.Rectangle ((0.25,0.25),0.5,0.5,color="green", fill=False) 
        ax.add_patch(rect) 
    elif shape=="ellipse": 
        ellipse=patches.Ellipse((0.5,0.5),0.7,0.4,color="red", fill=False)
        ax.add_patch (ellipse) 
    elif shape=="half-ellipse": 
        h_ellipse=patches.Ellipse ((0.5,0.5), 0.7,0.3,color="purple", fill=False) 
        ax.add_patch(h_ellipse) 
        ax.set_clip_path (patches.Polygon ([[0,0],[0.5,1],[1,0]])) 
    ax.set_xlim (0,1) 
    ax.set_ylim (0,1) 
    ax.text (0.5,-0.1, message,ha="center", va="center", fontsize=10, transform=ax.transAxes) 
    ax.axis("off") 

fig, axs = plt.subplots(2,2,figsize=(10,8))
shapes_and_messages=[ 
    ("circle", "this is a circle"), 
    ("rectangle", "this is a reactangle"),
    ("ellipse", "this is a ellipse"), 
    ("half-ellipse", "this is a half-ellipse") ]
for ax, (shape, message) in zip(axs.flat, shapes_and_messages): 
    draw_shape (ax, shape, message) 
plt.tight_layout() 
plt.show() 