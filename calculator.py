from tkinter import *
import math as m
window = Tk()
window.configure(bg="#BFC9CA")
window.title("Scientific Calculator")
e = Entry(window, width=50, borderwidth=5, relief=RIDGE, fg="White", bg="#ABEBC6")
e.grid(row=0, column=0, columnspan=5, padx=10, pady=15)

def click(to_print):
    old = e.get()
    e.delete(0, END)
    e.insert(0, old+to_print)
    return

def sc(event):
    key = event.widget
    text = key['text']
    no = e.get()
    result=''
    if text=='deg':
        result=str(m.degrees(float(no)))
    if text=='sin':
        result=str(m.sin(float(no)))
    if text=='cos':
        result=str(m.cos(float(no)))
    if text=='tan':
        result=str(m.tan(float(no)))
    if text=='log':
        result=str(m.log10(float(no)))
    if text=='ln':
        result=str(m.log(float(no)))
    if text=='sqrt':
        result=str(m.(float(no)))



def clear():
    e.delete(0, END)
    return

def bksps():
    current = e.get()
    length = len(current)-1
    e.delete(length, END)

def evaluate():
    ans = e.get()
    ans = eval(ans)
    e.delete(0, END)
    e.insert(0, ans)
















"""log = Button(window, text="log", padx=25, pady=10, relief=RIDGE)
log.bind("<Button-1>", sc)
log.grid(row=1, column=0)

zero = Button(window, text="0", padx=27, pady=10, bg="Grey", fg="White", command=lambda:click("0"))
zero.grid(row=7, column=2)"""





window.mainloop()