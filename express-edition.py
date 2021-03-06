from subprocess import run
from time import sleep
from ctypes import windll
import requests

SSID='seu-wlan'
test="ping www.baidu.com"

def post_seu(a,b):
        post_addr="https://xxxxxxxxxxxxxxxxxxxxx"
        post_header={
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'Accept-Encoding': 'gzip, deflate,br',
                'Accept-Language': 'zh-Hans-CN,zh-Hans;q=0.8,en-US;q=0.5,en;q=0.3',
                'Connection': 'keep-alive',
                'Content-Length': '56',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'w.seu.edu.cn',
                'Origin': 'https://xxxxxxxxxxxxxxxxxxxxx',
                'Referer': 'https://xxxxxxxxxxxxxxxxxxxxx',
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134',
                'X-Requested-With': 'XMLHttpRequest',
                'Cookie': 'think_language=zh-Hans-CN; sunriseUsername='+a+'',
                'Cache-Control': 'max-age=0'
                }

        post_data ={
                'username': a,
                'password': b,
                'enablemacauth': '0'
                }
        requests.post(post_addr, data=post_data, headers=post_header,verify=False)

def resetIP(a):
        run("ipconfig/release",shell=True)
        run("ipconfig/renew",shell=True)
        sleep(a)  

def connect_seu(ID,pwd):

        run('netsh wlan connect name='+SSID)
        sleep(3)
        
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
                                print("X post→w.seu FAIL-----network is not connected, try to reset IP address") 
                                resetIP(1)
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

if __name__ == '__main__':
    connect_seu('xxxxxxx',b'xxxxxxxxx')
    input()
