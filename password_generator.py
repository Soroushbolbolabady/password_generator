import string
import random

user_input = int(input("Enter your password lenght : "))

def password_generator(lenght):
	letters = string.ascii_letters
	digits = string.digits
	symbols = string.punctuation
	char_pool = list(letters + digits + symbols)
	password = ''
	
	for i in range(lenght):
		random_char = random.choice(char_pool)
		password += random_char
	
	print(password)

password_generator(user_input)
