def input_p(customers, index):
    print('이전 고객 정보 조회')
    if index < 0:
        print('이전 데이터로 이동 불가.')

    else:
        index -= 1
        print(f'{index + 1}번째 고객 정보 입니다.')
        print(customers[ index ])
    return index