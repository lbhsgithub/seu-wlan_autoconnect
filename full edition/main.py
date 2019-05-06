from connect_seu import *
from GUI import *
from os import path
import shutil
import sys
import ctypes

ADDRESS="C:\\Users\\Public\\seu-wlan_userinfo.txt" 
StartUpADD="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\StartUp"

class I():
    user_ID=[]
    user_pwd=[]
    address=[]
    def __init__(self,a):
        self.address=a    
    def readinfo(self):
        with open(self.address,"rb") as f1:
            _byte = f1.read()
        self.user_ID=bytes.decode( _byte[:9])
        self.user_pwd=_byte[9:]

def main():
    if (sys.path[0]!=StartUpADD)&(ctypes.windll.shell32.IsUserAnAdmin()==1):
        shutil.copy(sys.argv[0],StartUpADD)
    else:
        if path.exists(ADDRESS):
            info=I(ADDRESS)
            info.readinfo()
            connect_seu(info.user_ID,info.user_pwd)
        else:
            GUI(ADDRESS)

main()
