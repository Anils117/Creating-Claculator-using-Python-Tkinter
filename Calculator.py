from tkinter import *
tk=Tk()
tk.title("Calculator")

input=Entry(tk,width=40)
input.grid(row=0,column=0,columnspan=4,padx=10,pady=10)

def click(n):
	string=input.get()
	input.delete(0,END)
	num=str(string)+str(n)
	input.insert(0,num)

def clear():
	input.delete(0,END)

def addition():
	first_number=input.get()
	global f_num
	global math
	math="addition"
	f_num=int(first_number)
	input.delete(0,END)

def subtraction():
	first_number=input.get()
	global f_num
	global math
	math="subtraction"
	f_num=int(first_number)
	input.delete(0,END)

def multiplication():
	first_number=input.get()
	global f_num
	global math
	math="multiplication"
	f_num=int(first_number)
	input.delete(0,END)

def divison():
	first_number=input.get()
	global f_num
	global math
	math="divison"
	f_num=int(first_number)
	input.delete(0,END)

def equal():
	second_number=input.get()
	input.delete(0,END)

	if math=="addition":
		input.insert(0,f_num+int(second_number))
	if math=="subtraction":
		input.insert(0,f_num-int(second_number))
	if math=="multiplication":
		input.insert(0,f_num*int(second_number))
	if math=="divison":
		input.insert(0,f_num/int(second_number))

button_1=Button(tk,text="1",padx=30,pady=10,command=lambda : click(1))
button_2=Button(tk,text="2",padx=30,pady=10,command=lambda : click(2))
button_3=Button(tk,text="3",padx=30,pady=10,command=lambda : click(3))
button_4=Button(tk,text="4",padx=30,pady=10,command=lambda : click(4))
button_5=Button(tk,text="5",padx=30,pady=10,command=lambda : click(5))
button_6=Button(tk,text="6",padx=30,pady=10,command=lambda : click(6))
button_7=Button(tk,text="7",padx=30,pady=10,command=lambda : click(7))
button_8=Button(tk,text="8",padx=30,pady=10,command=lambda : click(8))
button_9=Button(tk,text="9",padx=30,pady=10,command=lambda : click(9))
button_0=Button(tk,text="0",padx=30,pady=10,command=lambda : click(0))

button_addition=Button(tk,text="+",padx=30,pady=10,command=addition)
button_subtraction=Button(tk,text="-",padx=32,pady=10,command=subtraction)
button_multiplication=Button(tk,text="*",padx=32,pady=10,command=multiplication)
button_divison=Button(tk,text="%",padx=28,pady=10,command=divison)
button_clear=Button(tk,text="Clear",padx=20,pady=10,command=clear)
button_equal=Button(tk,text="=",padx=30,pady=10,command=equal)


button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)
button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)
button_0.grid(row=4,column=0)


button_addition.grid(row=1,column=3)
button_subtraction.grid(row=2,column=3)
button_multiplication.grid(row=3,column=3)
button_divison.grid(row=4,column=2)
button_clear.grid(row=4,column=1)
button_equal.grid(row=4,column=3)






tk.mainloop()
