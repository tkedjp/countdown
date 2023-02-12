import tkinter
# from tkinter import ttk
from tkinter import *
from tkmacosx import Button

from time import sleep
import time
from playsound import playsound

# ウィンドウの作成
root = tkinter.Tk()
root.title('タイマー')
root.geometry('350x320')
root.resizable(0, 0)

#フォント
basic_font = ('Arial', 70, 'bold')

#フレームの作成
time_frame = tkinter.Frame(root)
time_select_frame = tkinter.Frame(root)
button_frame = tkinter.Frame(root)
time_frame.pack()
time_select_frame.pack()
button_frame.pack()

#時間設定
minute=StringVar()
minute.set('00')
second=StringVar()
second.set('00')

#ラベル
minute_label = tkinter.Label(time_frame, textvariable=minute, font=basic_font, fg='black')
minute_label.grid(row=1, column=2, padx=5, pady=15, ipadx=4, ipady=4)
colon_label = tkinter.Label(time_frame, text=':', font=basic_font, fg='black')
colon_label.grid(row=1, column=3, padx=5, pady=15, ipadx=4, ipady=4)
second_label = tkinter.Label(time_frame, textvariable=second, font=basic_font, fg='black')
second_label.grid(row=1, column=4, padx=5, pady=15, ipadx=4, ipady=4)

def Timer():
    # global minute,second
    times=int(minute.get())*60 + int(second.get())

    while times > -1:
        minute, second=(times//60, times %60)
        # hour=0
        if minute>60:
            minute=(minute//60, minute%60)

        second.set(second)
        minute.set(minute)

        time_frame.update()
        time.sleep(1)

        if (times==0):
            playsound("bell.mp3")
            second.set("00")
            minute.set("00")

        times -= 1

def three():
    minute.set("03")
    second.set("00")

def four():
    minute.set("04")
    second.set("00")

def five():
    minute.set("05")
    second.set("00")

#時間設定
stop_button = Button(time_select_frame, text='3分', command=three)
stop_button.grid(row=1, column=1, padx=5, pady=20, ipadx=3, ipady=3)
stop_button = Button(time_select_frame, text='4分', command=four)
stop_button.grid(row=1, column=2, padx=5, pady=20, ipadx=3, ipady=3)
stop_button = Button(time_select_frame, text='5分', command=five)
stop_button.grid(row=1, column=3, padx=5, pady=20, ipadx=3, ipady=3)

#ボタン
start_button = Button(button_frame, text='START', command=Timer)
start_button.grid(row=1, column=1, padx=5, pady=20, ipadx=3, ipady=3)
reset_button = Button(button_frame, text='RESET')
reset_button.grid(row=1, column=2, padx=5, pady=20, ipadx=3, ipady=3)

# ウィンドウのループ処理
root.mainloop()
