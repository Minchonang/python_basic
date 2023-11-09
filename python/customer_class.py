# 메인 로직을 최대한 짧게 정리 => 함수 이용
# import customer as cust
# import cust.customer_func as ff
# from cust.ver1 import  customer_func as ff
# from cust.ver1.customer_func import do_I as I

import pickle
import os

def print_menu():
    return input('''
        다음 중에서 하실 작업의 메뉴를 입력하세요.
        I - 고객 정보 입력
        P - 이전 고객 정보 조회
        C - 현재 고객 정보 조회
        N - 다음 고객 정보 조회
        U - 현재 고객 정보 수정
        D - 현재 고객 정보 삭제
        S - 현재 고객 정보 저장
        Q - 프로그램 종료
    ''').upper()


# 사용자로부터 데이타를 입력받고
# 입력 받는 데이터를 검토 한다.
# 첫번째 파라미터는 로직이어야 한다. (함수)
# 두번째 파라미터는 인풋에 사용되는 메세지 문자열
def chk_input_data(msg, func):
    while True:
        x = input(msg).upper()
        if func(x):
            break
        else:
            print('잘못입력하셨습니다. 다시 입력해 주세요.')
    return x
def do_I():
    global customers, index
    print('고객정보 입력')
    customer = { 'name':'', 'gender': '', 'email': '', 'year': 0 }
    customer['name'] = chk_input_data('이름을 입력하세요 : ',
                                        lambda x: True if len(x) > 2 else False)
    customer['gender'] = chk_input_data('성별 (M/F)를 입력하세요 : ',
                                        lambda x: True if x in ('M', 'F') else False)
    customer['email'] = chk_input_data('이메일 주소를 입력하세요 : ',
                                        lambda x: True if '@' in x else False)
    customer['year'] = chk_input_data('출생년도 4자리 입력하세요 : ',
                                        lambda x: True if len(x) == 4 and x.isdigit() else False)

    customers.append(customer)
    index = len(customers) - 1

def do_P():
    global index
    print('이전 고객 정보 조회')
    if index <= 0:
        print('이전 데이타로 이동 불가.')
        print(index)
    else:
        index -= 1
        print(f'{index + 1}번째 고객 정보 입니다.')
        print(customers[index])


def do_C():
    global index
    print('현재 고객 정보 조회')
    if index >= 0:
        print(f'{index + 1}번째 고객 정보 입니다.')
        print(customers[index])
    else:
        print('입력된 정보가 없습니다. 정보 입력은 I를 선택하세요.')


def do_N():
    global index
    print('다음 고객 정보 조회')
    if index >= (len(customers) - 1):
        print('이후 데이터 이동 불가')
        print(index)
    else:
        index += 1
        print(f'{index + 1}번째 고객 정보 입니다.')
        print(customers[index])


def do_U():
    global customers, index
    print('현재 고객 정보 수정')
    customer = { 'name':'', 'gender': '', 'email': '', 'year': 0 }
    customer['name'] = input('이름을 입력하세요 : ')
    while True:
        customer['gender'] = input('성별 (M/F)를 입력하세요 : ').upper()
        if customer['gender'] in ('M', 'F'):
            break
        else:
            print('잘못입력하셨습니다. 다시 입력 해 주세요.')
    while True:
        customer['email'] = input('이메일 주소를 입력하세요 : ')
        golbang = '@' in customer['email']
        if golbang:
            break
        else:
            print('"@"를 포함한 이메일 주소를 입력하세요.')

    while True:
        customer['year'] = input('출생년도 4자리 입력하세요 : ')
        check = len(customer['year']) == 4 and customer['year'].isdigit()
        if check:
            break
        else:
            print('잘 입력 해라....')
    customers[index] = customer


def do_D():
    print(f'현재 고객 정보{customers[index]["name"]} 삭제')
    del customers[index]
    
def do_S():
    try:
        with open('../customer/customer_list.pickle', 'wb') as save_customer_list:
            pickle.dump(customers, save_customer_list)
    except Exception as e:
        print('저장 오류: ', e)

class Customer:
    def __init__(self): 
        self.customers = list()
        self.index = -1

    # Main
    def main():
        while True:
            menu = print_menu()
            if menu == 'I':
                do_I()
            elif menu == 'P':
                do_P()
            elif menu == 'C':
                do_C()
            elif menu == 'N':
                do_N()
            elif menu == 'U':
                do_U()
            elif menu == 'D':
                do_D()
            elif menu == 'S':
                do_S()
            elif menu == 'Q':
                print('안녕히가세요~')
                break
            else:
                print('잘못 입력하셨습니다. 다시 입력 해주세요')

    if __name__ == '__main__':
        main()