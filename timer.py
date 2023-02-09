import tkinter
# from tkinter import ttk
from tkinter import *
from tkmacosx import Button

from time import sleep
import time
import pygame.mixer as pymix

# ウィンドウの作成
root = tkinter.Tk()
root.title('タイマー')
root.geometry('350x320')
root.resizable(0, 0)

#フォント
basic_font = ('Arial', 70, 'bold')

# 変数の宣言
minute=StringVar()
second=StringVar()

# デフォルト値を0に設定
minute.set('00')
minute = int(minute.get())
second.set('00')
second = int(second.get())

def three():
    global minute,second
    minute = 3
    second = 0
    temp = int(minute)*60 + int(second)
    print(temp)
    mins,secs = divmod(temp,60)
    print(mins, secs)

    # format() メソッドを用いて、小数点以下2桁までの値を格納
    minute = ("{00:2d}".format(mins))
    second = ("{00:2d}".format(secs))
    print(minute, second)

    # 毎回、temp値をデクリメントしてからGUIウィンドウを更新する
    minute_label.update()
    second_label.update()
    time.sleep(1)

    # tempが0になったら鐘を鳴らす
    if temp is 0:
        bell()

    # 1秒ごとにtmpを1つづ減らす
    temp -= 1
    minute_label.update()
    second_label.update()

# def four():
#     global minute,second

# def five():
#     global minute,second


def bell():
	pymix.init()
	sound_file = ''
	sounds = pymix.Sound(sound_file)
	sounds.play()

#フレームの作成
time_frame = tkinter.Frame(root)
time_select_frame = tkinter.Frame(root)
button_frame = tkinter.Frame(root)
time_frame.pack()
time_select_frame.pack()
button_frame.pack()

#ディスプレイ
minute_label = tkinter.Label(time_frame, text=minute, font=basic_font, fg='black')
minute_label.grid(row=1, column=2, padx=5, pady=15, ipadx=4, ipady=4)
colon_label = tkinter.Label(time_frame, text=':', font=basic_font, fg='black')
colon_label.grid(row=1, column=3, padx=5, pady=15, ipadx=4, ipady=4)
second_label = tkinter.Label(time_frame, text=second, font=basic_font, fg='black')
second_label.grid(row=1, column=4, padx=5, pady=15, ipadx=4, ipady=4)

#時間設定
stop_button = Button(time_select_frame, text='3分', command=three)
stop_button.grid(row=1, column=1, padx=5, pady=20, ipadx=3, ipady=3)
stop_button = Button(time_select_frame, text='4分')
stop_button.grid(row=1, column=2, padx=5, pady=20, ipadx=3, ipady=3)
stop_button = Button(time_select_frame, text='5分')
stop_button.grid(row=1, column=3, padx=5, pady=20, ipadx=3, ipady=3)

#ボタン
stop_button = Button(button_frame, text='STOP')
stop_button.grid(row=1, column=1, padx=5, pady=20, ipadx=3, ipady=3)
reset_button = Button(button_frame, text='RESET')
reset_button.grid(row=1, column=2, padx=5, pady=20, ipadx=3, ipady=3)

# ウィンドウのループ処理
root.mainloop()