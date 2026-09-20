import secrets
import string

password = ""

def generate_password():
    global password
    for i in range(how_many):
        password += secrets.choice(string.ascii_letters)

    print(password)

print("Welcome to the generate of passwords!")
print("How many letters you want to have your password? (1-100)")
how_many = int(input(""))

if how_many >= 0 and how_many <= 100:
    generate_password()

else:
    print("You typed incorrect amount of!")
