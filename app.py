from tkinter import *

def clear():
    global display_string
    display_string = ""
    display_value.set("")
    return

def insert_value(val):
    global display_string
    display_string = display_string + str(val)
    display_value.set(display_string)
    return

def calculate():
    global display_string
    try:
        result = str(eval(display_string))
        display_value.set(result)
        display_string = result

    except SyntaxError:
        display_value.set("Syntax Error")
        display_string = ""

    except ZeroDivisionError:
        display_value.set("Arithmetic Error")
        display_string = ""

window = Tk()
window.configure(bg="#fff")
window.title("Calculator")

display_string = ""
display_value = StringVar(window)

display = Entry(window, font=('sans-serif', 40), bd=0, bg="#fff", fg="#8A4FFF", justify=RIGHT, width=14, textvariable=display_value)
display.grid(row=0, columnspan=4, ipady=20)

clear = Button(window, text="C", font=('sans-serif', 20), command=clear, bd=0, activebackground="#BCB6F6", bg="#C3BEF7", cursor="hand2").grid(row=1, column=0, columnspan=2, sticky="nwse", ipady=20)

percent = Button(window, text="%", font=('sans-serif', 20), command=lambda:insert_value("%"), bd=0, activebackground="#BCB6F6", bg="#C3BEF7", cursor="X_cursor", state=DISABLED).grid(row=1, column=2, sticky="nwse", ipady=20)

divide = Button(window, text="÷", font=('sans-serif', 24), command=lambda:insert_value("/"), bd=0, activebackground="#BCB6F6", bg="#C3BEF7", cursor="hand2").grid(row=1, column=3, sticky="nwse", ipady=20)

num_7 = Button(window, text="7", font=('sans-serif', 20), command=lambda:insert_value(7), bd=0, activebackground="#BCB6F6", bg="#C3BEF7", cursor="hand2").grid(row=2, column=0, sticky="nwse", ipady=20)

num_8 = Button(window, text="8", font=('sans-serif', 20), command=lambda:insert_value(8), bd=0, activebackground="#BCB6F6", bg="#C3BEF7", cursor="hand2").grid(row=2, column=1, sticky="nwse", ipady=20)

num_9 = Button(window, text="9", font=('sans-serif', 20), command=lambda:insert_value(9), bd=0, activebackground="#BCB6F6", bg="#C3BEF7", cursor="hand2").grid(row=2, column=2, sticky="nwse", ipady=20)

multiply = Button(window, text="×", font=('sans-serif', 20), command=lambda:insert_value("*"), bd=0, activebackground="#BCB6F6", bg="#C3BEF7", cursor="hand2").grid(row=2, column=3, sticky="nwse", ipady=20)

num_4 = Button(window, text="4", font=('sans-serif', 20), command=lambda:insert_value(4), bd=0, activebackground="#BCB6F6", bg="#C3BEF7", cursor="hand2").grid(row=3, column=0, sticky="nwse", ipady=20)

num_5 = Button(window, text="5", font=('sans-serif', 20), command=lambda:insert_value(5), bd=0, activebackground="#BCB6F6", bg="#C3BEF7", cursor="hand2").grid(row=3, column=1, sticky="nwse", ipady=20)

num_6 = Button(window, text="6", font=('sans-serif', 20), command=lambda:insert_value(6), bd=0, activebackground="#BCB6F6", bg="#C3BEF7", cursor="hand2").grid(row=3, column=2, sticky="nwse", ipady=20)

minus = Button(window, text="-", font=('sans-serif', 20), command=lambda:insert_value("-"), bd=0, activebackground="#BCB6F6", bg="#C3BEF7", cursor="hand2").grid(row=3, column=3, sticky="nwse", ipady=20)

num_1 = Button(window, text="1", font=('sans-serif', 20), command=lambda:insert_value(1), bd=0, activebackground="#BCB6F6", bg="#C3BEF7", cursor="hand2").grid(row=4, column=0, sticky="nwse", ipady=20)

num_2 = Button(window, text="2", font=('sans-serif', 20), command=lambda:insert_value(2), bd=0, activebackground="#BCB6F6", bg="#C3BEF7", cursor="hand2").grid(row=4, column=1, sticky="nwse", ipady=20)

num_3 = Button(window, text="3", font=('sans-serif', 20), command=lambda:insert_value(3), bd=0, activebackground="#BCB6F6", bg="#C3BEF7", cursor="hand2").grid(row=4, column=2, sticky="nwse", ipady=20)

plus = Button(window, text="+", font=('sans-serif', 20), command=lambda:insert_value("+"), bd=0, activebackground="#BCB6F6", bg="#C3BEF7", cursor="hand2").grid(row=4, column=3, sticky="nwse", ipady=20)

num_0 = Button(window, text="0", font=('sans-serif', 20), command=lambda:insert_value(0), bd=0, activebackground="#BCB6F6", bg="#C3BEF7", cursor="hand2").grid(row=5, column=0, sticky="nwse", ipady=20)

decimal_pt = Button(window, text=".", font=('sans-serif', 20), command=lambda:insert_value("."), bd=0, activebackground="#BCB6F6", bg="#C3BEF7", cursor="hand2").grid(row=5, column=1, sticky="nwse", ipady=20)

equal = Button(window, text="=", font=('sans-serif', 20), command=calculate, bd=0, activebackground="#7733FF", bg="#8A4FFF", fg="#fff", cursor="hand2").grid(row=5, column=2, columnspan=2, sticky="nwse", ipady=20)

window.mainloop()