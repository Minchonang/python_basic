customer_list = {}
Index = 0
keys = ['index', 'name', 'sex', 'email', 'birth']
while True:
    i = 0
    user_input = input('I : 고객 정보 입력\nP : 이전 정보\nN : 다음 정보\nU : 정보 수정\nD : 정보 삭제\nQ : 프로그램 종료\n')
    print(user_input)

    if user_input.lower() == 'i':
        customer = {}
        for key in keys:
            if key == 'index':
                customer[key] = Index
            else:
                value = input(f'Enter {key}\n')
                customer[key] = value
        customer_list[Index] = customer
        print(customer_list)
        Index += 1

    elif user_input.lower() == 'n':
        i += 1
        print(customer_list[i], '\n')

    elif user_input.lower() == 'p':
        i -= 1
        print(customer_list[i], '\n')

    elif user_input.lower() == 'q':
        print("program end")
        break

# 고객관리 프로그램
# 고객의 정보 : 이름, 성별, 이메일, 출생년도
# 고객의 정보는 입력받아 본인이 선택한 자료구조에 저장해야 함.
# 이름은 문자열, 성멸은 남자M, 여자F, 이메일은 문자열, 태어난 연도는 정수로 저장
# 고객 관리 프로그램은 고객의 정보를 CRUD할 수 잇는 기능이 있어야 함.
# 고객 정보를 파일에 저장하는 기능을 구현하지 않아도 됨.
# "I"를 눌러 고객의 정보를 입력받기
# 저장된 고객 정보는 "P" 또는 "N"을 눌러 이전 고객정보 또는 다음 고객정보를 조회할 수 있어야 함.
# 조회한 고객 정보는 "U" 를 눌러 새로운 정보로 수정할 수 있어야 함.
# "D" 를 누르면 조회한 고객 정보를 삭제해야 함.
# 프로그램의 종료는 "Q" 를 누릅니다.
# 로컬 변수 : customer_list(전체 데이터저장용 변수), Index(현재 위치 저장용 변수)
# 입력 데이터 값의 타입 및 크기(길이)를 체크 해야 함.
# 패키지를 활용 하고 문자출력(메세지, 메뉴) 전용 함수와 데이터를 처리하는 함수를 별도의 모듈로 정리
# 네비게이터 : 소스 및 기능, 문법 설명
# 드라이버 : 네비게이터가 설명 해주는 대로 코딩

'''
고객 정보는 딕셔너리 타입으로, 4개의 항목으로 저장
각각의 타입은 문자열, 문자열(조건->M, F), 문자열, 정수
조건에 따라 >  switch or if 사용
눌러 > input() 사용

확인해야 할 것들
input이 
'''
