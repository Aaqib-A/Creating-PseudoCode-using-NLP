import spacy
from spacy import displacy

nlp = spacy.load("./NLP_Object")
nlp_default = spacy.load("en_core_web_lg")

def entity_identify(statement):
    doc = nlp(statement) 
    
    ent_text=[]
    ent_label=[]
    for ent in doc.ents:
        #print (ent.text, ent.start_char, ent.end_char, ent.label_)
        ent_text.append(ent.text)
        ent_label.append(ent.label_)
        
    return (ent_text,ent_label)
	
def get_keywords(keyword):
    doc = nlp_default(keyword)
    token=""
    for word in doc:
        #print(word.lemma_)
        token = word.lemma_
        
    if (token == "int" or token == "integer"):
        return ("integer") 
    elif (token == "float"):
        return ("float") 
    elif (token == "number" or token == "num"):
        return ("number")
    elif (token == "variable" or token == "var" or token == "vari"):
        return ("variable")
    elif (token == "double" or token == "doub"):
        return ("double")
    elif (token == "long"):
        return ("long")
    elif (token == "byte"):
        return ("byte")
    elif (token == "short"):
        return ("short")
    
    elif (token == "character" or token == "char"):
        return ("char")
    elif (token == "string" or token == "str"):
        return ("string")
    elif (token == "text" or token == "txt"):
        return ("text")
    
    elif (token == "array" or token == "arr"):
        return ("array")
    elif (token == "list"):
        return ("list")
    elif (token == "vector" or token == "vec"):
        return ("vector")
    
    elif (token == "boolean" or token == "bool"):
        return ("boolean")
    elif (token == "class"):
        return ("class")
    elif (token == "void"):
        return ("void")
    
    elif (token == "global"):
        return ("global")
    elif (token == "local"):
        return ("local")

    elif (token == "addition" or token == "add" or token == "+"):
        return ("add")
    elif (token == "subtraction" or token == "sub" or token == "minus" or token == "min" or token == "-"):
        return ("subtract")
    elif (token == "multiply" or token == "mul" or token == "*"):
        return ("multiply")
    elif (token == "divide" or token == "div" or token == "/"):
        return ("divide")
    elif (token == "modulo" or token == "modulus" or token == "mod" or token == "%"):
        return ("mod")
    
    elif (token == "create" or token == "define" or token == "declare" or token == "set"):
        return ("create")
    elif (token == "print" or token == "display" or token == "show" or token == "write"):
        return ("print")
    elif (token == "get" or token == "input" or token == "insert"):
        return ("input")
    
    elif (token == "function" or token == "func"):
        return ("function")
    elif (token == "program" or token == "programme" or token == "prog" or token == "prg"):
        return ("program")
        
    elif(token == "if"):
        return("if")
    elif(token == "then"):
        return("then")
    #elif(token == "else if" or "elif" or "elseif" or "if else" or "ifelse"):
    #    return("else if")
    elif(token == "else"):
        return ("else")
    
    elif(token == "switch"):
        return("switch")
        
    elif(token == "for"):
        return("for")
    elif(token == "while"):
        return("while")
    elif(token == "do while"):
        return("do while")
        
        
    else:
        return(token)
    
#get_keywords("programme")
#get_keywords("save") #Wierd bug with else if statement	

