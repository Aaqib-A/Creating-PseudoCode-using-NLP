raw_datatypes = {"variable":"var", "var":"var",
                 "variables":"var", "vars":"var",
                 
                 "integer":"int", "int":"int",
                 "integers":"int", "ints":"int",
                 
                 "float":"float", "number":"float",  "num":"float", 
                 "floats":"float", "numbers":"float","nums":"float",
                 
                 "double":"double",
                 "doubles":"double",
                 
                 "boolean":"bool", "bool":"bool", 
                 "booleans":"bool", "bools":"bool",
                 
                 "character":"char",  "char":"char", 
                 "characters":"char", "chars":"char",
                 
                 "string":"str", "str":"str", 
                 "strings":"str", "strs":"str",
                 
                 "void":"void",
                 "voids":"void",
                 
                 "array":"array", "arr":"array", "list":"array", "vector":"array",
                 "arrays":"array", "arrs":"array", "lists":"array", "vectors":"array",
				 
				 "class":"class",
				 "classes":"class"}

raw_operators = {"add":"+", "addition":"+", "+":"+",
                 "sub":"-", "subtract":"-", "subtraction":"-", "-":"-", "minus":"-",
                 "mul":"*", "multiply":"*", "*":"*",
                 "divide":"/","div":"/", "/":"/",
                 "mod":"%", "modulo":"%", "modulus":"%", "%":"%"}


raw_commands=['create', 'define', 'declare', 'set', 'print', 'display']

raw_loops=['loop','loops'
           'for loop', 'for loops','for',
           'while loop','while loops', 'while',
           'do while loop','do while loops', 'do while']

raw_others=["time", 
            "times"]

custom_stoppers=['\. ',' then ', ' than ']

custom_class = ["log","screen", "database"]

#============== Lists End Here ==============#

'''
lang:
1 - Python
2 - C++
'''
lang=1

if lang==1:
	raw_datatypes["list"]="list"
	raw_datatypes["lists"]="list"
	raw_datatypes["vector"]="list"
	raw_datatypes["vectors"]="list"


#============== Saving Starts Here ==============#
dest_file="Dict_Lists"

#Saving
import shelve

import os
if not os.path.exists('Shelf'):
    os.makedirs('Shelf')
	
shelf = shelve.open("Shelf/" +dest_file+ ".shlf")
shelf["raw_datatypes"] = raw_datatypes
shelf["raw_operators"] = raw_operators
shelf["raw_commands"] = raw_commands
shelf["raw_loops"] = raw_loops
shelf["raw_others"] = raw_others
shelf["custom_stoppers"] = custom_stoppers

shelf.close()

'''
#Loading
shelf = shelve.open("Shelf/" +dest_file+ ".shlf")

new_raw_datatypes = shelf["raw_datatypes"]
new_raw_operators = shelf["raw_operators"]
new_raw_commands = shelf["raw_commands"]
new_raw_loops = shelf["raw_loops"]
new_raw_others = shelf["raw_others"]
new_custom_stoppers = shelf["custom_stoppers"]

shelf.close()

print(new_raw_datatypes, "\n")
print(new_raw_operators, "\n")
print(new_raw_commands, "\n")
print(new_raw_loops, "\n")
print(new_raw_others, "\n")
print(new_custom_stoppers, "\n")
'''



'''
import json
dict_list = [raw_datatypes, raw_operators, raw_commands, raw_loops, raw_others, custom_stoppers]
with open(dest_file, "w", encoding="utf-8") as output_file:
	for dict in dict_list:
		json.dump(dict, output_file)
		output_file.write("\n")	
'''