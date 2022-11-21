import random

characters = '1234567890@qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'

def cre_password():
	return ''.join((random.choice(characters) for i in range(random.randint(8,12))))

# print(cre_password())