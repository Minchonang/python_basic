# I : 정보 입력
# U : 정보 수정
# D : 정보 삭제
# P : 정보 조회 (이전)
# N : 정보 조회 (이후)
# Q : 프로그램 종료
# 지속적으로 사용자에게 메뉴 정보를 화면에 출력 후 메뉴 정보를 입력 받는다.

# I : 사용자가 이름, 성별, 이메일, 출생년도를 순차적으로 입력할 수 있게한다.
# P,N : 입력받은 여러명의 정보를 조회 (이전, 이후)
# P : 현재 위치가 최소 인덱스 보다 작으면 안됀다.
# N : 현재 위치가 최대 인덱스 보다 크면 안됀다.
# U,D : 현재 위치의 고객정보를 수정, 삭제 해야 한다.
# Q : 프로그램 종료 멘트 출력 후 프로그램 종료.

# 고객정보 자료구조
# 이름 : 문자열
# 성별 : M, F
# 이메일 : 문자열
# 출생년도 : 정수
# customer = { 'name':'', 'gender': '', 'email': '', 'year': 1999 }

customers = list()
index = 0
# 나중에 지우기!!!
# temp = {'name':'손정현', 'gender': 'M', 'email' : 's@s', 'year': 1999}
# customers.append(temp)
# index = len(customers) - 1


def genderTest(customer):
    customer["gender"] = input("성별 (M/F)를 입력하세요 : ").upper()
    if customer["gender"] in ("M", "F"):
        return customer["gender"]
    else:
        print("잘못입력하셨습니다. 다시 입력 해 주세요.")
        return genderTest(customer)


def emailTest(customer):
    customer["email"] = input("이메일 주소를 입력하세요 : ")
    golbang = "@" in customer["email"]
    if golbang:
        return customer["email"]
    else:
        print('"@"를 포함한 이메일 주소를 입력하세요.')
        return emailTest(customer)


# 이메일 중복 로직 추가~~~~


def yearTest(customer):
    customer["year"] = input("출생년도 4자리 입력하세요 : ")
    check = len(customer["year"]) == 4 and customer["year"].isdigit()
    if check:
        return customer["year"]
    else:
        print("잘 입력 해라....")
        return yearTest(customer)


def inputI():
    global index
    print("고객정보 입력")
    customer = {"name": "", "gender": "", "email": "", "year": 0}
    customer["name"] = input("이름을 입력하세요 : ")
    customer["gender"] = genderTest(customer)
    customer["email"] = emailTest(customer)
    customer["year"] = yearTest(customer)

    print(f"입력한 정보: {customer}")
    customers.append(customer)
    print(f"전체 고객 정보: {customers}")
    # 새로 입력한 고객 정보의 위치 적용 여부 고민

    index = len(customers) - 1


def inputP():
    print("이전 고객 정보 조회")
    global index
    if index < 0:
        print("이전 데이타로 이동 불가.")
        print(index)
    else:
        index -= 1
        print(f"{index + 1}번째 고객 정보 입니다.")
        print(customers[index])


def inputC():
    global index
    print("현재 고객 정보 조회")
    if index >= 0:
        print(f"{index + 1}번째 고객 정보 입니다.")
        print(customers[index])
    else:
        print("입력된 정보가 없습니다. 정보 입력은 I를 선택하세요.")


def inputN():
    print("다음 고객 정보 조회")
    global index
    if index >= (len(customers) - 1):
        print("이후 데이터 이동 불가")
        print(index)
    else:
        index = 0
        print(f"{index + 1}번째 고객 정보 입니다.")
        print(customers[index])


def inputU(index):
    print("현재 고객 정보 수정")
    customer = {"name": "", "gender": "", "email": "", "year": 0}
    # 수정 할 고객 정보 검색 기능
    # 수정 내용이 없는 항목은 이전 값 유지 하도록.
    customer["name"] = input("이름을 입력하세요 : ")
    # customers[index]['name'] = input('이름을 입력하세요 : ')
    customer["gender"] = genderTest(customer)
    customer["email"] = emailTest(customer)
    customer["year"] = yearTest(customer)

    print(customer)
    customers[index] = customer


def inputD():
    global index
    if len(customers) >= 1:
        print(f'현재 고객 정보{customers[index]["name"]} 삭제')
        real = input("정말 삭제하시겠습니까? Y/N: ").upper()
        if real == "Y":
            print(f'{customers[index]["name"]}를 삭제하였습니다.')

            index -= 1
            del customers[index]

        elif real == "N":
            print("삭제를 취소합니다.")
        else:
            inputD()
    else:
        print("저장된 정보가 없습니다.")


def print_menu():
    return input(
        """
        다음 중에서 하실 작업의 메뉴를 입력하세요.
        I - 고객 정보 입력
        P - 이전 고객 정보 조회
        C - 현재 고객 정보 조회
        N - 다음 고객 정보 조회
        U - 현재 고객 정보 수정
        D - 현재 고객 정보 삭제
        Q - 프로그램 종료
    """
    ).upper()


# Main

while True:
    menu = print_menu()

    if menu == "I":
        inputI()
    elif menu == "P":
        inputP()
    elif menu == "C":
        inputC()
    elif menu == "N":
        inputN()
    elif menu == "U":
        inputU(index)
    elif menu == "D":
        inputD()
    elif menu == "Q":
        print("안녕히가세요~")
        break
    else:
        print("잘못 입력하셨습니다. 다시 입력해 주세요")
