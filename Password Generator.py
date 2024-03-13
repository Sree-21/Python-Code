import string
import random
length = int(input("Enter password length: "))

characterList=string.ascii_letters+string.digits+string.punctuation

password = []

for i in range(length):
    randomchar = random.choice(characterList)
    password.append(randomchar)
print("The random password is " + "".join(password))