import string
import random
import sys

pass_len = int(input("Enter the length of the password: "))
if pass_len <= 0:
    print("Enter a valid password length!")
    sys.exit()

char_pool = string.ascii_letters

inc_num = input("Include numbers? (yes/no): ").lower()
if inc_num == "yes":
    char_pool += string.digits
elif inc_num != "no":
    print("Enter a valid answer (yes/no).")
    sys.exit()

inc_char = input("Include symbols? (yes/no): ").lower()
if inc_char == "yes":
    char_pool += string.punctuation
elif inc_char != "no":
    print("Enter a valid answer (yes/no).")
    sys.exit()

password = ""
for _ in range(pass_len):
    password += random.choice(char_pool)

print("Generated Password:", password)