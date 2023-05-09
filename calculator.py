from tkinter import *
import math as m
window = Tk()
window.configure(bg="#BFC9CA")
window.title("Scientific Calculator")
e = Entry(window, width=50, borderwidth=5, relief=RIDGE, fg="White", bg="#ABEBC6")
e.grid(row=0, column=0, columnspan=5, padx=10, pady=15)
window.mainloop()