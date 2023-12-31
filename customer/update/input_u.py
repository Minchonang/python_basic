from customer.common import chk_input_data
def input_u(customers, index):
    print('현재 고객 정보 수정')
    customer = { 'name': '', 'gender': '', 'email': '', 'year': 0 }
    customer['name'] = chk_input_data('이름을 입력하세요: ',
                                        lambda x: True if len(x) > 2 else False, upper=False)
    customer['gender'] = chk_input_data('성별 (M/F)를 입력하세요 : ',
                                        lambda x: True if x in ('M', 'F') else False, upper=True)
    customer['email'] = chk_input_data('이메일 주소를 입력하세요 : ',
                                        lambda x: True if '@' in x else False, upper=False)
    customer['year'] = chk_input_data('출생년도 4자리 입력하세요 : ',
                                        lambda  x: True if len(x) == 4 and x.isdigit() else False, upper=False)
    print(customer)
    customers[index] = customer
