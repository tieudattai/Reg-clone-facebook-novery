from random import randint, choice
import unidecode

domains = ['gmail.com', 'yahoo.com', 'hotmail.com',
			'outlook.com', 'reddit.com']

def convert_name(name):
	lower = name.lower()
	name = lower.strip().split(' ')
	name = ''.join(name)
	return unidecode.unidecode(name)

def cre_email(name='', custom=-1):
	"""
		- kiểm tra chuyển đổi tên email nếu có
		- không có tên tiến hành random ký tự
	"""
	if name == '':
		characters = '1234567890qwertyuiopasdfghjklzxcvbnm'
		name_email = ''.join((choice(characters) \
			for i in range(randint(8,12))))
	else:
		name_email = convert_name(name)
	"""
		- kiểm tra tên miền nếu có
		- không có thì random tên miền
		- lỗi trả về miền cuối cùng
	"""
	if custom == -1:
		domain = choice(domains)
	else:
		try:
			domain = domains[custom]
		except:
			domain = domains[-1]
	"""
		- tạo phần nối giữ tên email và tên miền
	"""
	mid = choice(['', '_', '.']) + str(randint(1,1000)) + '@'
	return name_email + mid + domain

# print(cre_email("Ngô Thế Tài"))