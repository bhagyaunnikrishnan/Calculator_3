from tkinter import *
import math
window = Tk()
blank_space = ""
window.configure(bg="#7F8C8D")
window.title("Scientific Calculator")
window.resizable(width=FALSE, height=False)
window.geometry("438x573+460+40")

coverFrame = Frame(window, bd=20, pady=2, relief=RIDGE)
coverFrame.grid()

coverMainFrame = Frame(coverFrame, bd=10, pady=2, bg="Silver", relief=RIDGE)
coverMainFrame.grid()

MainFrame = Frame(coverMainFrame, bd=5, pady=2, relief=RIDGE)
MainFrame.grid()

class Calculator():
    def __init__(self):
        self.total = 0
        self.current = ""
        self.input_value = True
        self.check_sum = False
        self.op = ""
        self.result = False

added_value = Calculator()
e = Entry(MainFrame, font=('arial', 18, 'bold'), bd=14, width=26, justify="right", bg="#ABEBC6")
e.grid(row=0, column=0, columnspan=4, pady=1)
e.insert(0, "0")

numpad = "789456123"
i = 0
btn =[]


for j in range(3,6):
    for k in range(3):
        btn.append(Button(MainFrame, width=6, height=2, font=('arial', 16, 'bold'), bd=4, text=numpad[i]))
        btn[i].grid(row=j, column=k, pady=1)
        i += 1

btnBackSpace = Button(MainFrame, width=6, height=2, font=('arial', 16, 'bold'), bd=4, text="DEL", bg="#FF9800")
btnBackSpace.grid(row=1, column=0, pady=1)

btnClear = Button(MainFrame, width=6, height=2, font=('arial', 16, 'bold'), bd=4, text=chr(67), bg="#FF9800")
btnClear.grid(row=1, column=1, pady=1)

window.mainloop()