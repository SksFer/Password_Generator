import string
import random

def random_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""

    for i in range (length):
        password += random.choice(characters)
    return password

length = int(input("How long will your password be?"))

new_password = random_password(length)
print("the new password is:", new_password)