from tkinter import *
from  tkinter.ttk import *
from tkinter.colorchooser import *
import  tkinter 
import threading
from tkinter import scrolledtext
from os import path
from tkinter import filedialog
from tkinter import messagebox
import random
import sys
import math
from docx import Document
import hashlib

def SNT(snt):
    if(snt <2):
        return False
    for i in range(2,int(math.sqrt(snt))):
        if(snt % i == 0):
            return False
    return True
## kiểm tra số nguyên tố
def GCD(a,b):
    temp=0
    while(b!=0):
        temp = a%b
        a=b
        b=temp
    
    if(a==1):
        return True
    else:
        return False
## kiểm tra ước chúng của 2 số có bằng 1 hay không
def PowModulo(cs,sm,modulo):
    binarycs = bin(sm) ## chuyển mũ về nhị phân
    binarycs = binarycs[2:None]
    reusult =1 ## khởi tạo kết quả là 1
    for i in binarycs: ## hàm for chạy trong xâu chứa nhị phân của mũ
        reusult = (reusult*reusult)% modulo
        if(i=="1"):
            reusult = (reusult*cs) % modulo ## khi hệ số nhị phân là 1 sẽ nhân result với cơ số và modulo
    return reusult
##
def ModuloNghichDao(a,p):
    #sư dụng thuật toán ơ colit mở rộng
    #khởi tạo
    k=p
    r=0
    y1=1
    y0=0
    y=0
    q=0
    while(a != 0):
        r=p%a
        if(r==0):
            break
        q=(p//a)
        y=(y0-y1*q)
        p=(a)
        a=r
        y0=y1
        y1=y
    if(y<0):
        return y+k
    else:
        return y
def ktrauocP(p,b):
    if((p-1)%b==0):
        return True
    else:
        return False
# kiem tra uoc cua x thuoc (2..p-2)
def kqtao(t,p,b):
     soMu = p-1//b
     kq = PowModulo(t,soMu,p)
     if(kq==1): return False
     else: return True
# ktra so dc sinh
##
def taokhoa():
    global p,q,n,phi,e,d
    while True:
        p = random.randint(1, 1000)
        if(SNT(p)):
            break
    #chon so q  thoa man q la uoc cua p-1
    while True:
        q = random.randint(1,p-1)
        if(SNT(q) and ktrauocP(p,q)):
            break
    #tim so g_a de tim so g(la phan tu sinh)
    n = p*q
    phi = (q-1)*(p-1)
    while True:
        e = random.randint(1,phi-1)
        if(GCD(e,phi)):
            break
   
    d= ModuloNghichDao(e,phi)
   
    string1.insert(0, str(p))
    string2.insert(0, str(q))
    string3.insert(0,str(n))
    string4.insert(0, str(e))
    string5.insert(0,str(d))
    return
##
def reset():
    string1.delete(0,sys.getsizeof(string1))
    string2.delete(0,sys.getsizeof(string2))
    string3.delete(0,sys.getsizeof(string3))
    string4.delete(0,sys.getsizeof(string4))
    string5.delete(0,sys.getsizeof(string5))
    string7.delete(0,sys.getsizeof(string7))
    txt.delete('1.0', END)
    string8.delete(0,END)
##
def checkfile2():
    string8.delete(0,END)
    dir2 = filedialog.askopenfilename()
    string8.insert(0,dir2)
##
def checkfile1():
    string7.delete(0,END)
    dir = filedialog.askopenfilename()
    string7.insert(0,dir)
##
def kyso():
    dir = string7.get()
    if(dir ==""):
        messagebox.showerror("Thông báo","Bạn cần nhập đường dẫn đến file cần ký")
    if(string1.get()==""):
         messagebox.showerror("Thông báo","Bạn cần tạo khóa trước khi  ký")
    filesave=open("fileMh.txt",mode="w",encoding="utf8")
    fileOpen= open(dir,mode="r+", encoding="latin-1")
    stringText_ = fileOpen.read()
    hashencode = hashlib.sha256(bytes(stringText_,encoding="utf8")).hexdigest()
    fileOpen.close()
    stringHash=""
    for i in hashencode: #cần sửa
        xm =  PowModulo(ord(i),e,n)
        stringHash+=chr(xm)
    filesave.write(stringHash)
    filesave.write(stringText_)
    filesave.close()
    txt.insert(tkinter.INSERT,stringHash)
    messagebox.showinfo("Thông báo","Văn bản đã được ký")
##
def checkhash(text,hash): ##cần sửa
    hash_tex11t = hashlib.sha256(bytes(text,encoding="utf8")).hexdigest()
    hashab = hash
    a=0
    b=0
    for i in range(0,len(hash_tex11t)):
       a = PowModulo(ord(hashab[i]),d,n)
       if(a!=ord(hash_tex11t[i])):
            return False

    return True

##
def kiemtratext():
    dir2 = string8.get()
    if(dir2 ==""):
        messagebox.showerror("Thông báo","Bạn cần nhập đường dẫn đến file cần kiểm tra chữ ký")
    fileOpen=open(dir2,mode="r+", encoding="latin-1")
    stringText_ = fileOpen.read()
    fileOpen.close()
    fileOpen2=open("fileMh.txt",mode="r", encoding="utf8")
    stringhash_ = fileOpen2.read(64)
    stringtext =fileOpen2.read()
    if( checkhash(stringText_,stringhash_)):
         messagebox.showinfo("Thông báo","Văn bản không bị chỉnh sửa gì")
    else:
        messagebox.showerror("Thông báo","Văn bản đã bị chỉnh sửa")
    fileOpen2.close()

win = Tk()
win.title("Chữ Ký Số RSA")
win.iconbitmap("ico.ico")
win.geometry("1200x600+500+400")
bg = PhotoImage(file="./nenchinh.png")
win.resizable(width = FALSE,height = FALSE)

control_tab = Notebook(win)

tab1 = tkinter.Frame(control_tab)

tab2 =Frame(control_tab)

tab3 = Frame(control_tab)

control_tab.add(tab1,text="Chữ ký số RSA")

control_tab.add(tab2,text="Thông tin tác giả")

control_tab.add(tab3,text="Hướng dẫn sử dụng")
###
f_big = tkinter.Frame(tab1,bg="#80aaff")
lb1 = tkinter.Label(f_big , text = "tạo khóa",bg="#80aaff",fg='red',font="10")
lb1.place(width = 80,height = 50,x = 0,y = 0)
f_son1 = tkinter.Frame(f_big,bg = '#d9d9d9')
tkinter.Label(f_son1,text= "khóa công khai(n,e)",bg = '#d9d9d9',fg='#000000',font= "10").place(height = 20,width =150,x = 0,y = 10)
tkinter.Label(f_son1,text= "số nguyên tố p = ",bg = '#d9d9d9',fg='#000000',font= "5").place(height = 20,width =150,x=101,y=60)
string1 = Entry(f_son1)
string1.place(height = 20,width =150,x=250,y=60)
tkinter.Label(f_son1,text= "số nguyên tố q = ",bg = '#d9d9d9',fg='#000000',font= "5").place(height = 20,width =150,x=110,y=90)
string2 = Entry(f_son1)
string2.place(height = 20,width =150,x=250,y=90)

tkinter.Label(f_son1,text= "n = ",bg = '#d9d9d9',fg='#000000',font= "5").place(height = 20,width =150,x=85,y=120)
string3 = Entry(f_son1)
string3.place(height = 20,width =150,x=250,y=120)
tkinter.Label(f_son1,text= "e = ",bg = '#d9d9d9',fg='#000000',font= "5").place(height = 20,width =150,x=85,y=150)
string4 = Entry(f_son1)
string4.place(height = 20,width =150,x=250,y=150)

f_son1.place(width = 500,height =260,x=50,y=40)

f_son2 = tkinter.Frame(f_big,bg = '#d9d9d9')
tkinter.Label(f_son2,text= "khóa bí mật (d)",bg = '#d9d9d9',fg='#000000',font ="10").place(height = 20,width =150,x = 0,y = 10)
tkinter.Label(f_son2,text= "số nguyên d = ",bg = '#d9d9d9',fg='#000000',font= "5").place(height = 20,width =150,x=110,y=50)
string5 = Entry(f_son2)
string5.place(height = 20,width =150,x=250,y=50)
f_son2.place(width = 500,height =100,x=50,y=310)
tkinter.Button(f_big,text = "tạo khóa ngẫu nhiên",bg = '#d9d9d9',fg='#000000',command = taokhoa).place(height = 30,width =150,x=180,y=430)
f_big.place(width = 500,height = 800,x = 0,y = 0)
##
f_big2 = tkinter.Frame(tab1,bg='#80aaff')
tkinter.Label(f_big2,text = "Thực hiện ký",fg='red',font="10",bg='#80aaff').place(width = 100,height = 20,x=0,y=20)
tkinter.Button(f_big2,text = "chọn lại",bg = '#d9d9d9',fg='#000000',command=reset).place(width = 120,height = 20,x=500,y=50)
tkinter.Label(f_big2,text = "Chọn file thực hiện ký: ",bg = '#d9d9d9',fg='#000000').place(width = 120,height = 20,x=20,y=90)
string7 =  tkinter.Entry(f_big2)
string7.place(width = 420,height = 20,x=30,y=120)
photo =PhotoImage(file= r'file.png')
tkinter.Button(f_big2,image =photo, command = checkfile1).place(width = 30,height = 20,x=450,y=120)
tkinter.Button(f_big2,text="ký lên văn bản",command=kyso).place(width = 100,height = 20,x=530,y=120)
tkinter.Label(f_big2,text = " tệp chữ ký file văn bản đã được gửi đi ",bg = '#d9d9d9',fg='#000000').place(width = 220,height = 20,x=20,y=150)
txt  = tkinter.scrolledtext.ScrolledText(f_big2,height = 300,width=600,fg = 'red')
txt.place(width = 600,height = 300,x=30,y=170)
tkinter.Label(f_big2,text = "chọn file thực hiện kiểm tra chữ ký số:",bg = '#d9d9d9',fg='#000000').place(width = 220,height = 20,x=20,y=490)
string8 = tkinter.Entry(f_big2)
string8.place(width = 420,height = 20,x=30,y=510)
tkinter.Button(f_big2,image =photo, command = checkfile2).place(width = 30,height = 20,x=450,y=510)
tkinter.Button(f_big2,text=" kiểm tra văn bản ký",command=kiemtratext).place(width = 120,height = 20,x=530,y=510)
f_big2.place(width = 700,height = 800,x = 500,y = 0)
##
##
finfor_ = tkinter.Frame(tab2,bg="#80aaff")
tkinter.Label(finfor_,background="#80aaff",text="Thông tin tác giả: ", font=30).place(height=50,width=120,x=10,y=5)
tkinter.Label(finfor_,background="#80aaff",text="Bài tập lớn môn: AN TOÀN BẢO MẬT THÔNG TIN", font=10).place(height=50,width=500,x=80,y=40)
tkinter.Label(finfor_,background="#80aaff",text="Đề tài: Tìm hiểu về chữ ký điện tử RSA và ứng dụng minh họa", font=20).place(height=50,width=500,x=130,y=120)
tkinter.Label(finfor_,background="#80aaff",text="Nhóm 4", font=10).place(height=50,width=500,x=-60,y=160)
tkinter.Label(finfor_,background="#80aaff",text="Thành viên:  ", font=10).place(height=50,width=500,x=-50,y=200)
tkinter.Label(finfor_,background="#80aaff",text="Phạm Xuân Đức - 2019605697", font=10).place(height=50,width=500,x=15,y=250)
finfor_.place(width= 1200, height=800,x=0,y=0)
##
fguide_ = tkinter.Frame(tab3,bg="#80aaff")
tkinter.Label(fguide_,background="#80aaff",text="Hướng dẫn sử dụng:", font=30).place(height=50,width=300,x=10,y=5)
tkinter.Label(fguide_,background="#80aaff",text="- Đầu tiên bạn hãy ấn \"Tạo khóa ngẫu nhiên\" để tạo khóa(Đợi 2-5p). Để thực hiện tạo khóa", font=10).place(height=50,width=1000,x=-47,y=40)
tkinter.Label(fguide_,background="#80aaff",text="- Sau khi đã tạo khóa ngẫu nhiên hãy chọn file để ký", font=10).place(height=50,width=500,x=70,y=80)
tkinter.Label(fguide_,background="#80aaff",text="- Sau khi đã chọn file để ký, bạn hãy ấn ký lên văn bản để thực hiện ký", font=20).place(height=50,width=500,x=130,y=120)
tkinter.Label(fguide_,background="#80aaff",text="- Sau đó hãy thực hiện lưu file đã ký vào máy", font=10).place(height=50,width=500,x=44,y=160)
tkinter.Label(fguide_,background="#80aaff",text="- Để kiểm tra chữ ký hãy ấn chọn file ký vừa lưu vào máy (khi kiểm tra file .docx cần tắt word trước khi kiểm tra)", font=10).place(height=50,width=1000,x=16,y=200)
tkinter.Label(fguide_,background="#80aaff",text="- Rồi ấn kiểm tra chữ ký để kiểm tra", font=10).place(height=50,width=500,x=16,y=240)

fguide_.place(width= 1200, height=800,x=0,y=0)
control_tab.pack(fill = 'both',expand =1)
win.mainloop()