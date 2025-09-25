from tkinter import *

root = Tk()
photo = PhotoImage(file = "c:\chapter08\Cinamonroll icon dark.png")
label = Label(root, image=photo)
label.pack()
root.mainloop()