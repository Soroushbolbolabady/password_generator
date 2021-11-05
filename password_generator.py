import string
import random




user_input = int(input("Enter your password lenght : "))

def password_generator(lenght):

	letter = string.ascii_letters
	digit = string.digits
	symbol = string.punctuation
	array = list(letter + digit + symbol)
	password = []
	
	for i in range(lenght):
		random_char = random.choice(array)
		password.append(random_char)
	
	new_password = "".join(password)
	print(new_password)


password_generator(user_input)