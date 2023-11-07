customerList = list()
index = -1

while True:
	menu = input('''
		메뉴를 입력하세요.
		i: 고객 정보 입력
		p: 이전 고객 정보 조회
		c: 현재 고객 정보 조회
		n: 다음 고객 정보 조회
		u: 현재 고객 정보 수정
		d: 현재 곡개 정보 삭제
		q: 프로그램 종료
	''').upper()

	if menu == 'I':
		print('고객 정보 입력')
		# customer = dict()
		customer = {
			'name': '',
			'gender': '',
			'email': '',
			'year': 0
		}
		customer['name'] = input('이름을 입력하세요\n')

		while True:
			customer['gender'] = input('성별 (M/F)를 입력하세요.\n').upper()
			if customer['gender'] in ('M', 'F'):
				break
			else:
				print('입력한 데이터가 잘못되었습니다. 다시 입력해 주세요.\n')

		while True:
			customer['email'] = input('이메일을 입력해 주세요.\n')
			at = '@' in customer['email']
			if at:
				break
			else:
				print('"@"를 포함해주세요.')
# 				이메일 중복 확인 기능 추가

		while True:
			customer['year'] = input('출생년도 4자리를 입력해 주세요.\n')
			check = len(customer['year']) == 4 and customer['year'].isdigit()
			if check:
				break
			else:
				print('다시 입력하세요.')

		customerList.append(customer)
		print('정상적으로 입력되었습니다.')
		print(customerList)
		# 새로 입력한 고객 정보의 위치 적용 여부 결정 필요.
		index += len(customerList) - 1

	elif menu == 'P':
		print('이전 고객 정보 조회')
		if index <= 0:
			print('첫번째 데이터입니다.')
		else:
			index -= 1
			print(f'{ index + 1 }번째 고객 정보입니다.')
			print(customerList[index])

	elif menu == 'C':
		print('현재 고객 정보 조회')
		if index >= 0:
			print(f'{index + 1}번째 고객 정보입니다.')
			print(customerList[index])
		else:
			print('입력된 정보가 없습니다. 정보 입력은 I를 입력하세요.')

	elif menu == 'N':
		print('다음 고객 정보 조회')
		if index >= len(customer) - 1:
			print('마지막 데이터입니다.')
			print(f'{index}번째 고객 정보입니다.')
		else:
			index += 1
			print(f'{index}번째 고객 정보입니다.')
			print(customerList[index])

	elif menu == 'U':
		print('현재 고객 정보 수정')
		print('고객 정보 입력')
		# customer = dict()
		customer = {
			'name': '',
			'gender': '',
			'email': '',
			'year': 0
		}
		# tnwjdg
		# 수정 내용이 없는 항목은 이전 값 유지하기.
		customer['name'] = input('이름을 입력하세요.\n')
		# customerList[index]['name'] = input('이름을 입력하세요\n')

		while True:
			customer['gender'] = input('성별 (M/F)를 입력하세요.\n').upper()
			if len(customer['gender']) == 0:
				customer['gender'] = customerList[index]['gender']
			if customer['gender'] in ('M', 'F'):
				break
			else:
				print('입력한 데이터가 잘못되었습니다. 다시 입력해 주세요.\n')

		while True:
			customer['email'] = input('이메일을 입력해 주세요.\n')
			at = '@' in customer['email']
			if at:
				break
			else:
				print('"@"를 포함해주세요.\n')
		# 				이메일 중복 확인 기능 추가

		while True:
			customer['year'] = input('출생년도 4자리를 입력해 주세요.\n')
			check = len(customer['year']) == 4 and customer['year'].isdigit()
			if check:
				break
			else:
				print('다시 입력하세요.\n')

		print('정상적으로 입력되었습니다.')
		print(customer)
		customerList[index] = customer

	elif menu == 'D':
		print(f'고객 정보({ customerList[index]["name"] }) 삭제')
		del customerList[index]

	elif menu == 'Q':
		print('See you again.')
		break
	else:
		print('잘못 입력하셨습니다. 다시 입력해 주세요.')
