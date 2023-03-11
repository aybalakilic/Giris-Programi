from tkinter import *
from user import username,password
from tkinter import messagebox

arayuz=Tk()
arayuz.title("Giriş Ekranı")
arayuz.resizable(False,False)

arayuz.geometry("800x450")

buyuk_frame=Frame(arayuz,height=430,width=780,bg="#47c9af")
buyuk_frame.place(x=10,y=10)

top_frame=Frame(buyuk_frame,height=100,width=680,bg="#b85fd9")
top_frame.place(x=50,y=30)

giris_yazisi=Label(top_frame,text="HOŞGELDİNİZ",font=("Times-20",45,"bold"),bg="#b85fd9",fg="white")
giris_yazisi.place(x=110,y=10)

kullanici_label=Label(buyuk_frame,text="Kullanıcı adınızı giriniz:",font=("Times-20",25,"bold"),bg="#b85fd9",fg="white")
kullanici_label.place(x=50,y=200)

def islem():

    if kullanici_entry.get()==username and sifre_entry.get()==password:

        yeni_ekran=Tk()

        yeni_ekran.geometry("400x400")

        yeni_ekran.title("Ana Sayfa")
        yeni_ekran.resizable(False,False)

        frame =Frame(yeni_ekran,height=780,width=780,bg="#47c9af")
        frame.place(x=10,y=10)

        hosgeldin_yazisi=Label(yeni_ekran,text="İşleminiz Başarıyla\nGerçekleşmiştir",font=("Times-20",20,"bold"),bg="#47c9af",fg="white")
        hosgeldin_yazisi.place(x=80,y=100)

        img=PhotoImage(file="ev.png")
        fotograf=Label(frame,image=img)
        fotograf.place(x=100,y=150)

        
        arayuz.destroy()
        
        yeni_ekran.mainloop()

    elif kullanici_entry.get()==username and sifre_entry.get()!=password:

        mesaj="Şifre hatalı"
        messagebox.showerror("Başarısız!",mesaj)

    elif kullanici_entry.get()!=username and sifre_entry.get()==password:

        mesaj="Kullanıcı adı hatalı"
        messagebox.showerror("Başarısız!",mesaj)

    elif kullanici_entry.get()!=username and sifre_entry.get()!=password:

        mesaj="Kullanıcı adı ve sifre hatalı"
        messagebox.showerror("Başarısız!",mesaj)


kullanici_entry=Entry(buyuk_frame,font=("Times-20",18,"italic"))
kullanici_entry.place(x=440,y=210)

sifre_label=Label(buyuk_frame,text="Şifrenizi giriniz:",font=("Times-20",25,"bold"),bg="#b85fd9",fg="white")
sifre_label.place(x=50,y=250)

sifre_entry=Entry(buyuk_frame,font=("Times-20",18,"italic"))
sifre_entry.place(x=440,y=260)

buton=Button(buyuk_frame,text="Giriş Yap",font=("Times-20",20,"bold"),bg="#b85fd9",fg="white",command=islem)
buton.place(x=330,y=320)

arayuz.mainloop()