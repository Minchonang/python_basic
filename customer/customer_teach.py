# I : 정보 입력
# U : 정보 수정
# D : 정보 삭제
# P : 정보 조회 (이전)
# N : 정보 조회 (이후)
# Q : 프로그램 종료
# 지속적으로 사용자에게 메뉴 정보를 화면에 출력 후 메뉴 정보를 입력 받는다.

# I : 사용자가 이름, 성별, 이메일, 출생년도를 순차적으로 입력할 수 있게 한다.
# P,N : 입력 받은 여러 명의 정보를 조회 (이전, 이후)
# P : 현재 위치가 최소 인덱스 보다 작으면 안됀다.
# N : 현재 위치가 최대 인덱스 보다 크면 안됀다.
# U,D : 현재 위치의 고객 정보를 수정, 삭제 해야 한다.
# Q : 프로그램 종료 멘트 출력 후 프로그램 종료.

# 고객 정보 자료 구조
# 이름 : 문자열
# 성별 : M, F
# 이메일 : 문자열
# 출생년도 : 정수
# customer = { 'name':'', 'gender': '', 'email': '', 'year': 1999 }

from customer.common import customer_read
from customer.common import input_menu
from customer.insert.input_i import input_i
from customer.read.input_c import input_c
from customer.read.input_n import input_n
from customer.read.input_p import input_p
from customer.update.input_u import input_u
from customer.delete.input_d import input_d
# import os



# Main
def main():
    # print('>>>>>>>>>', os.getcwd())
    # customer_read = open('../customer/customer_list.txt', 'r')
    # customer_read.close()
    customer_read()

    customers = list()
    index = -1
    while True:
        menu = input_menu()
        if menu == 'I':
            index = input_i(customers, index)

        elif menu == 'P':
            index = input_p(customers, index)

        elif menu == 'C':
            input_c(customers, index)

        elif menu == 'N':
            index = input_n(customers, index)

        elif menu == 'U':
            input_u(customers, index)

        elif menu == 'D':
            input_d(customers, index)

        elif menu == 'Q':
            print('프로그램을 종료합니다.')
            break
        else:
            print('잘못 입력하셨습니다. 다시 입력해 주세요')

if __name__ == '__main__':
    main()
