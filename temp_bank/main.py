import imp
from encryption import encryption
from hardware import hardware
from checkstatus import checkstatus
from bankapi import bankapi
import time
class main():
    while True:
        print("Welcome to tempbank atm! \n")
        print(checkstatus().status_dict)
        bankapi_module = bankapi()
        menu = str(input("\n Choose your menu \n 1.Balance 2.Deposit 3.Withdraw 4.END : "))
        if  menu == '1' :
            print("please input your card...\n")
            time.sleep(1)
            card_in = hardware().check_card()
            if card_in == True:
                card_num = hardware().read_cardnum()
                card_pw = hardware().read_pasword()
                print("processing...")
                time.sleep(1)
                if bankapi_module.check_pw(card_num=card_num,user_input=card_pw) == True:
                    print("Your Blance is : {dollar}$".format(dollar=bankapi_module.saved_money))
                    input("Pass to Enter")
                    time.sleep(1)
                else :
                    print("password worng")
            else :
                print("serrvice can be use in card")

        elif menu == '2' :
            print("please input your card...\n")
            time.sleep(1)
            card_in = hardware().check_card()
            if card_in == True:
                card_num = hardware().read_cardnum()
                card_pw = hardware().read_pasword()
                print("processing...")
                time.sleep(1)
                if bankapi_module.check_pw(card_num=card_num,user_input=card_pw) == True:
                    print("{dollar}$ Deposit is warking... :".format(dollar=hardware().read_billbox()))
                    time.sleep(1)
                    bankapi_module.send_money(card_num=card_num,bill=hardware().read_billbox())
                    print("Done!")
                    input("Pass to Enter")
                    time.sleep(1)
                else :
                    print("password worng")
            else :
                print("serrvice can be use in card")

        elif menu == '3' :
            print("please input your card...\n")
            time.sleep(1)
            card_in = hardware().check_card()
            if card_in == True:
                card_num = hardware().read_cardnum()
                card_pw = hardware().read_pasword()
                print("processing...")
                time.sleep(1)
                if bankapi_module.check_pw(card_num=card_num,user_input=card_pw) == True:
                    withdraw_cash = int(input("How much do you want to withdraw? :"))
                    time.sleep(1)
                    if withdraw_cash <= bankapi_module.saved_money :
                        bankapi_module.withdrew_money(card_num=card_num,bill=withdraw_cash)
                        print("Done")
                    else :
                        print("Too mouch!")
                    input("Pass to Enter")
                    time.sleep(1)
                else :
                    print("password worng")
            else :
                print("serrvice can be use in card")

        elif menu == '4' : break

        else : print("Worng Menu")

if __name__ == "__main__":
    main()