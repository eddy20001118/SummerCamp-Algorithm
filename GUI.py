# -*- coding: UTF-8 -*-

from Tkinter import *
import tkMessageBox
import xlrd
root = Tk()
root.title("Button Test")
data = xlrd.open_workbook('map.xlsx')
sheet = data.sheets()[2]
buttonLable = ["A","B","C","D","E","F","G","H"]
bg1 = ""
for i in range(0,8):
    for j in range(0,8):
        text1 = str(sheet.cell(i,j))[7]
        if text1 == "R":
            bg1 = "red"
        elif text1 == "Y":
            bg1 = "yellow"
        elif text1 == "G":
            bg1 = "green"
        elif text1 == "B":
            bg1 = "blue"
        else:
            bg1 = "white"
        Button(root,text=text1,bd=0,bg=bg1,width=2,height=2).grid(row=i,column=j)

Button(root,text="红",bd=0,bg="red",width=2,height=2).grid(row=8,column=0)
Button(root,text="黄",bd=0,bg="yellow",width=2,height=2).grid(row=8,column=1)
Button(root,text="绿",bd=0,bg="green",width=2,height=2).grid(row=8,column=2)
Button(root,text="蓝",bd=0,bg="blue",width=2,height=2).grid(row=8,column=3)
root.mainloop()