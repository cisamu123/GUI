from tkinter import *
from tkinter import filedialog as fd
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
def click():
	username = username_entry.get()
	password = password_entry.get()

	messagebox.showinfo('Login successfully completed', f'{username}, {password}')
#WINDOW CREATE
window = Tk()
#WINDOW TITLE
window.title("GUI BY CISAMU")
#WINDOW GEOMETRY
window.geometry("400x500+600+300")
window.resizable(False, False)
#WINDOW ICO
window.iconbitmap("Icon.ico")
#WINDOW BACKGROUND
window['bg'] = 'black'
mainmenu = Menu(window)
window.config(menu = mainmenu)
def start():
	print("Hello!")
	print("Made a small GUI program. Use for any purpose, the program is open source. I ask you to mark the author under your modification. Because I have reserved all rights to use")
	print("#Author Cisamu")
	print("#All rights reserved (c)2022")
#WINDOW INPUT
EntryInput = Entry(window)
EntryInput.insert(0, 'Write: ')
#DELETE INPUT
def Every():
	EntryInput.delete(0, END)
DeleteButton = Button(window, font='Arial 15', text='Clear', command=Every)
def open_file():
	fd.askopenfilename()
	print("In this version of the program, this function does not work yet!")
def save_file():
	noteopen1 = open('Saved.txt', 'a') 
	noteopen1.write(EntryInput.get())
	noteopen1.close()
	print("The text was successfully saved to the folder with the program")
def save_file_manually():
	fd.asksaveasfilename()
	print("In this version of the program, this function does not work yet!")
def Settings_menu():
	Settings_window = Toplevel()
	Settings_window.title("Settings")
	Settings_window.resizable(0, 0)
	settingstxt = Label(Settings_window, text='SETTINGS', font='Arial 15 bold', bg='black', fg='white')
	canvas = Canvas(Settings_window, width=200, height=200, bg="black")
	settingstxt.pack()
	level_var = tk.IntVar()
	nation_var = tk.IntVar()
	level_text = tk.StringVar()
	tk.Radiobutton(Settings_window, text='White', variable=level_var, value=1).pack()
	tk.Radiobutton(Settings_window, text='Black', variable=level_var, value=2).pack()
	tk.Radiobutton(Settings_window, text='Blue', variable=level_var, value=3).pack()
	settl = {
		1: 'easy',
		2: 'easy2',
		3: 'easy3',
	}
	level = level_var.get()
	level_text.set(f"You select {level} setting")
	print("In this version of the program, this function does not work yet!")
	canvas.pack()
def Login():
	Login_window = Toplevel()
	Login_window.title("Login")
	Login_window.resizable(0, 0)
	canvas = Canvas(Login_window, width=200, height=200, bg="black")
	logintxt = Label(Login_window, text='LOGIN', font='Arial 15 bold', bg='black', fg='white')
	logintxt.pack()
	username_label = Label(Login_window, text='USERNAME', font='Arial 11 bold', bg='black', fg='white', padx=10, pady=8)
	username_label.pack()
	username_entry  = Entry(Login_window, font='Arial 12', bg='black', fg='lime')
	username_entry.pack()
	password_label = Label(Login_window, text='PASSWORD', font='Arial 11 bold', bg='black', fg='white', padx=10, pady=8)
	password_label.pack()
	password_entry  = Entry(Login_window, font='Arial 12', bg='black', fg='lime')
	password_entry.pack()
	canvas.pack()

	send_btn = Button(Login_window, text='Login', command=click)
	send_btn.pack(padx=10,pady=8)
def Developer():
	Developer_window = Toplevel()
	Developer_window.title("Developer")
	Developer_window.resizable(0, 0)
	Developerwin = Canvas(Developer_window, width=200, height=200, bg="black")
	developertxt = Label(Developer_window, text='DEVELOPER', font='Arial 15 bold', bg='black', fg='white')
	developertxt.pack()
	developer_label = Label(Developer_window, text='CISAMU', font='Arial 11 bold', bg='black', fg='white', padx=10, pady=8)
	developer_label.pack()
	developercopy_label = Label(Developer_window, text='(c) 2022', font='Arial 11 bold', bg='black', fg='white', padx=10, pady=8)
	developercopy_label.pack()
def case():
	file_menu = Menu(window, tearoff = 0)
	setting_menu = Menu(window, tearoff = 0)
	user_menu = Menu(window, tearoff = 0)
	developer_menu = Menu(window, tearoff = 0)
	file_menu.add_command(label = "Open File", command = open_file)
	file_menu.add_command(label = "Save File in a previously prepared", command = save_file)
	file_menu.add_command(label = "Save File manually", command = save_file_manually)
	mainmenu.add_cascade(label = "File", menu = file_menu)
	mainmenu.add_cascade(label = "Settings", menu = setting_menu)
	setting_menu.add_command(label = "Open", command = Settings_menu)
	mainmenu.add_cascade(label = "User", menu = user_menu)
	user_menu.add_command(label = "Open", command = Login)
	mainmenu.add_cascade(label = "Developer", menu = developer_menu)
	developer_menu.add_command(label = "Open", command = Developer)
EntryInput.pack()
DeleteButton.pack()

def main():
	start()
	case()
	Every()
main()
#WINDOW LOOP
window.mainloop()
#Author Cisamu
#All rights reserved (c)2022