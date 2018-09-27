from source.VirtualWatermeter.CircleWatermeter import *
from source.VirtualWatermeter.DigitalWatermeter import *



if __name__ == '__main__':

    top = Tk()  # 创建窗口对象

    canvas = Canvas(top, width=600, height=600, bg='white')  # 创建画布

    watermeter4 = DigitalWatermeter(None, canvas)  # 创建表盘
    watermeter5 = DigitalWatermeter(watermeter4, canvas)
    watermeter6 = DigitalWatermeter(watermeter5, canvas)
    watermeter7 = DigitalWatermeter(watermeter6, canvas)
    watermeter8 = DigitalWatermeter(watermeter7, canvas)

    watermeter1 = CircleWatermeter(watermeter8, canvas, 5, 4, )
    watermeter2 = CircleWatermeter(watermeter1, canvas, 4, 5, )
    watermeter3 = CircleWatermeter(watermeter2, canvas, 2, 5)  # 创建表盘
    canvas.pack()

    while (1):  # 走针
        watermeter2.line_move(canvas)

    top.mainloop()  # 进入消息循环