def get_variables(statement):
    
    ent_text, ent_label = entity_identify(statement)
    
    vari_name = []
    vari_scope = []
    vari_datatype = []
    vari_value = []
    
    curr_var_name = "NA"
    curr_var_scope = "NA"
    curr_default_datatype = "NA"    
    curr_var_value = "NA"
    
    #print(ent_label)
    omit_if_none = ["VARI", "SCOPE", "DATATYPE", "VALUE", "TEXT"]
    if (set(omit_if_none) & set(ent_label)): #If both intersects
        #print("Something matches")
        print("",end="")
    else:
        return(vari_name, vari_scope, vari_datatype, vari_value)
            
    
    variable_flag = [0, 0, 0, 0]
    for index in range(len(ent_text)):
        if ent_label[index] == "SEPERATOR" and 1 in variable_flag:
            
            vari_name.append(curr_var_name)
            vari_scope.append(curr_var_scope)
            vari_datatype.append(curr_default_datatype)
            vari_value.append(curr_var_value)   
            
            variable_flag = [0, 0, 0, 0]
            curr_var_name = "NA"
            curr_var_scope = "NA"
            curr_var_value = "NA"
        
        if ent_label[index]== "VARI":
            variable_flag[0]+=1
            if variable_flag[0]>=2:
                
                vari_name.append(curr_var_name)
                vari_scope.append(curr_var_scope)
                vari_datatype.append(curr_default_datatype)
                vari_value.append(curr_var_value) 
    
                variable_flag = [1, 0, 0, 0]
                curr_var_name = "NA"
                curr_var_scope = "NA"
                curr_var_value = "NA"
            curr_var_name = ent_text[index]
            
        if ent_label[index] == "SCOPE": 
            variable_flag[1]+=1 
            if variable_flag[1]>=2:
                vari_name.append(curr_var_name)
                vari_scope.append(curr_var_scope)
                vari_datatype.append(curr_default_datatype)
                vari_value.append(curr_var_value) 
    
                variable_flag = [0, 1, 0, 0]
                curr_var_name = "NA"
                curr_var_scope = "NA"
                curr_var_value = "NA"
            curr_var_scope = get_keywords(ent_text[index])
            
        if ent_label[index] == "DATATYPE": 
            variable_flag[2]+=1
            if variable_flag[2]>=2:
                vari_name.append(curr_var_name)
                vari_scope.append(curr_var_scope)
                vari_datatype.append(curr_default_datatype)
                vari_value.append(curr_var_value) 
    
                variable_flag = [0, 0, 1, 0]
                curr_var_name = "NA"
                curr_var_scope = "NA"
                curr_var_value = "NA"
            curr_default_datatype = get_keywords(ent_text[index])
            
        if ent_label[index] == "VALUE" or ent_label[index] == "TEXT":
            variable_flag[3]+=1
            if variable_flag[3]>=2:
                vari_name.append(curr_var_name)
                vari_scope.append(curr_var_scope)
                vari_datatype.append(curr_default_datatype)
                vari_value.append(curr_var_value) 
    
                variable_flag = [0, 0, 0, 1]
                curr_var_name = "NA"
                curr_var_scope = "NA"
                curr_var_value = "NA"
            curr_var_value = ent_text[index]
            #print("Value detected: "+curr_var_value)
            
    #if curr_var_name != "NA":
    #    vari_name.append(curr_var_name)
    #elif curr_default_datatype != "NA":
    #    vari_name.append(curr_default_datatype+"_1")
    #else:
    #    vari_name.append("string_1")
    
    #Special Cases - Start     
    #Filling missing information if name is given (Last value only)
    if curr_var_name != "NA":
        vari_name.append(curr_var_name)    
        vari_scope.append(curr_var_scope)
        vari_datatype.append(curr_default_datatype)
        vari_value.append(curr_var_value) 
                
        variable_flag = [0, 0, 0, 0]
        curr_var_name = "NA"
        curr_var_scope = "NA"
        curr_var_value = "NA"

    #Filling missing information if no name is given (Last value only)
    elif curr_var_name == "NA":
        if curr_default_datatype == "NA":
            curr_default_datatype = assign_default_datatype(ent_label)
        vari_name.append(curr_default_datatype+"_1")
        vari_scope.append(curr_var_scope)
        vari_datatype.append(curr_default_datatype)
        vari_value.append(curr_var_value) 
                
        variable_flag = [0, 0, 0, 0]
        curr_var_name = "NA"
        curr_var_scope = "NA"
        curr_var_value = "NA"      
    #Special Cases - END
        
    #Set default datatype - START
    if vari_datatype != []:
        if vari_datatype[-1] == "NA":
            curr_default_datatype = assign_default_datatype(ent_label)
            #if "VALUE" in ent_label: 
            #    curr_default_datatype = get_keywords("float")
            #elif "TEXT" in ent_label:
            #    curr_default_datatype = get_keywords("string")
            #else:
            #    curr_default_datatype = get_keywords("string")
            
        for index, each_vari_datatype in enumerate(vari_datatype):
            if each_vari_datatype == "NA":
                vari_datatype[index] = curr_default_datatype                 
    #Set default datatype - END  
    
    #Solves first name as 'NA' bug - Start
    for index, loop_vari in enumerate(vari_name):
        if loop_vari == "NA":
            temp_number_extension = 1
            temp_name = vari_datatype[index]+"_"+str(temp_number_extension)
            while temp_name in vari_name:
                temp_number_extension += 1
                temp_name = vari_datatype[index]+"_"+str(temp_number_extension)
            vari_name[index] = temp_name
    #Solves first name as 'NA' bug - End
    
    return(vari_name, vari_scope, vari_datatype, vari_value)

