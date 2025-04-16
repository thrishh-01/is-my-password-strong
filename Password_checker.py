import re  
def check_password_strength(password):
    if len(password) >= 8 and re.search("[a-z]", password) and re.search("[A-Z]", password) and re.search("[0-9]", password) and re.search("[@#$%^&+=]", password):
        return "Very Strong"
    elif len(password) >= 8 and re.search("[a-z]", password) and re.search("[A-Z]", password) and re.search("[0-9]", password):
        return "Strong"
    elif len(password) >= 6:
        return "Medium"
    else:
        return "Weak"
password = input("Enter your password: ")
def check_strength(password):
    if len(password) < 6:
        return "MAKE THE PASSWORD BIGGER!!!😠"
    else:
        return "THE PASSWORD IS BIG ENOUGH!😁"
result = check_strength(password)
print(result)  
strength = check_password_strength(password)
print(f"Password strength: {strength}")
