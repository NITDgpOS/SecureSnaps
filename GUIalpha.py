from Tkinter import *
root=None
img=None
pswd=None
def EnterPswd(x):
    global pswd
    pswd=Entry(x,show="*")
    pswd.pack(side=LEFT)
def main():
    global root
    global img
    root=Tk()
    fr1=Frame(root,bg="cyan",bd=16)
    fr1.pack(side=TOP)
    img=PhotoImage("abc.gif")
    Button(fr1,image=img,bd=4,width=80,height=80).pack(side=LEFT)
    Label(fr1,text="Password :",bg="cyan").pack(side=LEFT)
    EnterPswd(fr1)
    Label(fr1,text="  ",bg="cyan").pack(side=LEFT) 
    Button(fr1,text="Enc",bg="yellow",fg="red",justify=CENTER,width=5,height=2).pack(side=LEFT) #need to add command to encode
    Label(fr1,text=" ",bg="cyan").pack(side=LEFT)
    Button(fr1,text="Dec",bg="pink",fg="blue",justify=CENTER,width=5,height=2).pack(side=LEFT) #need to add command to decode
    Label(fr1,text="  ",bg="cyan").pack(side=LEFT)
    #menu=Menu(root)
    #fm=Menu(menu,title="Settings")
    #fm.add_command(label="Command One") #add command 1
    #fm.add_separator()
    #fm.add_command(label="Command Two") #add command 2
    #fm.add_separator()
    #root.config(title="GUI")
    
    root.mainloop()
main()