def assign_default_datatype(ent_label):
    if "VALUE" in ent_label: 
        return get_keywords("float")
    elif "TEXT" in ent_label:
        return get_keywords("string")
    else:
        return get_keywords("string")
    
def get_func_prog_name(statement):
    
    ent_text, ent_label = entity_identify(statement)
    
    func_prog_name=""
    name_detector_flag = 0
    
    
    for index in range(len(ent_text)):
        
        #If user specifies the function name
        if (ent_label[index] == "FUNC_NAME"):
            func_prog_name = ent_text[index]
            name_detector_flag = 2
            break;
        
        #If user does not specifies the function name
        if (name_detector_flag<2):                
            if(ent_label[index] == "FUNC_PROG"):
                if name_detector_flag ==0:
                    func_prog_name += ent_text[index]
                elif name_detector_flag !=0:
                    func_prog_name += "_"+ ent_text[index]
                #name_detector_flag +=1
                name_detector_flag +=0.5
                
            elif(ent_label[index] == "OPERATOR"):
                if name_detector_flag ==0:
                    func_prog_name += ent_text[index]
                elif name_detector_flag ==1:
                    func_prog_name += "_"+ ent_text[index]
                name_detector_flag +=1
                
            elif(ent_label[index] == "DATATYPE"):
                if name_detector_flag ==0:
                    func_prog_name += ent_text[index]
                elif name_detector_flag !=0:
                    func_prog_name += "_"+ ent_text[index]
                name_detector_flag +=1
                
            elif(ent_label[index] == "COMMAND"):
                if name_detector_flag ==0:
                    func_prog_name += ent_text[index]
                elif name_detector_flag !=0:
                    func_prog_name += "_"+ ent_text[index]
                #name_detector_flag +=1
                name_detector_flag +=0.5
                
            elif(ent_label[index] == "VARI"):
                if name_detector_flag ==0:
                    func_prog_name += ent_text[index]
                elif name_detector_flag !=0:
                    func_prog_name += "_"+ ent_text[index]
                name_detector_flag +=1
                
        if func_prog_name=="":
            func_prog_name = "program1"
    
    return (func_prog_name)
	
#import re
def get_operations(statement):
    ent_text, ent_label = entity_identify(statement)
    
    operator=""
    variables=[]
    special_class = ""
    for index in range(len(ent_text)):
              
        if(ent_label[index] == "OPERATOR"):
            if ent_text[index] == "+" and operator == "":
                operator = get_keywords(ent_text[index])
            
        elif(ent_label[index] == "VARI"):
            variables.append(ent_text[index])
        
        elif(ent_label[index] == "TEXT"):
            temp_remo_quote = ent_text[index]
            temp_remo_quote = temp_remo_quote.replace("'", "")
            temp_remo_quote = temp_remo_quote.replace("\"", "")
            
            variables.append(temp_remo_quote)
        
        if(ent_label[index] == "COMMAND"):
            operator = get_keywords(ent_text[index])
        
        if(ent_label[index] == "SPL_CLASS"):
            special_class = ent_text[index]
           
    return (operator, variables, special_class)

