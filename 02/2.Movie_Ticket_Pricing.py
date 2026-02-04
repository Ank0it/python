# Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children.
#          Everyone gets a $2 discount on Wednesday.

age = int(input("Enter your age: "))
day = input("Enter today day: ")

# 1st way
if age >= 18 :
    if day == "Wednesday":
        print("Movie tickets price : $10")
    else:
        print("Movie tickets price : $12")       
else:
    if day == "Wednesday":
        print("Movie tickets price : $6")
    else:
        print("Movie tickets price : $8")
    
# 2nd way 

price=12 if age >= 18 else 8
   
if day == "Wednesday" :
    price -=2

print("Tickets price for U is $",price)    


    
