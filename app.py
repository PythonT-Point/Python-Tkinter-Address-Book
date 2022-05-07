# Import Module
from tkinter import *
import tkinter
  
# Create Object
ws = Tk()
  
# Set geometry
ws.geometry('600x500')
  
# Information List
datalist = []
  
# Add Information
def addinfo():
    global datalist
    datalist.append([PersonName.get(),phoneNumber.get(),personaladdress.get(1.0, "end-1c")])
    updatebookinfo()
  
# View Information
def viewinfo():
    PersonName.set(datalist[int(select.curselection()[0])][0])
    phoneNumber.set(datalist[int(select.curselection()[0])][1])
    personaladdress.delete(1.0,"end")
    personaladdress.insert(1.0, datalist[int(select.curselection()[0])][2])
  
# Delete Information
def deleteinfo():
    del datalist[int(select.curselection()[0])]
    updatebookinfo()
  
def resetinfo():
    PersonName.set('')
    phoneNumber.set('')
    personaladdress.delete(1.0,"end")
  
# Update Information
def updatebookinfo():
    select.delete(0,END)
    for n,p,a in datalist:
        select.insert(END, n)
  
# Add Buttons, Label, ListBox
PersonName = StringVar()
phoneNumber = StringVar()
  
frame = Frame()
frame.pack(pady=10)
  
frame1 = Frame()
frame1.pack()
  
frame2 = Frame()
frame2.pack(pady=10)
  
Label(frame, text = 'PersonName', font='arial 14 bold').pack(side=LEFT)
Entry(frame, textvariable = PersonName,width=50).pack()
  
Label(frame1, text = 'Phone No.', font='arial 14 bold').pack(side=LEFT)
Entry(frame1, textvariable = phoneNumber,width=50).pack()
  
Label(frame2, text = 'Address', font='arial 14 bold').pack(side=LEFT)
personaladdress = Text(frame2,width=37,height=10)
personaladdress.pack()
  
Button(ws,text="Add",font="arial 14 bold",command=addinfo).place(x= 102, y=272)
Button(ws,text="View",font="arial 14 bold",command=viewinfo).place(x= 102, y=312)
Button(ws,text="Delete",font="arial 14 bold",command=deleteinfo).place(x= 102, y=352)
Button(ws,text="Reset",font="arial 14 bold",command=resetinfo).place(x= 102, y=392)
  
scrollbar = Scrollbar(ws, orient=VERTICAL)
select = Listbox(ws, yscrollcommand=scrollbar.set, height=14)
scrollbar.config (command=select.yview)
scrollbar.pack(side=RIGHT, fill=Y)
select.place(x=200,y=260)
  
# Execute Tkinter
ws.mainloop()