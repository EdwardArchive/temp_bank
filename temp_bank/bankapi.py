from tkinter.tix import Tree
from urllib import response
import requests
from encryption import encryption

class bankapi():

    #금액 API를 통해 정보를 가져올수 없으므로 300$로 시작하여서 변동됩니다.
    saved_money = 300

    def __init__(self):
        #은행 API의 예시 주소입니다 동작은 하지 않습니다. 따라서 실행할때 마다 기본값을 넣어두었습니다.
        self.base_api_url = "http://restapi.example.com/bankapi/"
        self.status_api_url = "http://restapi.example.com/bankapi/status"
        self.status_atm_api_url=  "http://restapi.example.com/bankapi/atm/version"
        self.pw_api_url = "http://restapi.example.com/bankapi/card/check"
        self.send_api_url = "http://restapi.example.com/bankapi/card/sned"
        self.cash_check_api_url = "http://restapi.example.com/bankapi/card/cashscheck"
        self.withdrew_money_api_url = "http://restapi.example.com/bankapi/card/withdrew" 
    
    def check_status(self):
        try:
            response = requests.get(self.status_api_url)
            res=response.json()
        except:
            res = "API is Working"
        return res

    def check_sw_status(self):
        try:
            response = requests.get(self.status_atm_api_url)
            res=response.json()
        except:
            res ="1.0.7 KBank"
        return res

    def check_pw(self,card_num,user_input):
        try:
            response = requests.get(self.pw_api_url+encryption.encryption_logic(card_num)+"?"+encryption.encryption_logic(user_input))
            res=response.json()
        except:
            if card_num == '1520-0000-2020-2022' and user_input == '2022':
                res = True
            else :
                res = False
        return res

    def send_money(self,card_num,bill):
        try:
            response = requests.get(self.send_api_url+encryption.encryption_logic(card_num)+"?"+encryption.encryption_logic(bill))
            res=response.json()
        except:
            print("dd")
            res = True
            bankapi.saved_money += bill
        
        return res
    
    def get_money(self,card_num,user_input):
        try:
            response = requests.get(self.cash_check_api_url+encryption.encryption_logic(card_num)+"?"+encryption.encryption_logic(user_input))
            res=response.json()
        except:
            if card_num == '1520-0000-2020-2022' and user_input == '2022':
                res = bankapi.saved_money
            else :
                res = False
        return res

    def withdrew_money(self,card_num,bill):
        try:
            response = requests.get(self.send_api_url+encryption.encryption_logic(card_num)+"?"+encryption.encryption_logic(bill))
            res=response.json()
        except:
            res = True
            bankapi.saved_money -= bill