def clickedbt1():
    res = "Welcome to " + txt1.get()
    lb1.configure(text = res)

    #lb1.configure(text="Button was clicked!")
    #lb2 = tkinter.Label(window, text = "Button was clicked!").pack()


import tkinter
import tkinter.ttk

window  = tkinter.Tk()
window.title("NLI-GSC: Natural Language Interface for Generating Source Code")

window.geometry("1000x300")

lb1 = tkinter.Label(window, text = "Hello World")
bt1 = tkinter.Button(window, text="Enter", command = clickedbt1)
txt1= tkinter.Entry(window, width=10)

combo1 = tkinter.ttk.Combobox(window)
combo1['values'] = ("python", "C", "\'Algorithm\'")
combo1.current(0)


lb1.pack()
bt1.pack()
txt1.pack()
combo1.pack()

window.mainloop()


