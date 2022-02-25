class hardware():
    
    def read_cardnum(self):
        cardnum = '1520-0000-2020-2022'
        return cardnum

    def read_cardbox(self):
        inout = True
        return inout

    def read_billbox(self):
        bill = 253
        return bill

    def read_pasword(self):
        password = str(input("please input card pw : "))
        return password

    def check_card(self):
        card_inout = hardware.read_cardbox(self)
        return card_inout
    
    def check_bill(self):
        bill = hardware.read_billbox(self)
        return bill

    def get_cardnum(self):
        cardnum = hardware.read_cardnum(self)
        return cardnum
    
    def get_sw_status(self):
        version = '1.0.7 KBank'
        return version