from tkinter import *
from tkinter import ttk # theme of tk
from tkinter import messagebox

GUI=Tk()
GUI.title('Program')
GUI.geometry('500x400')

def Button2():
    text='ตอนนี้มีเงิน300'
    messagebox.showinfo('เงินในบัญชี',text)#showerror showwarning

def Button3():
    text='เงินในบัญชีเหลือน้อย'
    messagebox.showwarning('เงินในบัญชี',text)#showerror showwarning

def Button4():
    text='เงินหมดบัญชี'
    messagebox.showerror('เงินในบัญชี',text)#showerror showwarning
    
L1=Label(GUI,text='โปรแกรมเด้อ',font=('Angsana New',30),fg='green')
L1.place(x=30,y=30)


FB1=Frame(GUI)#กระดาน
#FB1=LabelFrame(GUI,text='Money')
FB1.place(x=100,y=150)

B1=ttk.Button(FB1,text='เงินเหลือ',command=Button2)#FB1เป็นตัวกำหนดตำแหน่ง
B1.pack(ipadx=20,ipady=20) #บนสุด ขนาด
#B1.place(x=50,y=200)#locate
#B1.pack(ipadx=20,ipady=20,padx=30,pady=30) เพิ่มขนาดกรอบ

FB2=Frame(GUI)
FB2.place(x=100,y=200)
B2=ttk.Button(FB2,text='เงินใกล้หมดละนะ',command=Button3)
B2.pack(ipadx=20,ipady=20)

FB3=Frame(GUI)
FB3.place(x=100,y=250)
B3=ttk.Button(FB2,text='เงินเบิ้ดแหล่ว',command=Button4)
B3.pack(ipadx=20,ipady=20)
GUI.mainloop()
