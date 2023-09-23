from tkinter import *
import tkinter.messagebox as msg

class multiple():
    def __init__(self,root):
        self.root=root
        self.root.geometry('400x400')
        self.root.title('library management system')
        self.root.config(bg='powderblue')

        title = Label(self.root,text='Home page',bg='powderblue',font=('bold','20'))
        title.pack()

        admin_button = Button(self.root,text='Admin',command=self.admin_page)
        admin_button.place(x=150,y=90)
        user_button = Button(self.root,text='user',command=self.user_page)
        user_button.place(x=150,y=150)


    def admin_page(self):
        window = Tk()
        window.title('admin page')
        window.geometry('300x300')
        window.config(bg='powderblue')

        book_name_label = Label(window,text='book name:',bg='powderblue')
        book_name_label.place(x=20,y=40)
        book_author_label = Label(window,text='author name:',bg='powderblue')
        book_author_label.place(x=20,y=80)
        book_quantity_label = Label(window,text='quantity:',bg='powderblue')
        book_quantity_label.place(x=20,y=120)

        self.name_entry = Entry(window)
        self.name_entry.place(x=140,y=40)
        self.author_entry = Entry(window)
        self.author_entry.place(x=140,y=80)
        self.qty_entry = Entry(window)
        self.qty_entry.place(x=140,y=120)

        admit_submit = Button(window,text='submit',bg='lightgrey',command=self.admin_data)
        admit_submit.place(x=100,y=170)


    def user_page(self):
        window1 = Tk()
        window1.title('user page')
        window1.geometry("300x300")
        window1.config(bg="powderblue")

        book_name_label = Label(window1,text='book name:',bg='powderblue')
        book_name_label.place(x=20,y=60)
        author_label= Label(window1,text='author name:',bg='powderblue')
        author_label.place(x=20,y=100)

        self.book_entry = Entry(window1)
        self.book_entry.place(x=100,y=60)
        self.author_entry = Entry(window1)
        self.author_entry.place(x=100,y=100)

        user_submit = Button(window1,text='submit',bg='lightgrey',command=self.user_data)
        user_submit.place(x=100,y=150)
    def admin_data(self):
        import mysql.connector
        mydb= mysql.connector.connect(host='localhost',port=3306,user='root',password='soudhi',database='library_management')
        mycursor= mydb.cursor()

        book_name = self.name_entry.get()
        author_name = self.author_entry.get()
        quantity = self.qty_entry.get()

        mycursor.execute("insert into admin values(%s,%s,%s)",(book_name,author_name,quantity))
        mydb.commit()
        msg.showinfo("admin books", "book add to stock")

    def user_data(self):
        import mysql.connector
        mydb = mysql.connector.connect(host='localhost',port=3306,user='root',password='soudhi',database='library_management')
        mycursor = mydb.cursor()

        book_name = self.book_entry.get()
        author_name = self.author_entry.get()

        mycursor.execute("select quantity from admin where book_name=%s and book_author=%s",(book_name,author_name))

        q=0
        for i in mycursor:
            q=int(i[0])
        if q>=1:
            q=q-1
            mycursor.execute("update admin set quantity=%s where book_name=%s and book_author=%s",(q,book_name,author_name))
            mycursor.execute("insert into user values(%s,%s)",(book_name,author_name))
            mydb.commit()
            msg.showinfo("book availability","book available")

        else:
            msg.showerror("book availability","book not found")


root = Tk()
obj = multiple(root)
root.mainloop()