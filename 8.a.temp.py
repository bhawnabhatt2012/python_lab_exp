from tkinter import *
import sqlite3

conn = sqlite3.connect('phonelist.db')
c = conn.cursor()


root = Tk()

row1 = Frame(root)
label1 = Label(row1,text = 'Name',width=5)
entry1 = Entry(row1)
label1.pack(side = LEFT)
entry1.pack(side = RIGHT,expand = YES, fill = X)
row1.pack(side=TOP,expand=YES,fill=BOTH)


row2 = Frame(root)
label2 = Label(row2,text = 'Phone',width=5)
entry2 = Entry(row2)
label2.pack(side = LEFT)
entry2.pack(side = RIGHT,expand = YES,fill = X)
row2.pack(side = TOP, expand = YES, fill = BOTH)

row4 = Frame(root)
sbar = Scrollbar(row4)
listbox1 = Listbox(row4,relief = SUNKEN)
sbar.config(command = listbox1.yview)
sbar.pack(side = RIGHT,fill = Y)
listbox1.pack(side = LEFT,expand = YES,fill = BOTH)
row4.pack(side = TOP,expand = YES,fill=BOTH)

def add():
    name_value = entry1.get()
    phone_value = entry2.get()
    c.execute("INSERT INTO PHONELIST VALUES(?,?);",(phone_value,name_value))
    print('Data added successfully')
    conn.commit()

def update():
    updated_name = entry1.get()
    phone_value = entry2.get()
    c.execute("UPDATE PHONELIST SET NAME = ? WHERE PHONE_NUMBER = ?;",(updated_name,phone_value))
    print('Data updated successfully')
    conn.commit()

def delete():
    phone_value = entry2.get()
    c.execute("DELETE FROM PHONELIST WHERE PHONE_NUMBER = ?",(phone_value,))
    print('Data deleted successfully')
    conn.commit()

def load():
    listbox1.delete(0,END)
    data = c.execute("SELECT * FROM PHONELIST;")
    for row in data:
        value = row[0] + ', ' + row[1]
        listbox1.insert(END,value)

def onselect(evt):
    data = c.execute("SELECT * FROM PHONELIST;")
    namesList = []
    phonesList = []
    for row in data:
        namesList.append(row[1])
        phonesList.append(row[0])

    w = evt.widget
    index = int(w.curselection()[0])
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry1.insert(0, namesList[index])
    entry2.insert(0, phonesList[index])

load()

listbox1.bind('<<ListboxSelect>>',onselect)

row3 = Frame(root)
add_btn = Button(row3,text='Add',command = add)
update_btn = Button(row3,text='Update',command = update)
delete_btn = Button(row3,text='Delete',command = delete)
load_btn = Button(row3,text='Load',command = load)
add_btn.pack(side = LEFT,expand = YES,fill = BOTH)
update_btn.pack(side = LEFT,expand = YES,fill = BOTH)
load_btn.pack(side = RIGHT,expand = YES,fill = BOTH)
delete_btn.pack(side = RIGHT,expand = YES,fill = BOTH)
row3.pack(side = TOP,expand = YES,fill = BOTH)



root.mainloop()
conn.close()







