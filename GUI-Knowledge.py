from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox

GUI = Tk() #นี่คือหน้าเจอหลักของโปรแกรม
GUI.title('โปรแกรมบันทึกข้อมูล') #นี่คือชื่อโปรแกรม
GUI.geometry('500x400') #นี่คือขนาดโปรแกรม

L1 = Label(GUI,text='โปรแกรมบันทึกความรู้',font=('Angsana New',30),fg='green')
L1.place(x=50,y=150)

################
def Button2():
    text = 'ตอนนี้มีเงินอยู่ในบัญชีอยู่ 300 บาท'
    messagebox.showinfo('เงินในบัญชี',text)

FB1 = LabelFrame(GUI) #คล้ายกระดาน
FB1.place(x=100,y=200)
B2 = ttk.Button(GUI,text='เงินมีอยู่กี่บาท',command=Button2)
B2.pack(ipadx=20,ipady=20)

#################
def Button3():
    text = 'Python 101,Math'
    messagebox.showinfo('วิชาเรียนวันที่ 10-20 ก.พ.',text)

FB2 = LabelFrame(GUI) #คล้ายกระดาน
FB2.place(x=100,y=300)
B3 = ttk.Button(GUI,text='สัปดาห์นี้เรียนวิชาอะไร',command=Button3)
B3.pack(ipadx=20,ipady=20)
#################
GUI.mainloop()
