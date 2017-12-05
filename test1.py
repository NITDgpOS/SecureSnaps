from tkinter import *

root=Tk()

photo=PhotoImage(file="/home/ankush/Downloads/page/ford-mustang.png")
label=Label(root,image=photo)
label.grid(row=1,column=3)

one=Label(root,text="INPUT IMAGE")
one.grid(row=0,column=0)

two=Label(root,text="OUTPUT IMAGE")
two.grid(row=0,column=3)

photo1=PhotoImage(file="/home/ankush/Downloads/page/super-cars.png")
label1=Label(root,image=photo1)
label1.grid(row=1,column=0)

three=Label(root,text="password")
three.grid(column=1,sticky=E)

entry1=Entry(root)
entry1.grid(row=2,column=2)

button1=Button(text="Choose file",fg="black")
button2=Button(text="Encrypt",fg="black",bg="yellow")
button3=Button(text="Decrypt",fg="black",bg="green")

button1.grid(row=2,column=0)
button3.grid(row=2,column=4)
button2.grid(row=2,column=3)

root.mainloop()