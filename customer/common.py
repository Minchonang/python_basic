import os
import pickle
def input_menu():
    return input('''
        다음 중에서 하실 작업의 메뉴를 입력하세요.
        I - 고객 정보 입력
        P - 이전 고객 정보 조회
        C - 현재 고객 정보 조회
        N - 다음 고객 정보 조회
        U - 현재 고객 정보 수정
        D - 현재 고객 정보 삭제
        Q - 프로그램 종료
    ''').upper()

def customer_read(customers, index):
    with open('../customer/customer_list.pickle', 'rb') as read_customer_list:
        if os.path.getsize('../customer/customer_list.pickle') > 0:
            customers = pickle.loads(read_customer_list)
            index += len(customers)
            print('저장된 고객 목록: ',customers)
        else:
            print('저장된 고객 정보가 없습니다.')
        return index


def chk_input_data(msg, func, upper=True):
    while True:
        x = input(msg)
        if upper:
            x = x.upper()
        if func(x):
            break
        else:
            print('잘못 입력하셨습니다. 다시 입력해 주세요.')
    return x

