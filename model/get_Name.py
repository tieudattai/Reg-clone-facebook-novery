from random import choice

first_name = ['Nguyễn', 'Bùi', 'Lê', 'Phạm', 'Đỗ',
				'Trần', 'Đào', 'Vũ', 'Đinh', 'Ngô']

mid_name = ['Thị', 'Văn', 'Ngọc', 'Minh', 'Tú', 'Thị Minh']

last_name = ['Cường', 'Tài', 'Trung', 'Kiên', 'Hà', 'Ánh',
			'Minh', 'Anh', 'Chiến', 'Hoa', 'Hòa', 'An',
			'Bảo', 'Bình', 'Biên', 'Dung', 'Dương', 'Duy',
			'Dũng', 'Đạt', 'Dịu', 'Đức', 'Đô', 'Đại', 'Giang',
			'Quang', 'Quyên', 'Hải', 'Hưng', 'Huyền', 'Hương',
			'Hiền', 'Qúy', 'Thư', 'Thu']

def cre_name(mode=0):
	if mode == 1:
		return choice(first_name)
	elif mode == 2:
		return choice(mid_name) + ' ' + choice(last_name)
	else:
		return choice(first_name) + ' ' + choice(mid_name) + ' ' + choice(last_name)

# print(cre_name())