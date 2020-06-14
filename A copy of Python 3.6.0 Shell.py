#A copy of Python 3.6.0 Shell


import tkinter

def do_nothing():
    print("ok ok..I will do nothing;although I ought to.")

window = tkinter.Tk()
window.title("Python 3.6.0 Shell")

#Create the main menubar
menu_bar = tkinter.Menu(window)

#Configure the menu bar
window.config(menu = menu_bar)

#create the file menu. It will be located in the menu bar
file_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="File", menu= file_menu )

#****** File*****
file_menu.add_command(label="New File          Ctrl+N", command= do_nothing)
file_menu.add_command(label="Open...           Ctrl+O", command =do_nothing)
file_menu.add_command(label="Open Module... Alt+M", command = do_nothing)
file_menu.add_command(label="Recent Files ", command = do_nothing)
file_menu.add_command(label="Class Browser  Alt+C", command = do_nothing)
file_menu.add_command(label="Path Browser ", command= do_nothing)
file_menu.add_separator()
file_menu.add_command(label="Save          Ctrl+S",  command= do_nothing)
file_menu.add_command(label="Save As.....      Ctrl+Shift+S  ",              command= do_nothing)
file_menu.add_command(label="Save Copy As...   Alt+Shift+S", command=do_nothing)
file_menu.add_separator()
file_menu.add_command(label="Print Window      Ctrl+P", command=do_nothing)
file_menu.add_separator()
file_menu.add_command(label="Close      Alt+F4", command = do_nothing)
file_menu.add_command(label="Exit         Ctrl+Q", command=do_nothing)

#*******Edit*******
edit_menu= tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

edit_menu.add_command(label="Undo          Ctrl+Z", command= do_nothing)
edit_menu.add_command(label="Redo          Ctrl+Shift+Z", command =do_nothing)
edit_menu.add_separator()
edit_menu.add_command(label="Cut          Ctrl+X", command =do_nothing)
edit_menu.add_command(label="Copy            Ctrl+C",command =do_nothing)
edit_menu.add_command(label="Paste         Ctrl+V", command =do_nothing)
edit_menu.add_command(label="Select All      Ctrl+A", command =do_nothing)
edit_menu.add_separator()
edit_menu.add_command(label="Find...                               Ctrl+F",command =do_nothing)
edit_menu.add_command(label="Find Again                          Ctrl+G",command =do_nothing)
edit_menu.add_command(label="Find Selection                     Ctrl+F3",command =do_nothing)
edit_menu.add_command(label="Find in Files...                     Alt+F3",command =do_nothing)
edit_menu.add_command(label="Replace...                          Ctrl+H",command =do_nothing)
edit_menu.add_command(label="Go to Line                          Alt+G",command =do_nothing)
edit_menu.add_command(label="Show Completions                Ctrl+space",command =do_nothing)
edit_menu.add_command(label="Expand Word                      Alt+/",command =do_nothing)
edit_menu.add_command(label="Show call tip                      Ctrl+backslash ",command =do_nothing)
edit_menu.add_command(label="Show surrounding parens       Ctrl+()",command =do_nothing)

#*****Shell****
shell_menu = tkinter.Menu()

menu_bar.add_cascade(label="Shell", menu=shell_menu)
shell_menu.add_command(label="View Last Restart    F6", command =do_nothing)
shell_menu.add_command(label="Restart Shell    Ctrl+F6 ", command =do_nothing)
shell_menu.add_separator()
shell_menu.add_command(label="Interrupt Execution      Ctrl+C ", command =do_nothing)

#**********Debug********
debug_menu= tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Debug", menu = debug_menu)

debug_menu.add_command(label="Go to File/Line", command =do_nothing)
debug_menu.add_command(label="Debugger", command =do_nothing)
debug_menu.add_command(label="Stack Viewer", command =do_nothing)
debug_menu.add_command(label="Auto-open Stack Viewer", command =do_nothing)


#**********    Options  ********
options_menu = tkinter.Menu(menu_bar)

menu_bar.add_cascade(label="Options", menu = options_menu)
options_menu.add_command(label= "Configure IDLE", command = do_nothing)
options_menu.add_separator()

#**********    Window  ********
window_menu= tkinter.Menu(menu_bar)

menu_bar.add_cascade(label="Window", menu = window_menu)

window_menu.add_command(label="Zoom Height        Alt+2", command = do_nothing)
window_menu.add_separator()
window_menu.add_command(label="Python 3.6.0 Shell", command = do_nothing)

#**********    Help  ********

help_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Help", menu= help_menu)

help_menu.add_command(label="About IDLE", command = do_nothing)
help_menu.add_separator()
help_menu.add_command(label="IDLE Help", command = do_nothing)
help_menu.add_command(label="Python Docs      F1", command= do_nothing)
help_menu.add_command(label="Turtle Demo ", command=do_nothing)


#                           *******TOOLBAR*******

toolbar = tkinter.Frame(window, bg = "orange")
toolbar.pack(side="top",fill="x")


insert_butt = tkinter.Button(toolbar, text="44-4", command= do_nothing)
insert_butt.pack(side="left", padx=2, pady=2)

print_butt = tkinter.Button(toolbar, text="Print", command= do_nothing)
print_butt.pack(side="left", padx=2, pady=2)




































window.mainloop()
