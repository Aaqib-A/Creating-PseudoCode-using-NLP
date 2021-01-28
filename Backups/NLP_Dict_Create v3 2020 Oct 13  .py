raw_datatypes = {
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
				 "classes":"class"
				 }

raw_operators = {"add":"+", "addition":"+", "+":"+",
                 "sub":"-", "subtract":"-", "subtraction":"-", "-":"-", "minus":"-",
                 "mul":"*", "multiply":"*", "*":"*",
                 "divide":"/","div":"/", "/":"/",
                 "mod":"%", "modulo":"%", "modulus":"%", "%":"%"}


raw_commands = {"create":"define", "define":"define", "declare":"define", "set":"define",
				"print":"print", "display":"print", "show": "print",
				"get":"input", 
				"save":"save",}

raw_loops=['loop','loops']

raw_loop_types=['for', 'while', 'do']

raw_equal = ["equal","equals", "="]

raw_scope = ["global", "local"]

raw_others=["time", 
            "times", 
			"name", "them", "to", "on"]

custom_stoppers=['\. ',' then ', ' than ', ',']

custom_class = ["log","screen", "database", "printer"]

custom_puntuations = {"\"":"\"\"\"", "'":"\"\"\"", 
						".":".", ",":","}

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
	
	raw_datatypes["variable"] = "var"
	raw_datatypes["var"] = "var"
	raw_datatypes["variables"] = "var"
	raw_datatypes["vars"] = "var"
	


#============== Saving Starts Here ==============#
dest_file="NLP_Data/Shelf//" + "Dict_Lists" + ".shlf"

#Saving
import shelve

import os
if not os.path.exists('NLP_Data/Shelf'):
    os.makedirs('NLP_Data/Shelf')
	
shelf = shelve.open(dest_file)
shelf["raw_datatypes"] = raw_datatypes
shelf["raw_operators"] = raw_operators
shelf["raw_commands"] = raw_commands
shelf["raw_loops"] = raw_loops
shelf["raw_loop_types"] = raw_loop_types

shelf["raw_equal"] = raw_equal
shelf["raw_scope"] = raw_scope

shelf["raw_others"] = raw_others
shelf["custom_stoppers"] = custom_stoppers
shelf["custom_class"] = custom_class
shelf["custom_puntuations"] = custom_puntuations

shelf.close()

'''
#Loading
shelf = shelve.open(dest_file)

new_raw_datatypes = shelf["raw_datatypes"]
new_raw_operators = shelf["raw_operators"]
new_raw_commands = shelf["raw_commands"]
new_raw_loops = shelf["raw_loops"]
new_raw_loop_types = shelf["raw_loop_types"]

new_raw_equal = shelf["raw_equal"]
new_raw_scope = shelf["raw_scope"]

new_raw_others = shelf["raw_others"]
new_custom_stoppers = shelf["custom_stoppers"]
new_custom_class = shelf["custom_class"]
new_custom_puntuations = shelf["custom_puntuations"]
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