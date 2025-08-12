import random
import string

def generate_password(length):

    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    
    password += random.choices(characters, k=length - 4)
  
    random.shuffle(password)
    return ''.join(password)
length = int(input("Enter password length: "))
if length < 4:
    print("Password length should be at least 4 characters.")
else:
    print("Generated Password:", generate_password(length))
