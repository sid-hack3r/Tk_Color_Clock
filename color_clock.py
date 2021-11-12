from tkinter import *
from tkinter import messagebox as m
import random
import time

root=Tk()
root.geometry("1030x2100")
root.config(bg="black")

color=[
	"red",
	"orange",
	"blue",
	"magenta",
	"red",
	"yellow",
	"cyan",
	"blue",
	"green",
	"white",
]
#===================================
def exit():
	var=m.askquestion("EXIT","Do You Want To Exit .")
	if var =="yes":
		root.destroy()
		
#===================================	
def change ():
	top=Toplevel ()
	top.geometry("1030x2100")
	for i in range (1,1000):
		rc=random.choice(color)
		top.config(bg=rc)
		top.update_idletasks()
	top.mainloop()
	
#===================================
def start ():
	
	
	r=random.choice(color)
	lbl.config(fg=r)
	root.update_idletasks()
	root.config(bg="black")
	Time=time.strftime("%H:%M:%S")
	lbl.config(text=Time)
	lbl.after(100,start)
	


#Label	
#===================================
name=Label(
	root,
	text="developer by: SIDHARTH ",
	font=("times new roman ",5 ,"bold","italic"),
	bg="black",
	fg="orange"
)
name.pack(  anchor=E)
lbl=Label(
	root,
	font=("times New roman",25),
	bg="black",
	fg="white",
)

lbl.pack(pady=800)

	


#start button
#===================================
bt=Button(
	root,
	text="START",
	bg="cyan",
	fg="black",
	activebackground="cyan",
	activeforeground="black",
	relief=FLAT,
	bd=10,
	command=start,
	padx=100
	
)
bt.pack(anchor=S)

#exit button
#===================================
bt=Button(
	root,
	text="EXIT",
	bg="cyan",
	fg="black",
	activebackground="cyan",
	activeforeground="black",
	relief=FLAT,
	bd=10,
	command=exit,
	padx=133
	
)
bt.pack(side=RIGHT)
	
#color change button
#===================================	
btn=Button (
	root,
	text="Change Color",
	bg="cyan",
	fg="black",
	activebackground="cyan",
	activeforeground="black",
	relief=FLAT,
	bd=10,
	command=change,
)
btn.pack(side="left",padx=0)	

root.mainloop()