from tkinter import *

root = Tk()
photo = PhotoImage(file = "c:\chapter08\Cinamonroll icon dark.png")
w = Label(root, image=photo, justify="left").pack(side="right")
Message = """귀여운 시나모롤"""
w2 = Label(root,
           padx=10,
           text=Message).pack(side="left")
root.mainloop()