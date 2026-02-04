# Problem: Suggest an activity based on the weather 
#          (e.g., Sunny - Go for a walk, Rainy - Read a book, Snowy - Build a snowman).

weather = input("Enter the current weather:")

if weather=="Sunny":
    activity="Go for a walk"
elif weather=="Rainy":
    activity="Read a book"
elif weather=="Snowy":
    activity="Build a snowman"
else:
    print("Cannot suggest an activity based on this weather")
    exit()
    
print(activity) 

     