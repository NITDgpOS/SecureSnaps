from Tkinter import *
import tkFileDialog
root=None
img=None
pswd=None
fr2=None
count=0
#def Settings(y):
def addimage():
    global root
    global count
    file=tkFileDialog.askopenfilename(parent=root,title="Choose an image")
    count+=1
    if (count%2 == 1):
        Label(fr2,text=file,bg="blue",fg="white").pack(side=TOP)
    else:
        Label(fr2,text=file,bg="white",fg="blue").pack(side=TOP)
def EnterPswd(x):
    global pswd
    pswd=Entry(x,show="*")
    pswd.pack(side=LEFT)
    print pswd.get()
def main():
    global root
    global img
    global fr2
    root=Tk()
    fr1=Frame(root,bg="cyan",bd=16)
    fr1.pack(side=TOP)
    img=PhotoImage(file="abc.gif")
    Button(fr1,image=img,bd=4,width=80,height=80,bg="indigo",command=addimage).pack(side=LEFT)
    Label(fr1,text="Password :",bg="cyan").pack(side=LEFT)
    EnterPswd(fr1)
    Label(fr1,text="  ",bg="cyan").pack(side=LEFT) 
    Button(fr1,text="Enc",bg="yellow",fg="red",justify=CENTER,width=5,height=2,bd=6).pack(side=LEFT) #need to add command to encode
    Label(fr1,text=" ",bg="cyan").pack(side=LEFT)
    Button(fr1,text="Dec",bg="pink",fg="blue",justify=CENTER,width=5,height=2,bd=6).pack(side=LEFT) #need to add command to decode
    Label(fr1,text="  ",bg="cyan").pack(side=LEFT)
    Button(fr1,text="Settings",bg="white",fg="black",justify=CENTER,width=10,height=1,bd=6).pack(side=LEFT)
    #menu=Menu(root)
    #fm=Menu(menu,title="Settings")
    #fm.add_command(label="Command One") #add command 1
    #fm.add_separator()
    #fm.add_command(label="Command Two") #add command 2
    #fm.add_separator()
    #root.config(title="GUI")
    fr2=Frame(root,bg="yellow",bd=16)
    fr2.pack(side=TOP)
    root.mainloop()
main()
