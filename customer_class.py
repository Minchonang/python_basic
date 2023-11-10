from customer_mvc_view import CustomerView
from customer_mvc_model import CustomerModel
import sys
import os
import pickle
import re

file_path = 'customer/customer_list.pickle'

class CustomerController:
    def __init__(self):
        self.customers = self.customer_read()
        self.index = -1
        self.customer_view = CustomerView()
        self.customer_model = CustomerModel()

    def customer_read(self):
        if os.path.exists(file_path):
            with open(file_path, 'rb') as read_customer_list:
                return pickle.load(read_customer_list)
        else:
            return list()
    def print_menu(self):
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
    def check_email_addr(email_addr):
        regex = re.compile('^[a-zA-Z][a-zA-Z0-9]{3,50}@[a-zA-Z0-9]{2,8}[.][a-zA-Z]{2,5}$')
        return regex.search(email_addr)


    def chk_input_data(self, msg, func):
        while True:
            x = input(msg).upper()
            if func(x):
                break
            else:
                print('잘못입력하셨습니다. 다시 입력해 주세요.')
        return x

    def do_P(self, customers, index):
        print('이전 고객 정보 조회')
        if index <= 0:
            print('이전 데이타로 이동 불가.')
            print(index)
        else:
            index -= 1
            print(f'{index + 1}번째 고객 정보 입니다.')
            print(customers[index])

    def do_C(self, customers, index):
        print('현재 고객 정보 조회')
        if index >= 0:
            print(f'{index + 1}번째 고객 정보 입니다.')
            print(customers[index])
        else:
            print('입력된 정보가 없습니다. 정보 입력은 I를 선택하세요.')

    def do_N(self, customers, index):
        print('다음 고객 정보 조회')
        if index >= (len(customers) - 1):
            print('이후 데이터 이동 불가')
            print(index)
        else:
            index += 1
            print(f'{index + 1}번째 고객 정보 입니다.')
            print(customers[index])

    def do_U(self, customers, index, upper):
        print('현재 고객 정보 수정')
        customer = { 'name': '', 'gender': '', 'email': '', 'year': 0 }
        customer['name'] = self.chk_input_data('이름을 입력하세요: ',
                                            lambda x: True if len(x) > 2 else False, upper=False)
        customer['gender'] = self.chk_input_data('성별 (M/F)를 입력하세요 : ',
                                            lambda x: True if x in ('M', 'F') else False, upper=True)
        customer['email'] = self.chk_input_data('이메일 주소를 입력하세요 : ',
                                            lambda x: True if '@' in x else False, upper=False)
        customer['year'] = self.chk_input_data('출생년도 4자리 입력하세요 : ',
                                            lambda  x: True if len(x) == 4 and x.isdigit() else False, upper=False)
        print(customer)
        customers[index] = customer

    def do_D(self, customers, index):
        print(f'현재 고객 정보{customers[index]["name"]} 삭제')
        del customers[index]

    def do_S(self, customers):
        try:
            with open( 'customer/customer_list.pickle', 'wb' ) as save_customer_list:
                pickle.dump(customers, save_customer_list)
        except Exception as e:
            print('저장 오류: ', e)


    def main(self):
        while True:
            menu = self.print_menu(self.customers, self.index)
            if menu == 'I':
                self.customer_view.do_I()
                self.index = self.customer_model.do_I(self.customers, customer)
            elif menu == 'P':
                self.index = self.do_P( self.customers, self.index )
            elif menu == 'C':
                self.do_C( self.customers, self.index )
            elif menu == 'N':
                self.do_N( self.customers, self.index )
            elif menu == 'U':
                customer = self.customer_view.do_U()
                self.index = self.customer_model.do_U( self.customers, customer, self.index )
            elif menu == 'D':
                self.do_D(self.customers, self.index)
            elif menu == 'S':
                self.do_S(self.customers)
            elif menu == 'Q':
                self.do_S( self.customers, self.index )
                print('안녕히 가세요~')
                sys.exit()
                # break
            else:
                print('잘못 입력하셨습니다. 다시 입력해 주세요')

if __name__ == '__main__':
    cust = CustomerController()
    cust.main()
