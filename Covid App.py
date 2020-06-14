from tkinter import *
import tkinter.messagebox

main= Tk()


main.geometry("800x650")
#one=tkinter.Label(main, text="Welcome to the Corona Virus Fact Zone.")
#one.pack()
main.title("COVID-19 FACT CHECK")

tkinter.messagebox.showinfo("Corona Info", "Corona Virus's death toll continues to climb astronomically.")

    
ans= tkinter.messagebox.askquestion("Question One", "Can the Corona Virus spread through hands?")
if ans == "yes":
    tkinter.messagebox.showinfo("Question response", "That's correct\n\nThe virus can spread to one's body if you use your dirty hands to touch your face.\nThank you.")
    #print("works")
    
else:
    tkinter.messagebox.showinfo("Question response", "Wrong choice...\n\nPlease try again.")

two=tkinter.Label(main, text="Thank you for using the fact check.\nYou can close the program now.")
two.pack()
main.mainloop()
