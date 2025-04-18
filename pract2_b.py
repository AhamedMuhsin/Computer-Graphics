#2_b Draw a simple hut on the screen
import matplotlib.patches as patches 
import matplotlib.pyplot as plt 
def draw_hut(ax, message): 
    base = patches.Rectangle((0.3, 0.2), 0.4, 0.4, color="yellow", fill=True) 
    ax.add_patch(base) 
    roof =  patches.Polygon([[0.25, 0.6], [0.5, 0.9], [0.75, 0.6]],color="brown", fill=True) 
    ax.add_patch(roof) 
    door = patches.Rectangle((0.45, 0.2), 0.1, 0.2, color="red", fill = True) 
    ax.add_patch(door) 
    ax.set_xlim(0, 1) 
    ax.text (0.5, -0.1, message, ha="center", va="center", fontsize=10, transform=ax.transAxes) 
    ax.set_ylim(0, 1) 
    ax.axis("off") 
fig, axs = plt.subplots (1, 1, figsize=(6,6)) 
draw_hut(axs, "This is a simple hut") 
plt.tight_layout () 
plt.show()