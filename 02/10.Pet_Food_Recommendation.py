# Problem: Recommend a type of pet food based on the pet's species and age. 
#          (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).

pet_species=input("Enter the species of pet :")
age=int(input("Enter the age of pet :"))

if pet_species=="Dog" and age <2 :
    food="Puppy food"
elif pet_species== "Cat" and age >5:
    food="Senior cat food"
else:
    print("Cannot recommend a type of pet food,better fed them warm water with lemon") 
    exit()

print(food)
           