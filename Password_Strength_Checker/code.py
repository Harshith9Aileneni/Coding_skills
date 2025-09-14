# Requirements:
# 1. Function that takes a password as input
# 2. Checks: length (8+ chars), has numbers, has uppercase, has lowercase
# 3. Returns strength score 1-4 and feedback
# 4. Use f-strings for all output
# 5. Test with 3 different passwords

print("Password should have length (8+ chars), have numbers, have uppercase, have lowercase")
password = input("Enter your password")


def check_password(password):
    length_test = len(password) >= 8
    uppercase = any(char.isupper() for char in password)
    lowercase = any(char.islower() for char in password)
    numb = any(char.isdigit() for char in password)

    if length_test and uppercase and lowercase and numb:
        print("your password has met the requirements")
    else:
        print(f"your {password} has not met the Requirement")

check_password(password)

