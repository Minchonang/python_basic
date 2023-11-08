def input_c(customers, index):
    print('현재 고객 정보 조회')
    if index >= 0:
        print(f'{index + 1}번째 고객 정보 입니다.')
        print(customers[index])
    else:
        print('입력된 정보가 없습니다. 정보 입력은 I를 선택하세요.')
