def input_n(customers, index):
    print('다음 고객 정보 조회')
    if index >= (len(customers) - 1):
        print('이후 데이터 이동 불가')
        print(index)
    else:
        index += 1
        print(f'{index + 1}번째 고객 정보 입니다.')
        print(customers[ index ])
    return index
