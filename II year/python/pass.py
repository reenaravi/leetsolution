def verify_password(password):
    if len(password) < 8:
        return "Password must be at least 8 characters long"

    has_letter = False
    has_digit = False
    has_special = False

    for ch in password:
        if ch.isalpha():
            has_letter = True
        elif ch.isdigit():
            has_digit = True
        else:
            has_special = True

    if has_letter and has_digit and has_special:
        return "Password is valid"
    else:
        return "Password must contain letters, numbers, and special characters"
pwd = input("Enter password: ")
print(verify_password(pwd))
