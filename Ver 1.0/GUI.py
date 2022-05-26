from tkinter import *
from tkinter import filedialog as fd
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
def case():
	file_menu = Menu(window, tearoff = 0)
	file_menu.add_command(label = "Open File", command = open_file)
	file_menu.add_command(label = "Save File in a previously prepared", command = save_file)
	file_menu.add_command(label = "Save File manually", command = save_file_manually)
	mainmenu.add_cascade(label = "File", menu = file_menu)
	mainmenu.add_cascade(label = "Settings")
	mainmenu.add_cascade(label = "User")
	mainmenu.add_cascade(label = "Developer")
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