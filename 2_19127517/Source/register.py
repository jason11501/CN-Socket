from tkinter import *
import os
def delete2():
    screen3.destroy()
def delete3():
    screen4.destroy()
def delete4():
    screen5.destroy()
def signUp_user():
    username_info=username.get()
    password_info=password.get()

    strToFind=username_info+' '+password_info
    with open('/Users/jsn/Desktop/usernames.txt') as existedNicknames:
    
        if strToFind in existedNicknames.read():#
            Label(screen1,text="[DA TON TAI] tai khoan",fg="red",font=("Calibri",11)).pack()#
            username_info=username.get()#
            password_info=password.get()#
        else:#
            file=open('/Users/jsn/Desktop/usernames.txt','a')#username_info+".txt","w")
            file.write(username_info+' '+password_info+'\n')
            file.close()
        
            username_entry.delete(0,END)
            password_entry.delete(0,END)
    
            Label(screen1,text="[THANH CONG] da dang ki",fg="green",font=("Calibri",11)).pack()
def signUp():
    global screen1
    screen1=Toplevel(screen)
    screen1.title("Dang ki")
    screen1.geometry("300x250")
    
    global username,password,username_entry,password_entry
    username=StringVar()
    password=StringVar()
    
    Label(screen1,text="Tai khoan ").pack()
    Label(screen1,text="").pack()

    Label(screen1,text="username ").pack()
    username_entry = Entry(screen1,textvariable=username)
    username_entry.pack()

    Label(screen1,text="pass ").pack()
    password_entry = Entry(screen1,textvariable=password)
    password_entry.pack()
    Label(screen1,text="").pack()
    Button(screen1,text="Dang ki",width=10,height=1,command=signUp_user).pack()
def dangNhapThanhCong():
    global screen3
    screen3=Toplevel(screen)
    screen3.title("[THANH CONG]")
    screen3.geometry("150x100")
    Label(screen3,text="[THANH CONG] dang nhap",fg="green").pack()
    Button(screen3,text="OK",command=delete2).pack()
def saiPass():
    global screen4
    screen4=Toplevel(screen)
    screen4.title("[THANH CONG]")
    screen4.geometry("150x100")
    Label(screen4,text="[SAI] pass").pack()
    Button(screen4,text="OK",command=delete3).pack()
def usrKoTonTai():
    global screen5
    screen5=Toplevel(screen)
    screen5.title("THAT BAI")
    screen5.geometry("150x100")
    Label(screen5,text="[KHONG TON TAI] tai khoan nay",fg="red").pack()
    Button(screen5,text="OK",command=delete4).pack()
def login_verify():
    usr1=username_verify.get()
    p1=password_verify.get()
    username_entry1.delete(0,END)
    password_entry1.delete(0,END)

    # strToFind=username_info+' '+password_info
    # with open('/Users/jsn/Desktop/usernames.txt') as existedNicknames:
    
    #     if strToFind in existedNicknames.read():#
    #         Label(screen1,text="[DA TON TAI] tai khoan",fg="red",font=("Calibri",11)).pack()#
    #         username_info=username.get()#
    #         password_info=password.get()#
    #     else:#
    #         file=open('/Users/jsn/Desktop/usernames.txt','a')#username_info+".txt","w")
    #         file.write(username_info+' '+password_info+'\n')
    #         file.close()
        
    #         username_entry.delete(0,END)
    #         password_entry.delete(0,END)
    
    #         Label(screen1,text="[THANH CONG] da dang ki",fg="green",font=("Calibri",11)).pack()
    strToFind=usr1+' '+p1
    with open('/Users/jsn/Desktop/usernames.txt') as existedNicknames:
        if strToFind in existedNicknames.read():
            dangNhapThanhCong()
                # print('[THANH CONG] dang nhap')
        else:
            usrKoTonTai()
            # print('ten dang nhap ko ton tai trong database, vui long dki')
def logIn():
    global screen2
    screen2=Toplevel(screen)
    screen2.title("Dang nhap")
    screen2.geometry("300x250")
    Label(screen2,text="Dien thong tin dang nhap").pack()
    Label(screen2,text="").pack()

    global username_verify,password_verify,username_entry1,password_entry1
    username_verify=StringVar()
    password_verify=StringVar()

    Label(screen2,text="username ").pack()
    username_entry1 = Entry(screen2,textvariable=username_verify)
    username_entry1.pack()
    Label(screen2,text="").pack()
    Label(screen2,text="pass").pack()
    password_entry1 = Entry(screen2,textvariable=password_verify)
    password_entry1.pack()
    Label(screen2,text="").pack()
    Button(screen2,text="Dang nhap",width=10,height=1,command=login_verify).pack()
def mainScreen():
    global screen
    screen=Tk()
    screen.geometry("300x250")
    screen.title("")
    Label(text="quan li tai khoan", bg="grey",width=300,font=("Calibri",13)).pack()
    Label(text="").pack()
    Button(text="dang nhap",height="2",width="30",command=logIn).pack()
    Label(text="").pack()
    Button(text="dang ki",height="2",width="30",command=signUp).pack()
    Label(text="").pack()
    Button(text="thoat",height="2",width="30",command=exit).pack()
    screen.mainloop()
mainScreen()
