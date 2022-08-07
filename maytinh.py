from tkinter import *

sc = Tk()
sc.title("Cửa sổ mới")
noidung_et = StringVar()

et = Entry(sc,text="",font=("Arial",20),textvariable=noidung_et)
def nhan1():
    noidung_et.set(noidung_et.get() + "1")
def nhan2():
    noidung_et.set(noidung_et.get() + "2")
def nhan3():
    noidung_et.set(noidung_et.get() + "3")
def nhan4():
    noidung_et.set(noidung_et.get() + "4")
def nhan5():
    noidung_et.set(noidung_et.get() + "5")
def nhan6():
    noidung_et.set(noidung_et.get() + "6")
def nhan7():
    noidung_et.set(noidung_et.get() + "7")
def nhan8():
    noidung_et.set(noidung_et.get() + "8")
def nhan9():
    noidung_et.set(noidung_et.get() + "9")
def nhan0():
    noidung_et.set(noidung_et.get() + "0")
def nhancham():
    noidung_et.set(noidung_et.get() + ".")
def nhanmongoac():
    noidung_et.set(noidung_et.get() + "(")
def nhandongngoac():
    noidung_et.set(noidung_et.get() + ")")
def nhancong():
    noidung_et.set(noidung_et.get() + "+")
def nhantru():
    noidung_et.set(noidung_et.get() + "-")
def nhannhan():
    noidung_et.set(noidung_et.get() + "*")
def nhanchia():
    noidung_et.set(noidung_et.get() + "/")
def nhanbang():
    noidung_et.set(eval(noidung_et.get())) ## hàm eval giúp tính toán
def nhanMR():
    noidung_et.set("")
def nhanDEL():
    noidung_et.set(noidung_et.get()[:-1])
bt1 = Button(sc,text="MR",fg="yellow",bg="grey",width=10,height=2,font=("Arial",12),command=nhanMR)
bt2 = Button(sc,text="DEL",fg="yellow",bg="grey",width=10,height=2,font=("Arial",12),command=nhanDEL)
bt3 = Button(sc,text="(",fg="yellow",bg="grey",width=10,height=2,font=("Arial",12),command=nhanmongoac)
bt4 = Button(sc,text=")",fg="yellow",bg="grey",width=10,height=2,font=("Arial",12),command=nhandongngoac)

bt5 = Button(sc,text="1",fg="yellow",bg="grey",width=10,height=2,font=("Arial",12),command=nhan1)
bt6 = Button(sc,text="2",fg="yellow",bg="grey",width=10,height=2,font=("Arial",12),command=nhan2)
bt7 = Button(sc,text="3",fg="yellow",bg="grey",width=10,height=2,font=("Arial",12),command=nhan3)
bt8 = Button(sc,text="+",fg="yellow",bg="grey",width=10,height=2,font=("Arial",12),command=nhancong)

bt9 = Button(sc,text="4",fg="yellow",bg="grey",width=10,height=2,font=("Arial",12),command=nhan4)
bt10 = Button(sc,text="5",fg="yellow",bg="grey",width=10,height=2,font=("Arial",12),command=nhan5)
bt11 = Button(sc,text="6",fg="yellow",bg="grey",width=10,height=2,font=("Arial",12),command=nhan6)
bt12 = Button(sc,text="-",fg="yellow",bg="grey",width=10,height=2,font=("Arial",12),command=nhantru)

bt13 = Button(sc,text="7",fg="yellow",bg="grey",width=10,height=2,font=("Arial",12),command=nhan7)
bt14 = Button(sc,text="8",fg="yellow",bg="grey",width=10,height=2,font=("Arial",12),command=nhan8)
bt15 = Button(sc,text="9",fg="yellow",bg="grey",width=10,height=2,font=("Arial",12),command=nhan9)
bt16 = Button(sc,text="*",fg="yellow",bg="grey",width=10,height=2,font=("Arial",12),command=nhannhan)

bt17 = Button(sc,text=".",fg="yellow",bg="grey",width=10,height=2,font=("Arial",12),command=nhancham)
bt18 = Button(sc,text="0",fg="yellow",bg="grey",width=10,height=2,font=("Arial",12),command=nhan0)
bt19 = Button(sc,text="=",fg="yellow",bg="grey",width=10,height=2,font=("Arial",12),command=nhanbang)
bt20 = Button(sc,text="/",fg="yellow",bg="grey",width=10,height=2,font=("Arial",12),command=nhanchia)

et.grid(column=1,row=1,sticky = "WE",columnspan=4)

bt1.grid(column=1,row=2)
bt2.grid(column=2,row=2)
bt3.grid(column=3,row=2)
bt4.grid(column=4,row=2)

bt5.grid(column=1,row=3)
bt6.grid(column=2,row=3)
bt7.grid(column=3,row=3)
bt8.grid(column=4,row=3)

bt9.grid(column=1,row=4)
bt10.grid(column=2,row=4)
bt11.grid(column=3,row=4)
bt12.grid(column=4,row=4)

bt13.grid(column=1,row=5)
bt14.grid(column=2,row=5)
bt15.grid(column=3,row=5)
bt16.grid(column=4,row=5)

bt17.grid(column=1,row=6)
bt18.grid(column=2,row=6)
bt19.grid(column=3,row=6)
bt20.grid(column=4,row=6)

sc.mainloop()
