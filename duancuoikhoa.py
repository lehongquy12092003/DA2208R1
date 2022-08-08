from tkinter import *
from random import randint
## et1.get() là người và et2 là computer

sc = Tk()
sc.title("Lê Hồng Quý - PYF2204R2")
sc.configure(bg="darkslateblue") ## màu nền cho cửa sổ

noidung_et2 = StringVar()
noidung_et1 = StringVar()

def click1():
    noidung_et1.set("Bao")
def click2():
    noidung_et1.set("Búa")
def click3():
    noidung_et1.set("Kéo")

def play():
    random = randint(0,2)
    if random == 0:
        noidung_et2.set("Búa")
    elif random == 1:
        noidung_et2.set("Bao")
    elif random == 2:
        noidung_et2.set("Kéo")
    if noidung_et1.get()== noidung_et2.get():
        lb_thongbao.config(text = "Bạn với máy hòa nhau",fg="orange")
    else: 
        if noidung_et1.get()=="Bao":
            if noidung_et2.get()=="Búa":
                lb_thongbao.config(text = "Bạn thắng :))",fg = "green")
            else:
                lb_thongbao.config(text = "Bạn đã thua, hãy thử lại nhé :<<",fg = "red")
    
        elif noidung_et1.get()=="Búa":
            if noidung_et2.get()=="Kéo":
                lb_thongbao.config(text = "Bạn thắng :))",fg = "green")
            else:
                lb_thongbao.config(text = "Bạn đã thua, hãy thử lại nhé :<<",fg = "red")
    
        elif noidung_et1.get()=="Kéo":
            if noidung_et2.get()=="Bao":
                lb_thongbao.config(text = "Bạn thắng :))",fg = "green")
            else:
                lb_thongbao.config(text = "Bạn đã thua, hãy thử lại nhé :<<",fg = "red")
    
lb1 = Label(sc, text = "GAME KÉO BÚA BAO VỚI MÁY", fg = "darkorange", bg = "sky blue", font=("Arial",40,"bold"))
lb2 = Label(sc, text = "Player :", fg = "springgreen", bg = "sienna", font = ("Arial",30))
lb3 = Label(sc, text = "Computer :", fg = "tomato",bg = "springgreen",font = ("Arial",30))
lb4 = Label(sc, text = "Bạn hãy click vào 1 trong 3 lựa chọn bên trái nhé :]]",fg = "fuchsia",bg = "bisque",font = ("Arial",20))

lb_thongbao = Label(sc, text = "",bg = "darkslateblue",font = ("Arial",30))

bt1 = Button(sc, text = "Bao",fg = "goldenrod",bg = "dimgrey",font = ("Arial",15,"bold"),relief = "groove",command = click1)
bt2 = Button(sc, text = "Búa",fg = "crimson",bg="yellow",font = ("Arial",15,"bold"),relief = "groove",command=click2)
bt3 = Button(sc,text = "Kéo",fg="lemonchiffon",bg="darkslategrey",font = ("Arial",15,"bold"),relief="groove",command=click3)

et1 = Entry(sc,font=("Arial",30),width=5,textvariable = noidung_et1)
et2 = Entry(sc,font = ("Arial",30),width=5,textvariable = noidung_et2)

bt = Button(sc,text = "Play",bg="pink",font = ("Arial",25,"bold"),relief = "groove",command=play)

lb1.grid(column = 1, row = 1, columnspan = 2, pady=(10,20), padx=(100,100)) ##pady là trên xuống
lb2.grid(column = 1, row = 3,pady = (40,25),padx=(0,40))
lb3.grid(column = 1, row = 5,pady = (40,25),padx=(30,0))

et1.grid(column = 2, row = 3,pady = (40,25),padx=(10,300))
et2.grid(column = 2, row = 5,pady = (40,25),padx=(0,300))

bt1.grid(column=1,row=2,columnspan = 2,padx=(400,0))
bt2.grid(column=1,row=3,columnspan = 2,padx=(400,0))
bt3.grid(column=1,row=4,columnspan = 2,padx=(400,0))

bt.grid(column = 2,row = 6,padx=(0,300))

lb_thongbao.grid(column = 1, row = 7,columnspan=2,pady=(25,25),padx=(60,0))

sc.mainloop()
