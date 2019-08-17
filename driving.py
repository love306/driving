country = input('您的國家是? ')
age = input('您的年齡? ')
age = int(age)
if country == '台灣':
	if age >= 18:
		print('可以考駕照')
	else:
		print('不能考駕照')
elif country == '美國':
	if age >= 16:
		print('你可以考駕照')
	else:
		print('孩子早點睡')
else:
	print('只能輸入台灣/美國')
	