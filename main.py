import tkinter as tk

calculation = ""

def add_to_calc(num):
    global calculation
    calculation += str(num)
    text_result.delete(1.0,"end")
    text_result.insert(1.0, calculation)

def eval_calc():
    try:
        global calculation
        calculation = str(eval(calculation))
        text_result.delete(1.0,"end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "Error!!!")

def clear_field():
    global calculation
    calculation = ""
    print("clearing")
    text_result.delete(1.0,"end")

r = tk.Tk()
r.geometry("310x275")

r.title('Calculator!!!')
text_result = tk.Text(r, height=2, width=16, font=("Ariel", 24))
text_result.grid(columnspan=5)

button = tk.Button(r, text='0', width=5, command=lambda: add_to_calc(0))
button.grid(row=2, column=1)
button1 = tk.Button(r, text='1', width=5, command=lambda: add_to_calc(1))
button1.grid(row=2, column=2)
button2 = tk.Button(r, text='2', width=5, command=lambda: add_to_calc(2))
button2.grid(row=2, column=3)
button3 = tk.Button(r, text='3', width=5, command=lambda: add_to_calc(3))
button3.grid(row=3, column=1)
button4 = tk.Button(r, text='4', width=5, command=lambda: add_to_calc(4))
button4.grid(row=3, column=2)
button5 = tk.Button(r, text='5', width=5, command=lambda: add_to_calc(5))
button5.grid(row=3, column=3)
button6 = tk.Button(r, text='6', width=5, command=lambda: add_to_calc(6))
button6.grid(row=4, column=1)
button7 = tk.Button(r, text='7', width=5, command=lambda: add_to_calc(7))
button7.grid(row=4, column=2)
button8 = tk.Button(r, text='8', width=5, command=lambda: add_to_calc(8))
button8.grid(row=4, column=3)
button_open = tk.Button(r, text='(', width=5, command=lambda: add_to_calc("("))
button_open.grid(row=5, column=1)
button9 = tk.Button(r, text='9', width=5, command=lambda: add_to_calc(9))
button9.grid(row=5, column=2)
button_close = tk.Button(r, text=')', width=5, command=lambda: add_to_calc(")"))
button_close.grid(row=5, column=3)
button_add = tk.Button(r, text='+', width=5, command=lambda: add_to_calc("+"))
button_add.grid(row=2, column=4)
button_sub = tk.Button(r, text='-', width=5, command=lambda: add_to_calc("-"))
button_sub.grid(row=3, column=4)
button_mul = tk.Button(r, text='*', width=5, command=lambda: add_to_calc("*"))
button_mul.grid(row=4, column=4)
button_div = tk.Button(r, text='/', width=5, command=lambda: add_to_calc("/"))
button_div.grid(row=5, column=4)
button_equal = tk.Button(r, text='=', width=15, command=lambda: eval_calc())
button_equal.grid(row=6, column=3, columnspan=2)
button_clear = tk.Button(r, text='C', width=15, command=lambda: clear_field())
button_clear.grid(row=6, column=1, columnspan=2)

r.mainloop()
