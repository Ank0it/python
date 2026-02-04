# Problem: Calculate the sum of even numbers up to a given number n.

n=int(input("Enter the number : "))

even_sum=0
for i in range(1,n+1):
    if i%2==0:
        even_sum +=1
print("Total number of even numbers up to n is : ", even_sum)