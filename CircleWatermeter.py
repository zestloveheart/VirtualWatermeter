#coding=utf-8

from tkinter import *  # 导入 Tkinter 库
import math
import time
import threading
class Watermeter:
    watermeter_num = 1

    def __init__(self,higher,canvas,x,y,r = 0.6):
        scale = 100
        self.x = x*scale
        self.y = y*scale
        self.r = r*scale

        self.watermeter_num = Watermeter.watermeter_num
        canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, width = 4)

        self.angle = 0

        canvas.create_line(self.x, self.y, self.x + math.sin(self.angle * math.pi / 180) * self.r * 0.8,
                           self.y - math.cos(self.angle * math.pi / 180) * self.r * 0.8, width=2,
                           tag=str(self.watermeter_num) + "_line")
        canvas.create_text(self.x,self.y+self.r*1.2, text="x"+str(pow(10,4-self.watermeter_num)), font="time 20")
        Watermeter.watermeter_num+=1

        self.higher = higher

    def line_move(self):
        self.angle+=6
        canvas.delete(str(self.watermeter_num) + "_line")
        canvas.create_line(self.x, self.y, self.x + math.sin(self.angle * math.pi / 180) * self.r * 0.8,
                           self.y - math.cos(self.angle * math.pi / 180) * self.r * 0.8, width=2,
                           tag=str(self.watermeter_num) + "_line")

        if self.angle==360:
            self.angle=0
            self.higher.line_move()
        canvas.update()



if __name__ == '__main__':
    print(math.cos(3.14))
    top = Tk()  # 创建窗口对象

    canvas = Canvas(top,width = 600,height = 600, bg='white') # 创建画布
    watermeter1 = Watermeter(None,canvas,2,5)                   # 创建表盘
    watermeter2 = Watermeter(watermeter1,canvas, 1, 4)
    watermeter3 = Watermeter(watermeter2,canvas,1,2,)
    watermeter4 = Watermeter(watermeter3,canvas,2,1,)
    watermeter5 = Watermeter(watermeter4,canvas,4,1,)
    watermeter6 = Watermeter(watermeter5,canvas,5,2,)
    watermeter7 = Watermeter(watermeter6,canvas,5,4,)
    watermeter8 = Watermeter(watermeter7,canvas,4,5,)
    canvas.pack()

    while (1):                      # 走针
        watermeter8.line_move()

    top.mainloop()  # 进入消息循环

