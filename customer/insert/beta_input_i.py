def input_i(customers, index):
    print('고객정보 입력')
    customer = { 'name': '', 'gender': '', 'email': '', 'year': 0 }
    customer['name'] = input('이름을 입력하세요 : ')
    while True:
        customer['gender'] = input('성별 (M/F)를 입력하세요 : ').upper()
        if customer['gender'] in ('M', 'F'):
            break
        else:
            print('잘못 입력하셨습니다. 다시 입력 해 주세요.')
    while True:
        customer['email'] = input('이메일 주소를 입력하세요 : ')
        golbang = '@' in customer['email']
        if golbang:
            break
        else:
            print('"@"를 포함한 이메일 주소를 입력하세요.')
    # 이메일 중복 로직 추가~~~~

    while True:
        customer['year'] = input('출생년도 4자리 입력하세요 : ')
        check = len(customer['year']) == 4 and customer['year'].isdigit()
        if check:
            break
        else:
            print('잘 입력 해라....')
    print(customer)
    customers.append(customer)
    print(customers)
    # 새로 입력한 고객 정보의 위치 적용 여부 고민
    index = len(customers) - 1
    return index
