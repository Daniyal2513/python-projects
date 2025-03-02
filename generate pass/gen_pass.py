import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(characters, k=length))

num_pass = int(input("Enter numbers of password:"))
pass_len = int(input("Enter password length:"))

for i in range(num_pass):
    print(f"{i+1}: {generate_password(pass_len)}")