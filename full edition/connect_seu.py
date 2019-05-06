from subprocess import run
from time import sleep
from ctypes import windll
from post_seu import *

SSID='seu-wlan'
test="ping www.baidu.com"

def resetIP(a):
        run("ipconfig/release",shell=True)
        run("ipconfig/renew",shell=True)
        sleep(a)  

def connect_seu(ID,pwd):

        run('netsh wlan connect name='+SSID)
        sleep(2)
        
        SW=0
        while SW==0:
                try:
                        post_seu(ID,pwd)
                except:
                        print("post→w.seu FAIL,possible causes:①IP error②campus network server error")
                        if run(test,shell=True).returncode==0:
                                print("√ post→w.seu FAIL-----while network is connected, no need for further operation")
                                SW=2
                        else:
                                print("X post→w.seu FAIL-----network is not connected, try to reset IP address") #只有这个需要循环
                                resetIP(4)
                else:
                        print("post→w.seu SUCCEEDD")
                        if run(test,shell=True).returncode==0:
                                print("√ post→w.seu SUCCEEDD-----network is connected, no need for further operation")
                                SW=1
                        else:
                                print("X post→w.seu SUCCEEDD-----while network is not connected, possible causes:①ID|password error②arrearage")
                                windll.user32.MessageBoxW(0,"可能是账号密码错误或欠费","网络连接失败",1|16)
                                SW=3
        return SW
