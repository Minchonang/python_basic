class CustomerView:
    def chk_input_data(self, msg, func, upper=True):
        while True:
            x = input(msg).upper()
            if func(x):
                break
            else:
                print('잘못입력하셨습니다. 다시 입력해 주세요.')
        return x
    def do_I(self.customers):
        print('고객 정보 입력')
        customer = {'name': '', 'gender': '', 'email': '', 'year': 0}
        with open( 'customer/customer_list.pickle', 'wb' ) as write_customer_list:
            customer['name'] = self.chk_input_data('이름을 입력하세요: ',
                                                    lambda x: True if len(x) > 2 else False, upper=False)
            customer['gender'] = self.chk_input_data('성별 (M/F)를 입력하세요 : ',
                                                    lambda x: True if x in ('M', 'F') else False, upper=True)
            customer['email'] = self.chk_input_data('이메일 주소를 입력하세요 : ',
                                                    lambda x: True if self.check_email_addr(x) else False, upper=False)
            customer['year'] = self.chk_input_data('출생년도 4자리 입력하세요 : ',
                                                    lambda x: True if len(x) == 4 and x.isdigit() else False, upper=True)
            return customer
            # customers.append(customer)
            # pickle.dump(customers, write_customer_list)
        # print(customer)
        # print('전체 고객: ', customers)
        # # 새로 입력한 고객 정보의 위치 적용 여부 고민
        # index = len(customers) - 1

    def do_U(self.customers):
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
        return customer