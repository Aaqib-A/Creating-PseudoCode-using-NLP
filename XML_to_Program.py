import xml.etree.ElementTree as ET
import os

def get_xml_variables(data):
    
    #print(data)     
    var_name = data.get('name', None)
    var_scope = data.get('scope', None)
    var_datatype = data.get('datatype', None)
    var_value = data.get('value', None)
    
    final_sentence = ""
    
    #Python    
    if var_scope != None:
        if var_scope == "global":
            final_sentence += var_scope + " "
        if var_scope == "local":
            final_sentence += ""
    if var_datatype != None:
        final_sentence += var_datatype + " "
    final_sentence += var_name + " "
    if var_value != None:
        final_sentence += "= " + var_value
    
    return (final_sentence)

# ----- START Testing ----- #
'''
for child in root[1][0]:
    #print(child.tag, child.attrib)
    print( get_xml_variables(child.attrib) )
'''
# ----- END Testing ----- #

def get_xml_program(data_tag, data):
    #print(data)
    #var_name = data.get('name', None)
    #output_var = data.get('output', None)
    output_var = "answer"
    
    final_sentence = ""
    
    #get Variables - START
    variables = []
    temp_var_name = "variable"
    
    var_name = data.get(temp_var_name, None)
    if var_name != None:
        variables.append(var_name)
        
    for i in range(len(data)):
        var_name = data.get( temp_var_name+str(i+1), None )
        if var_name == None:
            break
        else:
            variables.append(var_name)
            
    #print(variables)
    #get Variables - END
    
  
    if data_tag == "print":
        #print("print")
        final_sentence = "print(" + variables[0]
        variables.pop(0)
        for each_var in variables:
            final_sentence += " + " + each_var
        final_sentence += ")"
        
    if data_tag == "input":
        #print("input")
        final_sentence = "input(" + variables[0]
        variables.pop(0)
        for each_var in variables:
            final_sentence += " + " + each_var
        final_sentence += ")"
        
    if data_tag == "add":
        final_sentence = output_var + " = " + variables[0]
        variables.pop(0)
        for each_var in variables:
            final_sentence += " + " + each_var
            
    if data_tag == "subtract":
        final_sentence = output_var + " = " + variables[0]
        variables.pop(0)
        for each_var in variables:
            final_sentence += " - " + each_var
            
    if data_tag == "multiply":
        final_sentence = output_var + " = " + variables[0]
        variables.pop(0)
        for each_var in variables:
            final_sentence += " * " + each_var

    if data_tag == "divide":
        final_sentence = output_var + " = " + variables[0]
        variables.pop(0)
        for each_var in variables:
            final_sentence += " / " + each_var
            
    if data_tag == "mod":
        final_sentence = output_var + " = " + variables[0]
        variables.pop(0)
        for each_var in variables:
            final_sentence += " % " + each_var

    return (final_sentence)

# ----- Start Testing -----#
'''
variables_ignore_flag = True
for child in root[1]:
    if variables_ignore_flag == True:
        variables_ignore_flag = False
        continue
    #print(child.tag, child.attrib)
    #print( get_xml_program(child.tag, child.attrib) )
'''
# ----- End Testing -----#   

def get_xml_program_type(data_tag,data):
    
    orig_statement = ""
    prog_type = ""
    prog_name = ""
    if data_tag == "statement":
        orig_statement = data.get("value", None)
        
    if data_tag == "program":
        prog_type = data.get("type", None)
        prog_name = data.get("name", None)
        
    return(prog_type, prog_name, orig_statement)

# ----- Start Testing -----#    
'''
prog_type, prog_name, orig_statement = get_xml_program_type(child.tag ,child.attrib)
print("statement : " +orig_statement)
print("type : " +prog_type)
print("name : " +prog_name)

if prog_type == "function":
    print("function")
if prog_type == "program":
    print ("program")
'''
# ----- End Testing -----#   

source = "Data"
filename = "pseudocode.xml"
root_path_file = os.path.join(source, filename) 
filename = "program.py"
save_path_file = os.path.join(source, filename) 
   
def XML_toProgram(root_path_file, save_path_file):

    tree = ET.parse(root_path_file)
    root = tree.getroot()
    
    
    for child in root:
        #print(child.tag ,child.attrib)
        #print(get_xml_program_type(child.tag ,child.attrib))
        if child.tag == "statement":
            temp_var, temp_var, orig_statement = get_xml_program_type(child.tag ,child.attrib)
        elif child.tag == "program":
            prog_type, prog_name, temp_var = get_xml_program_type(child.tag ,child.attrib)

    indentation_length = 0
    with open(save_path_file,"w") as file:
        if prog_type == "function":
            write_line = "def " +  prog_name+"():\n"
            file.write(write_line)
                
        if prog_type == "program":
            write_line = "def main():\n"
            file.write(write_line)
            

        indentation_length+=1
        
        variables_ignore_flag = True
        for child in root[1][0]:
            write_line = indentation_length*"\t" + get_xml_variables(child.attrib) +"\n"
            file.write(write_line)
        file.write("\n")
        for child in root[1]:
            if variables_ignore_flag == True:
                variables_ignore_flag = False
                continue
            #print(child.tag, child.attrib)
            
            write_line = indentation_length*"\t" + get_xml_program(child.tag, child.attrib) +"\n"
            file.write( write_line )
    
        indentation_length-=1
        
        
        if prog_type == "function":
            file.write("\n")
            write_line = prog_name+"()\n"
            file.write(write_line)
                
        if prog_type == "program":
            file.write("\n")
            file.write("\n")  
            write_line = "if __name__ == \"__main__\":\n"
            file.write(write_line)
            indentation_length+=1
            write_line = indentation_length*"\t" +"main()\n"
            file.write(write_line)
            
#XML_toProgram(root_path_file, save_path_file)
