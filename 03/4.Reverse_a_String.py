# Problem: Reverse a string using a loop.

input_string=input("Enter the string :")
reverse_string=""
for char in input_string:
    reverse_string = char + reverse_string
print(reverse_string)