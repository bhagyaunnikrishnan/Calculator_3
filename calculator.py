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
######################################First Row########################################################################################
btnBackSpace = Button(MainFrame, width=6, height=2, font=('arial', 16, 'bold'), bd=4, text="DEL", bg="#FF9800")
btnBackSpace.grid(row=1, column=0, pady=1)

btnClear = Button(MainFrame, width=6, height=2, font=('arial', 16, 'bold'), bd=4, text=chr(67)+chr(76), bg="#FF9800")
btnClear.grid(row=1, column=1, pady=1)

btnClearAll = Button(MainFrame, width=6, height=2, font=('arial', 16, 'bold'), bd=4, text=chr(65)+chr(67), bg="#FF9800")
btnClearAll.grid(row=1, column=2, pady=1)

btnPM = Button(MainFrame, width=6, height=2, font=('arial', 16, 'bold'), bd=4, text=chr(177), bg="#FF9800")
btnPM.grid(row=1, column=3, pady=1)

######################################Scientific########################################################################################
btnSq = Button(MainFrame, width=6, height=2, font=('arial', 16, 'bold'), bd=4, text="√", bg="Black", fg="White")
btnSq.grid(row=2, column=0, pady=1)

btnCos = Button(MainFrame, width=6, height=2, font=('arial', 16, 'bold'), bd=4, text="Cos", bg="Black", fg="White")
btnCos.grid(row=2, column=1, pady=1)

btnSin = Button(MainFrame, width=6, height=2, font=('arial', 16, 'bold'), bd=4, text="Sin", bg="Black", fg="White")
btnSin.grid(row=2, column=2, pady=1)

btnTan = Button(MainFrame, width=6, height=2, font=('arial', 16, 'bold'), bd=4, text="Tan", bg="Black", fg="White")
btnTan.grid(row=2, column=3, pady=1)

######################################operators########################################################################################
btnAdd = Button(MainFrame, width=6, height=2, font=('arial', 16, 'bold'), bd=4, text="+", bg="Black", fg="White")
btnAdd.grid(row=3, column=3, pady=1)

btnSub = Button(MainFrame, width=6, height=2, font=('arial', 16, 'bold'), bd=4, text="-", bg="Black", fg="White")
btnSub.grid(row=4, column=3, pady=1)

btnMul = Button(MainFrame, width=6, height=2, font=('arial', 16, 'bold'), bd=4, text="*", bg="Black", fg="White")
btnMul.grid(row=5, column=3, pady=1)

btnDiv = Button(MainFrame, width=6, height=2, font=('arial', 16, 'bold'), bd=4, text="/", bg="Black", fg="White")
btnDiv.grid(row=6, column=3, pady=1)

btnZero = Button(MainFrame, width=6, height=2, font=('arial', 16, 'bold'), bd=4, text="0", bg="Black", fg="White")
btnZero.grid(row=6, column=0, pady=1)

btnDot = Button(MainFrame, width=6, height=2, font=('arial', 16, 'bold'), bd=4, text=".", bg="Black", fg="White")
btnDot.grid(row=6, column=1, pady=1)

btnEquals = Button(MainFrame, width=6, height=2, font=('arial', 16, 'bold'), bd=4, text="=", bg="Black", fg="White")
btnEquals.grid(row=6, column=2, pady=1)

#######################################################################################################################################

window.mainloop()