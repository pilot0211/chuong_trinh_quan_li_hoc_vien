import tkinter
from tkinter import ttk
from tkinter import scrolledtext
from chucnanghocvien import *
from lophoc import *
from tktooltip import ToolTip
giao_dien = tkinter.Tk()
giao_dien.title("Quản lý học viên - Python")
giao_dien.geometry('800x800')
font = ("Comic Sans MS",18)
#label
Font_tuple = ("Comic Sans MS", 20, "bold")
label = tkinter.Label(giao_dien,text="CHƯƠNG TRÌNH QUẢN LÝ HỌC VIÊN" ,fg='black',font=Font_tuple)
label.place(relx = 0.5, rely = 0.05, anchor = 'center')

label1 = tkinter.Label(giao_dien,text="Name" ,fg='black',font=font)
label1.place(relx = 0.05, rely = 0.07)

label2 = tkinter.Label(giao_dien,text="Age" ,fg='black',font=font)
label2.place(relx = 0.05, rely = 0.12)

label3 = tkinter.Label(giao_dien,text="Address" ,fg='black',font=font)
label3.place(relx = 0.05, rely = 0.17)

label4 = tkinter.Label(giao_dien,text="Sex" ,fg='black',font=font)
label4.place(relx = 0.05, rely = 0.22)

label5 = tkinter.Label(giao_dien,text="Information" ,fg='black',font=font)
label5.place(relx = 0.05, rely = 0.27)

label6 = tkinter.Label(giao_dien,text="Grade_English" ,fg='black',font=font)
label6.place(relx = 0.05, rely = 0.32)

#text box
name = tkinter.StringVar()
text_box1 = tkinter.Entry(giao_dien,width= 50,textvariable=name)
text_box1.place(relx = 0.5, rely = 0.1, anchor = 'center')

age = tkinter.IntVar()
text_box2 = tkinter.Entry(giao_dien,width= 50,textvariable=age)
text_box2.place(relx = 0.5, rely = 0.15, anchor = 'center')

address = tkinter.StringVar()
text_box3 = tkinter.Entry(giao_dien,width= 50,textvariable=address)
text_box3.place(relx = 0.5, rely = 0.2, anchor = 'center')

sex = tkinter.StringVar()
text_box4 = ttk.Combobox(giao_dien,width =47,textvariable=sex)
text_box4['values']=('Male','Female','Unknown')
text_box4.place(relx = 0.5, rely = 0.25, anchor = 'center')

infor = tkinter.IntVar()
text_box5 = tkinter.Entry(giao_dien,width= 50,textvariable=infor)
text_box5.place(relx = 0.5, rely = 0.3, anchor = 'center')

english = tkinter.IntVar()
text_box6 = tkinter.Entry(giao_dien,width= 50,textvariable=english)
text_box6.place(relx = 0.5, rely = 0.35, anchor = 'center')

text_area = scrolledtext.ScrolledText(giao_dien, 
                                      width = 30, 
                                      height = 8, 
                                      font = ("Times New Roman",
                                              15))
text_area.configure(state='disabled')
text_area.place(relx = 0.5, rely = 0.65, anchor = 'center')

font_tb7 = ("Comic Sans MS", 15, "bold")
tb7 = tkinter.StringVar()
text_box7 = tkinter.Entry(giao_dien, width = 15,bg='#dcdcdc', relief='flat',font=font_tb7,textvariable=tb7)
text_box7.place(relx = 0.5, rely = 0.85, anchor = 'center')
text_box7.configure(state='disabled')

tb8 = tkinter.StringVar()
text_box8 = tkinter.Entry(giao_dien, width = 18,bg='#dcdcdc', relief='flat',font=font_tb7,textvariable=tb8)
text_box8.place(relx = 0.5, rely = 0.5, anchor = 'center')
text_box8.configure(state='disabled')


id = tkinter.StringVar()
text_box9 = tkinter.Entry(giao_dien,width= 20,textvariable=id)
text_box9.place(relx = 0.05, rely = 0.47)

#def
def check():
    if(lophoc.getConnection != None):
        tb7.set('Connect Successful')

def show():
    data.execute("SELECT * FROM Quan_ly_hoc_vien.Hocvien")
    ketqua = data.fetchall()
    text_area.configure(state='normal')
    text_area.delete('1.0', 'end')
    for i in ketqua:
        ketqua = str(i)+', '
        text_area.configure(state='normal')
        text_area.insert(tkinter.INSERT,ketqua+"\n")
        text_area.configure(state='disabled')
    tb7.set(' ')
    return ketqua
    
def add():
    try:
        if(sex.get() == 'Male') or (sex.get() == 'Female') or (sex.get()=='Unknown'):
            sql = "INSERT INTO `Hocvien`(`Name`,Age,Country, English,Information,Sex)VALUES (%s,%s,%s,%s,%s,%s)"
            data.execute(sql,(name.get(),age.get(),address.get(),infor.get(),english.get(),sex.get(),))
            ketnoi.commit()
            tb8.set('Add Successful')
            show()
        else:
            tb8.set('Add Unsuccessful')
        name.set(' ')
        age.set(' ')
        address.set(' ')
        infor.set(' ')
        english.set(' ')
        sex.set(' ')
        tb7.set(' ')
    except:
        tb8.set('Add Unsuccessful')
        name.set(' ')
        age.set(' ')
        address.set(' ')
        infor.set(' ')
        english.set(' ')
        sex.set(' ')
        tb7.set(' ')

def delete():
    try:
        if (id.get() != ' '):
            sql = "DELETE FROM Quan_ly_hoc_vien.Hocvien WHERE Id = %s"
            data.execute(sql,(int(id.get()),))
            ketnoi.commit()
            id.set(' ')
            tb8.set('Delete Successful')
            tb7.set(' ')
            show()
        else:
            tb8.set('Delete Unsuccessful')
            tb7.set(' ')
    except:
        tb8.set('Delete Unsuccessful')
        tb7.set(' ')

def update():
    try: 
        if(id.get() !=' '):
            s = id.get().split(',')
            sql = "UPDATE Quan_ly_hoc_vien.Hocvien SET Name = %s WHERE Id = %s"
            data.execute(sql,(s[1].capitalize(),int(s[0]),))
            tb8.set('Update Successful')
            show()
        else:
            tb8.set('Update Unsuccessful')
        id.set(' ')
    except:
        tb8.set('Update Unsuccessful')
        id.set(' ')
    

#button
button1 = tkinter.Button(giao_dien,text='Thêm học viên',activebackground='#dcdcdc',width=15,command=add)
button1.place(relx = 0.05, rely = 0.37)

button2 = tkinter.Button(giao_dien,text='Xóa học viên',activebackground='#dcdcdc',width=15,command=delete)
button2.place(relx = 0.05, rely = 0.42)
ToolTip(button2, msg="nhập id để xóa", follow=True)

button3 = tkinter.Button(giao_dien,text='Hiển thị học viên',activebackground='#dcdcdc',width=15,command=show)
button3.place(relx = 0.5, rely = 0.4, anchor = 'center')

button4 = tkinter.Button(giao_dien,text='Sửa học viên',activebackground='#dcdcdc',width=15,command=update)
button4.place(relx = 0.5, rely = 0.45, anchor = 'center')
ToolTip(button4, msg="nhập 'id, tên muốn đổi' để sửa", follow=True)

button5 = tkinter.Button(giao_dien,text='Kiểm tra kết nối',activebackground='#dcdcdc',width=15,command=check)
button5.place(relx = 0.5, rely = 0.8, anchor = 'center')






























giao_dien.mainloop()