'''
from xml.dom import minidom 
import os  

root = minidom.Document() 
  
xml = root.createElement('root')  
root.appendChild(xml) 
  
productChild = root.createElement('product') 
productChild.setAttribute('name', 'Geeks for Geeks') 
  
xml.appendChild(productChild) 
  
xml_str = root.toprettyxml(indent ="\t")  
  
save_path_file = "gfg.xml"
  
with open(save_path_file, "w") as f: 
    f.write(xml_str)  
'''

#nlpToXML main function

from xml.dom import minidom 
import os 
def nlpToXML(statement):
    root = minidom.Document() 
    xml = root.createElement('root')  
    root.appendChild(xml) 
    
    ent_text, ent_label = entity_identify(statement)
    
    #=== Basics ===#
    '''
    productChild = root.createElement('product') 
    productChild.setAttribute('name', 'Geeks for Geeks') 

    xml.appendChild(productChild)
    '''
    #=== Basics ===#
    
    #Statement - Start
    statementChild = root.createElement('statement') 
    statementChild.setAttribute('value', statement) 

    xml.appendChild(statementChild)
    #Statement - End
    
    #Prog - Start
    prog = root.createElement('program') #
    if "FUNC_PROG" in ent_label:
        index = ent_label.index("FUNC_PROG")
        prog.setAttribute('type', get_keywords(ent_text[index])) #

    else:
        prog.setAttribute('type', "program") #

    program_name = get_func_prog_name(statement)
    prog.setAttribute('name', program_name) #
    xml.appendChild(prog)  #
    #Prog - End
    
    #Variables - Start
    variables_xml = root.createElement('variables') 
    prog.appendChild(variables_xml) 

    #vari_name_list = []
    #vari_scope_list = []
    #vari_datatype_list = []
    #vari_value_list = []
    vari_name_list, vari_scope_list, vari_datatype_list, vari_value_list = get_variables(statement)
    
    for index in range(len(vari_name_list)):
        variables_child_xml = root.createElement('variable')
        
        if vari_name_list[index] != "NA":
            variables_child_xml.setAttribute('name', vari_name_list[index]) 
        else:
            variables_child_xml.setAttribute('name', 'default_name')         
        if vari_scope_list[index] != "NA":
            variables_child_xml.setAttribute('scope', vari_scope_list[index]) 
        if vari_datatype_list[index] != "NA":
            variables_child_xml.setAttribute('datatype', vari_datatype_list[index])
        if vari_value_list[index] != "NA":
            variables_child_xml.setAttribute('value', vari_value_list[index])  
        
        variables_xml.appendChild(variables_child_xml) 
    #Variables - End
    
    #Operations - START
    oper, oper_vari_list, spl_class = get_operations(statement)
    if oper != "":
        operation = root.createElement(oper) 
        
        for index, each_oper_vari in enumerate(oper_vari_list):
            if len(oper_vari_list)>1:
                operation.setAttribute('variable'+str(index+1), each_oper_vari)
            else :
                operation.setAttribute('variable', each_oper_vari)
        
        if spl_class != "":
            operation.setAttribute('spl_class', spl_class)
        prog.appendChild(operation)
        
    #Operations - END
    
    xml_str = root.toprettyxml(indent ="\t")  
    
    return(program_name, xml_str)

source = "Data"
filename = "pseudocode.xml" 
save_path_file = os.path.join(source, filename) 

import re
def XML_Creator_func(statement, save_path_file):

    statement = re.sub("=", " = ", statement)
    statement = re.sub("  "," ", statement)   

    program_name, xml_str = nlpToXML(statement)

    if not os.path.exists(source):
        os.makedirs(source)

    with open(save_path_file, "w") as f: 
        f.write(xml_str)  

#XML_Creator_func(statement, save_path_file)	
