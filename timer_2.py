import tkinter
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
min=StringVar()
min_label = tkinter.Label(time_frame, textvariable=min, font=basic_font, fg='black')
min.set('0')
min_label.grid(row=1, column=2, padx=5, pady=15, ipadx=4, ipady=4)

colon_label = tkinter.Label(time_frame, text=':', font=basic_font, fg='black')
colon_label.grid(row=1, column=3, padx=5, pady=15, ipadx=4, ipady=4)

sec=StringVar()
sec_label = tkinter.Label(time_frame, textvariable=sec, font=basic_font, fg='black')
sec.set('00')
sec_label.grid(row=1, column=4, padx=5, pady=15, ipadx=4, ipady=4)

stop_counter = False

def unlock_button():
    min_label.config(fg='black')
    colon_label.config(fg='black')
    sec_label.config(fg='black')
    three_mins_button.config(state=NORMAL)
    four_mins_button.config(state=NORMAL)
    five_mins_button.config(state=NORMAL)
    start_button.config(state=NORMAL)

def Timer():
    global sec,min,stop_counter
    three_mins_button.config(state=DISABLED)
    four_mins_button.config(state=DISABLED)
    five_mins_button.config(state=DISABLED)
    start_button.config(state=DISABLED)

    times=int(min.get())*60+int(sec.get())

    while times > -1:
        minute, second=(times//60, times%60)

        sec.set(second)
        min.set(minute)

        time_frame.update()
        time.sleep(1)

        if (times==0):
            unlock_button()
            playsound("bell.mp3")
            sec.set("00")
            min.set("0")
            time_frame.update()
            stop_counter = True
        
        if stop_counter:
            stop_counter = False
            return

        times -= 1

        if times < 16:
            min_label.config(fg='red')
            colon_label.config(fg='red')
            sec_label.config(fg='red')

def three():
    min.set("0")
    sec.set("05")

def four():
    min.set("4")
    sec.set("00")

def five():
    min.set("5")
    sec.set("00")

def stop():
    global sec,min,stop_counter
    unlock_button()

    sec.set("00")
    min.set("0")
    time_frame.update()
    stop_counter = True

#時間設定
three_mins_button = Button(time_select_frame, text='3分', command=three)
three_mins_button.grid(row=1, column=1, padx=5, pady=20, ipadx=3, ipady=3)
four_mins_button = Button(time_select_frame, text='4分', command=four)
four_mins_button.grid(row=1, column=2, padx=5, pady=20, ipadx=3, ipady=3)
five_mins_button = Button(time_select_frame, text='5分', command=five)
five_mins_button.grid(row=1, column=3, padx=5, pady=20, ipadx=3, ipady=3)

#ボタン
start_button = Button(button_frame, text='START', command=Timer)
start_button.grid(row=1, column=1, padx=5, pady=20, ipadx=3, ipady=3)
stop_button = Button(button_frame, text='STOP', command=stop)
stop_button.grid(row=1, column=2, padx=5, pady=20, ipadx=3, ipady=3)

# ウィンドウのループ処理
root.mainloop()