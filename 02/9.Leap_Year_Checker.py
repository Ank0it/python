# Problem: Determine if a year is a leap year. (Leap years are divisible by 4, but not by 100 unless also divisible by 400).

year=int(input("Enter the year :"))

if year%4==0:
    print("You entered a leaf year")
else:
    print("You enetered a non leaf year")    