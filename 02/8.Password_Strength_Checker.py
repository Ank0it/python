# Problem: Check if a password is "Weak", "Medium", or "Strong". 
#          Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong)

password=input("Enter your password :")
count_chars=len(password)

if count_chars < 6:
    strength="Weak"
elif count_chars >=6 and count_chars <10:
    strength="Medium"
else:
    strength="Strong"

print(strength)            
