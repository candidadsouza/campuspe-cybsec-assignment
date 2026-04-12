# take password input
password = input("Enter password: ")

score = 0

# check length
if len(password) >= 8:
    score += 1
else:
    print("Password should be at least 8 characters")

# check uppercase
if any(c.isupper() for c in password):
    score += 1
else:
    print("Add uppercase letter")

# check lowercase
if any(c.islower() for c in password):
    score += 1
else:
    print("Add lowercase letter")

# check number
if any(c.isdigit() for c in password):
    score += 1
else:
    print("Add a number")

# check special character
if any(not c.isalnum() for c in password):
    score += 1
else:
    print("Add special character")

# final result
print("\nScore:", score)

if score <= 2:
    print("Strength: Weak")
elif score <= 4:
    print("Strength: Medium")
else:
    print("Strength: Strong")
