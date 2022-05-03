import tkinter as tk

root = tk.Tk()
root.title("Simple Calculator")
root.iconbitmap("Calc.ico")

e = tk.Entry(root, width=35 , borderwidth=3)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def clicked(number):
	e.insert(tk.END, number)


def clear_button():
	e.delete(0, tk.END)

global first_number

def clicked_add():
	global first_number
	first_number = int(e.get())
	e.delete(0, tk.END)
	global operation
	operation = "+"


def clicked_substract():
	global first_number
	first_number = int(e.get())
	e.delete(0, tk.END)
	global operation
	operation = "-"


def clicked_multiplication():
	global first_number
	first_number = int(e.get())
	e.delete(0, tk.END)
	global operation
	operation = "*"


def clicked_division():
	global first_number
	first_number = int(e.get())
	e.delete(0, tk.END)
	global operation
	operation = "/"


def clicked_equal():
	global first_number
	second_number = int(e.get())
	e.delete(0, tk.END)
	if(operation == '+'):
		first_number = first_number + second_number
		e.insert(0, first_number)
	elif(operation == '-'):
		first_number = first_number - second_number
		e.insert(0, first_number)
	elif(operation == '*'):
		first_number = first_number * second_number
		e.insert(0, first_number)
	elif(operation == '/'):
		first_number = first_number / second_number
		e.insert(0, first_number)
	


button_1 = tk.Button(root, text="1", padx=30, pady=10, font=20,
                     borderwidth=3, command=lambda: clicked(1)).grid(row=1, column=0)
button_2 = tk.Button(root, text="2", padx=30, pady=10, font=20,
                     borderwidth=3, command=lambda: clicked(2)).grid(row=1, column=1)
button_3 = tk.Button(root, text="3", padx=30, pady=10, font=20,
                     borderwidth=3, command=lambda: clicked(3)).grid(row=1, column=2)
button_4 = tk.Button(root, text="4", padx=30, pady=10, font=20,
                     borderwidth=3, command=lambda: clicked(4)).grid(row=2, column=0)
button_5 = tk.Button(root, text="5", padx=30, pady=10, font=20,
                     borderwidth=3, command=lambda: clicked(5)).grid(row=2, column=1)
button_6 = tk.Button(root, text="6", padx=30, pady=10, font=20,
                     borderwidth=3, command=lambda: clicked(6)).grid(row=2, column=2)
button_7 = tk.Button(root, text="7", padx=30, pady=10, font=20,
                     borderwidth=3, command=lambda: clicked(7)).grid(row=3, column=0)
button_8 = tk.Button(root, text="8", padx=30, pady=10, font=20,
                     borderwidth=3, command=lambda: clicked(8)).grid(row=3, column=1)
button_9 = tk.Button(root, text="9", padx=30, pady=10, font=20,
                     borderwidth=3, command=lambda: clicked(9)).grid(row=3, column=2)
button_0 = tk.Button(root, text="0", padx=75, pady=10, font=20, borderwidth=3,
                     command=lambda: clicked(0)).grid(row=4, column=0, columnspan=2)
button_add = tk.Button(root, text="+", padx=30, pady=10, font=20,
                       borderwidth=3, command=clicked_add).grid(row=4, column=2)
button_substract = tk.Button(root, text="-", padx=30, pady=10, font=20,
                             borderwidth=3, command=clicked_substract).grid(row=5, column=0)
button_multiply = tk.Button(root, text="x", padx=30, pady=10, font=20,
                            borderwidth=3, command=clicked_multiplication).grid(row=5, column=1)
button_division = tk.Button(root, text="/", padx=30, pady=10, font=20,
                            borderwidth=3, command=clicked_division).grid(row=5, column=2)
button_equal = tk.Button(root, text="=", padx=30, pady=10, font=20,
                         borderwidth=3, command=clicked_equal).grid(row=6, column=0)
button_clear = tk.Button(root, text="C", padx=75, pady=10, font=20,
                         borderwidth=3, command=clear_button).grid(row=6, column=1, columnspan=2)

root.mainloop()
