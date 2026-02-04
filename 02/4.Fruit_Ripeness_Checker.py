# Problem: Determine if a fruit is ripe, overripe, or unripe based on its color. 
        #  (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)

fruit = input("Enter the fruit name:")
color = input("Enter the color of fruit:")

if fruit == "Banana":
    if color == "Green":
       print("Unripe")
    elif color == "Yellow":
       print("Ripe")
    elif color=="Brown":
       print("Overripe")       

else:
    print("We do not have information about this fruit.")        