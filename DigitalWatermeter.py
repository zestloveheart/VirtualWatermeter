#coding=utf-8

from tkinter import *  # 导入 Tkinter 库
import math
import time
import threading

class DigitalWatermeter:
    watermeter_num = 1
    x = 100
    y = 100
    def __init__(self,higher,canvas):

        scale = 80
        self.watermeter_num = DigitalWatermeter.watermeter_num
        self.x = DigitalWatermeter.x + scale * (DigitalWatermeter.watermeter_num - 1)
        self.y = DigitalWatermeter.y

        self.digital = 0
        canvas.create_text(self.x, self.y , text=str(self.digital),
                           font="time 60 bold",tag = str(self.watermeter_num)+"_digital")

        canvas.create_rectangle(self.x-scale/2,self.y-scale/2,self.x+scale/2,self.y+scale/2,width = 2)
        DigitalWatermeter.watermeter_num+=1

        self.higher = higher

    def line_move(self,canvas):
        self.digital+=1

        if self.digital==10:
            self.digital=0
            self.higher.line_move(canvas)
        canvas.delete(str(self.watermeter_num) + "_digital")
        canvas.create_text(self.x, self.y, text=str(self.digital),
                           font="time 60", tag=str(self.watermeter_num) + "_digital")


        canvas.update()

if __name__ == '__main__':

    top = Tk()  # 创建窗口对象

    canvas = Canvas(top,width = 600,height = 200, bg='white') # 创建画布

    watermeter1 = DigitalWatermeter(None, canvas)                   # 创建表盘
    watermeter2 = DigitalWatermeter(watermeter1, canvas)
    watermeter3 = DigitalWatermeter(watermeter2, canvas)
    watermeter4 = DigitalWatermeter(watermeter3, canvas)
    watermeter5 = DigitalWatermeter(watermeter4, canvas)
    watermeter6 = DigitalWatermeter(watermeter5, canvas)

    canvas.pack()



    while (1):                      # 走针
        watermeter6.line_move(canvas)
        time.sleep(0.1)

    top.mainloop()  # 进入消息循环








