# Problem: Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of espresso.

order_size=input("Enter the size of your coffee(small/medium/large): ")
extra_shot=False

if extra_shot:
    coffee = order_size + " coffee with extra shot of espresso"
else:
    coffee = order_size + " coffee"

print(coffee)        
