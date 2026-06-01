print("-------Password Strength Checker-------\n")
password = input("Enter your password: ")

score = 0

if len(password) >= 8:
    score += 1
else:
    print("Password should contain at least 8 characters.")

upper = False
for char in password:
    if char.isupper():
        upper = True
        score += 1
        break

if not upper:
    print("Password should contain at least one uppercase letter.")

lower = False
for char in password:
    if char.islower():
        lower = True
        score += 1
        break

if not lower:
    print("Password should contain at least one lowercase letter.")

number = False
for char in password:
    if char.isdigit():
        number = True
        score += 1
        break

if not number:
    print("Password should contain at least one number.")

special = False
for char in password:
    if not char.isalnum():
        special = True
        score += 1
        break

if not special:
    print("Password should contain at least one special character.")

print("\nPassword Strength:")

if score <= 2:
    print("Weak")
elif score <= 4:
    print("Medium")
else:
    print("Strong")