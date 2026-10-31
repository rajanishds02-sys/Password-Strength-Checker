import string

def check_password(password):

    score = 0
    feedback = []

    # Check password length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters")

    # Check uppercase letters
    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("Add uppercase letters")

    # Check lowercase letters
    if any(c.islower() for c in password):
        score += 1
    else:
        feedback.append("Add lowercase letters")

    # Check numbers
    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("Add numbers")

    # Check special characters
    if any(c in string.punctuation for c in password):
        score += 1
    else:
        feedback.append("Add special characters")

    # Display password strength
    if score <= 2:
        strength = "WEAK"
    elif score <= 4:
        strength = "MEDIUM"
    else:
        strength = "STRONG"

    return strength, feedback


print("================================")
print("    PASSWORD STRENGTH CHECKER")
print("================================")

password = input("Enter a test password: ")

strength, feedback = check_password(password)

print("\nPassword Strength:", strength)

if feedback:
    print("\nSuggestions to improve:")
    for item in feedback:
        print("-", item)
else:
    print("\nGood! All basic checks passed.")

print("================================")