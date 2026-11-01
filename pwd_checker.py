
import re

def check_password(password):
    score = 0
    if len(password) >= 12:
        score += 1

    if re.search("[a-z]", password):
        score += 1

    if re.search("[A-Z]", password):
        score += 1

    if re.search("\d", password):
        score += 1

    if re.search("[^\w\s]", password):
        score += 1

    return ['very weak', 'weak', 'fair', 'good', 'strong', 'very strong'][score]

pwd = input("enter a password to check: ")
print("strength:", check_password(pwd))
