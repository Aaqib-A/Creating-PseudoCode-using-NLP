def clickedbt1():
    #res = "Welcome to " + input_box.get()
    #output_box.configure(text = res)

    #lb1.configure(text="Button was clicked!")
    #lb2 = tkinter.Label(window, text = "Button was clicked!").pack()
    
    with open("xml_test.xml") as file:
        data = file.read()
        #output_label.configure(text = data)
        #output_box.configure(text = data
        output_box.set(data)

import spacy
from spacy import displacy

from xml.dom import minidom 
import xml.etree.ElementTree as ET

import os 
import re

from XML_Creator import *
from XML_to_Program import *

nlp = spacy.load("./NLP_Object")

def processStatement():

    source = "Data"
    filename = "pseudocode.xml"
    pseudocode_file = os.path.join(source, filename)
    
    statement = input_box.get()

    XML_Creator_func(statement, pseudocode_file)
    

    filename = "program.py"
    program_file = os.path.join(source, filename)
    
    XML_toProgram(pseudocode_file, program_file)
    
    with open(program_file) as file:
        data = file.read()
        #output_label.configure(text = data)
        #output_box.configure(text = data
        output_box.insert ( data, 0 )

import tkinter
import tkinter.ttk

window  = tkinter.Tk()
window.title("NLI-GSC: Natural Language Interface for Generating Source Code")

window.geometry("1000x300")





instruction_label = tkinter.Label(window, text = "Please enter your idea in Natural Language")
input_box = tkinter.Text(window)
output_box = tkinter.Text(window)
#output_label = tkinter.Label(window, text = "", justify="left")

combo1 = tkinter.ttk.Combobox(window)
combo1['values'] = ("python", "C", "\'Algorithm\'")
combo1.current(0)

bt1 = tkinter.Button(window, text="Enter", command = processStatement)


#combo1.pack()
#instruction_label.pack()
#input_box.pack()
#output_box.pack()
#bt1.pack()

combo1.grid(row=0,column=1)
instruction_label.grid(row=1,column=0)

input_box.grid(row=2,column=0)
output_box.grid(row=2,column=1)
#output_label.grid(row=2,column=1)
bt1.grid(row=3,column=0)#, colspan=2)


window.mainloop()


