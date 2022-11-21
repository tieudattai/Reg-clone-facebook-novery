import random

firstphone = ['03', '09']
numbers = '0123456789'

def cre_phone():
	return random.choice(firstphone) + ''.join((random.choice(numbers) for i in range(8)))