from tkinter import messagebox
import tkinter 
from connect_seu import *
from encrypt import *
import webbrowser
import ctypes
import sys

def writeinfo(a,b,c):
    with open(a,"wb") as f:  
        f.write(str.encode(b)+c)

def web():
    webbrowser.open("http://w.seu.edu.cn")

def UAC():
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.argv[0] , None , None, 1) 
class Login_window():
    Adress=[]
    H=[]
    V=[]
    def __init__(self,a): 
        self.Adress=a
        self.background = tkinter.Tk()  
        #账号密码的label
        self.label_account = tkinter.Label(self.background, text='一卡通账号') 
        self.label_password = tkinter.Label(self.background, text='一卡通密码')
        #warning的label
        typeface="微软雅黑"
        size=9
        self.label_waning1 = tkinter.Label(self.background, text='首次启动需要保存登录信息，以后直接双击程序即开始自动连接',font=(typeface,size))
        self.label_waning2 = tkinter.Label(self.background, text='为了保证保存的账号密码无误，请先',font=(typeface, size))
        self.label_waning4 = tkinter.Label(self.background, text='——————————————————————————',font=(typeface,size))
        self.label_waning5 = tkinter.Label(self.background, text='Written by lbh, thank you for using.')
        # 账号密码输入框  
        self.input_ID = tkinter.Entry(self.background, width=15) 
        self.input_pwd = tkinter.Entry(self.background, show='*',  width=15)  
        # 创建按钮
        self.button_seu = tkinter.Button(self.background, command =web , text ='注销SEU登陆',width=18)
        self.button_save = tkinter.Button(self.background, command = self.get_connect, text ='保存并连接',width=12)
        self.button_startup = tkinter.Button(self.background, command =UAC, text ='设置开机自启',width=12)  
        # 位置布局
        dev=4
        lx0,ly0,ldx,ldy=10,5,0,25
        self.label_waning1.place(x=lx0, y=ly0)
        self.label_waning2.place(x=lx0, y=ly0+ldy)
        self.button_seu.place(x=210, y=ly0+ldy-dev)
        self.label_waning4.place(x=lx0, y=ly0+ldy*2)
        xx,yy=40,ly0+ldy*2+25
        dx,dy=70,35
        self.label_account.place(x=xx, y=yy)  
        self.label_password.place(x=xx, y=yy+dy)  
        self.input_ID.place(x=xx+dx, y=yy)  
        self.input_pwd.place(x=xx+dx, y=yy+dy)
        a=220
        self.button_save.place(x=a, y=yy-dev)
        self.button_startup.place(x=a,y=yy+dy-dev)

        self.V=int(28*12.5+lx0)         #9号字 28个
        self.H=yy+2*dy
        #COPYRIGHT
        self.label_waning5.place(x=self.V/2-18*6, y=yy+2*dy)         #36个字母
        #
        self.background.title("seu-wlan一键连接")  
        self.background.geometry(str(self.V)+'x'+str(self.H))
        #控制窗口尺寸
        self.background.minsize(self.V, self.H)
        self.background.maxsize(self.V, self.H+dy)
        #win.resizable(0,0)
        #
        self.center_window(self.V,self.H)
        
        
    # 按钮触发的函数：获取登录信息和连接   !数据传输是核心，不用指针的话，只能往下传输(单向)，不能改写原本的，没意义
    def get_connect(self):                                                     #类中函数可以在后面，类是先进行完整声明的#类的方法(即函数)与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称, 按照惯例它的名称是 self
        b = self.input_ID.get()                           #ljust(10," ")是对字符进行调整，所以这里我用不上，也就不用account=account[:-1]来减去空格了
        c = encrypt(self.input_pwd.get())    #顺手就给加密了
        k=connect_seu(b,c)
        if k==1:
            writeinfo(self.Adress,b,c)
            tkinter.messagebox.showinfo(title='保存成功', message='请关闭窗口')
        elif k==2:
            writeinfo(self.Adress,b,c)
            tkinter.messagebox.showinfo(title='保存成功', message='可以联网但学校网络有问题，之后连不上请联系作者') 
        else:
            tkinter.messagebox.showinfo(title='保存失败', message='请重新确认账号密码')  

    def center_window(self,w,h):
        # 获取屏幕 宽、高
        ws = self.background.winfo_screenwidth()
        hs = self.background.winfo_screenheight()
        # 计算 x, y 位置
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        self.background.geometry('%dx%d+%d+%d' % (w, h, x, y)) #第一个数横大小，第二个数纵大小，第三个数离左屏幕边界距离，第四个数离上面屏幕边界距离。

def GUI(a):
    # 初始化对象  
    L = Login_window(a)
    # 主程序执行?
    tkinter.mainloop()  

if __name__ == '__main__':
    address="C:\\Users\\Public\\seu-wlan_userinfo.txt"
    GUI(address)
