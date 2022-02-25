from hardware import hardware
from bankapi import bankapi

class checkstatus():
    
    def __init__(self):
        self.status_dict = {
            "API Status":self.check_api(),
            "Software Version(Now)" : self.check_offline_software(),
            "Software Version(Online)" : self.check_online_software(),
            "HW_Status" : self.check_hardware()
        }
    
    def get_status(self) :
        return self.status_dict

    def check_hardware(self):
        hw_check = {
        "CashBox":"OK",
        "Card reader":"OK",
        "Bill Box":"OK",
        "Baknote counter ":"OK"
        }
        return hw_check
    
    def check_offline_software(self):
        software_status = hardware().get_sw_status()
        return software_status

    def check_api(self):
        api_status = bankapi().check_status()
        return api_status
    
    def check_online_software(self) :
        software_status = bankapi().check_sw_status()
        return software_status

