import ttkbootstrap as tb
from tkinter import Menu, StringVar

root = tb.Window(themename="superhero") # Or choose another theme
root.title("My Application")

menubar = Menu(root)
root.config(menu=menubar) 
file_menu = Menu(menubar, tearoff=True , background="lightblue", foreground="black")
edit_menu = Menu(menubar, tearoff=True)
file_menu.add_command(label="New", command=lambda: print("New clicked") )
file_menu.add_command(label="Open", command=lambda: print("Open clicked"))
file_menu.add_separator() # Add a separator line
file_menu.add_command(label="Exit", command=root.quit , accelerator="Ctrl+Q")
options_menu = Menu(file_menu, tearoff=True)
options_menu.add_command(label="Option 1")
options_menu.add_command(label="Option 2")
file_menu.add_cascade(label="Options", menu=options_menu)
menubar.add_cascade(label="File", menu=file_menu)
menubar.add_cascade(label="Edit", menu=edit_menu)
root.mainloop()