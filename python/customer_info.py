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
	''')

	if menu.upper() == 'I':
		print('고객 정보 입력\n')

	elif menu.upper() == 'P':
		print('이전 고객 정보 조회\n')

	elif menu.upper() == 'C':
		print('현재 고객 정보 조회\n')

	elif menu.upper() == 'N':
		print('다음 고객 정보 조회\n')

	elif menu.upper() == 'U':
		print('현재 고객 정보 수정\n')

	elif menu.upper() == 'D':
		print('고객 정보 삭제\n')

	elif menu.upper() == 'Q':
		print('안녕하세요\n')
		break
	else:
		print('잘못 입력하셨습니다. 다시 입력해 주세요.\n')
