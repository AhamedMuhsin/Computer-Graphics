#6_a Write a program to implement 2D scaling. 
#6_b Write a program to perform 2D translation.
import matplotlib.pyplot as plt 
def scale_and_translate_2d(point, scaling_factors, translation_factors): 
    x, y = point 
    Sx, Sy = scaling_factors 
    Tx, Ty = translation_factors 
 
    x_scaled = x * Sx 
    y_scaled = y * Sy 
    x_new = x_scaled + Tx 
    y_new = y_scaled + Ty 
    return x_new, y_new 

x, y = map(float, input("Enter the coordinates of the point (x, y): ").split())
Sx, Sy = map(float, input("Enter the scaling factors (Sx, Sy): ").split()) 
Tx, Ty = map(float, input("Enter the translation factors (Tx, Ty): ").split()) 

result = scale_and_translate_2d((x, y), (Sx, Sy), (Tx, Ty)) 
#Display the result 
print(f"\nOriginal Point: ({x}, {y})") 
print (f"Scaling Factors: (Sx {Sx}, Sy {Sy})") 
print(f"Translation Factors: (Tx {Tx}, Ty {Ty})") 
print(f"New Point after Scaling and Translation: {result}") #Plot the original point 
plt.scatter(x, y, color='blue', label="Original Point") 
plt.text(x, y, f" ({x}, {y})", color="blue") 

plt.scatter(Sx, Sy, color='orange', label=" Scaled Point") 
plt.text(Sx, Sy, f"({Sx:.2f}, {Sy:.2f})", color="orange")

plt.scatter (Tx, Ty, color="green", label="Translated Point") 
plt.text(Tx, Ty, f"({Tx:.2f}, {Ty:.2f})", color="green") 
#Draw lines to connect the transformations 
plt.plot([x, Sx], [y, Sy], linestyle='--', color="gray", label="Scaling Transformation") 
plt.plot([Sx, Tx], [Sy, Ty], linestyle='--', color="gray", label ="Translation Transformation") 
plt.axhline(0, color="black", linewidth=0.5) 
plt.axvline(0, color="black", linewidth=0.5)
plt.grid(color='lightgray', linestyle='--', linewidth=0.5) 
plt.title("20 Scaling and Translation Visualization") 
plt.legend() 
plt.xlabel("X-axis") 
plt.ylabel("Y-axis") 
# plt.plot([x, Sx], [y, Sy], linestyle='--', color='gray', label="Scaling Transformation") 
# plt.plot([Sx, Tx], [Sy, Ty], linestyle='--', color='gray', label="Translation Transformation") 
# plt.axhline(0, color='black', linewidth=0.5) 
# plt.axvline(0, color='black', linewidth=0.5) 
# plt.grid(color='lightgray', linestyle='--', linewidth=8.5) 
# plt.title("20 Scaling and Translation Visualization") 
# plt.legend() 
# plt.xlabel("x-axis") 
# plt.ylabel("Y-axis") 
plt.axis('equal') 
plt.show() 