def input_d(customers, index):
    print(f'현재 고객 정보{ customers[index]["name"] } 삭제')
    del customers[index]
