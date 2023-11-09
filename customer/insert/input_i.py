from customer.common import chk_input_data
import pickle
import re

def check_email_addr(email_addr):
    regex = re.compile('^[a-zA-Z][a-zA-Z0-9]{3, 50}@[a-zA-Z0-9]{2, 8}[.][a-zA-Z]{2,5}$')
    return regex.search(email_addr)

def input_i(customers, index):
    print('고객 정보 입력')
    customer = {'name': '', 'gender': '', 'email': '', 'year': 0}
    with open('../customer/customer_list.pickle', 'wb') as write_customer_list:
        customer['name'] = chk_input_data('이름을 입력하세요: ',
                                            lambda x: True if len(x) > 2 else False, upper=False)
        customer['gender'] = chk_input_data('성별 (M/F)를 입력하세요 : ',
                                            lambda x: True if x in ('M', 'F') else False, upper=True)
        customer['email'] = chk_input_data('이메일 주소를 입력하세요 : ',
                                            lambda x: True if check_email_addr(x) else False, upper=False)
        customer['year'] = chk_input_data('출생년도 4자리 입력하세요 : ',
                                            lambda x: True if len(x) == 4 and x.isdigit() else False, upper=True)
        customers.append(customer)
        pickle.dump(customers, write_customer_list)
    print(customer)
    print('전체 고객: ', customers)
    # 새로 입력한 고객 정보의 위치 적용 여부 고민
    index = len(customers) - 1
    return index
