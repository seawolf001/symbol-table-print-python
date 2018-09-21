#####################################################
############          GROUP 7           #############
############  ANUPAM DAS  1401CS52      #############
############  JITENDRA KUMAR  1401CS19  #############
############  SATYA PRAKASH  1401CS06   #############
#####################################################


import re           # re is imported to process the strings in inputed file with regular expression                                                

# customised `symTableNode` class to hold the structure of the symbolTable 	
# data members: 
# 	type	-->	will hold the data types of the identifier
#	size	-->	will hold the data size of the identifer(char: 1byte, int: 4byte)
#	name	-->	name of valid identifier														
class symTableNode: 
	def __init__ (self, type, name, size):                  # class constructor that Python calls when we create a new instance of this class.
		self.type = type									# will hold the data types of the identifier
		self.size = size									# will hold the data size of the identifer(char: 1byte, int: 4byte)
		self.name = name									# will hold the name of valid identifier
		

regex_operator=ur"[+\-*/%]"                                 # unicode string regex for operator
regex_assignment=ur"==|!=|<=|>=|="                          # unicode string regex for assignment symbols
regex_symbols=ur"[\.\(\);{}\[\]]"                           # unicode string regex for special  symbols  
regex_identifier = ur"[a-zA-Z_$][a-zA-Z_$0-9]*"             # unicode string regex for identifier 
regex_char_const=ur"'\w'"                                   # unicode string regex for character constants 
regex_int_const = ur"(?<!\.)\b[0-9]+\b(?!\.[0-9])"          # unicode string regex for integer constants 
regex_boolean = ur"true|false"                              # unicode string regex for  boolean 
regex_operators_arithmetic = ur"[/*+-]"                     # unicode string regex for arithmetic symbols
regex_operators_boolean = ur"\band|or|not\b"                # unicode string regex for boolean operators
regex_operators_other = ur">|<|>=|<=|==|!="                 # unicode string regex for other operators
regex_key_words = ur"if|then|skip|else|while"               # unicode string regex for reserved keywords
regex_data_type = ur"int|char"                              # unicode string regex for data types


print "Enter the relative path of the file: ",
filename=raw_input()										# taking relative path of the file as user input	
with open (filename, "r") as f1:                            # opening the file 
	input_string=f1.read()	                                # reading  the  file and putting all in input_string variable
	total=input_string.split()                              # spliting the content of the  file on basis of whitespaces

print ""													# printing new line

identifier_list = re.findall(regex_identifier,input_string)     # store all non-overlapping matches of pattern in string in identifier_list
integer_constant_list = re.findall(regex_int_const,input_string)# store all non-overlapping matches of pattern in string in integer_constant_list
char_constant_list = re.findall(regex_char_const,input_string)  # store all non-overlapping matches of pattern in string in char_constant_list
type_list = re.findall(regex_data_type,input_string)            # store all non-overlapping matches of pattern in string in type_list
boolean_list = re.findall(regex_boolean,input_string)           # store all non-overlapping matches of pattern in string in boolean_list
opa_list = re.findall(regex_operators_arithmetic,input_string)  # store all non-overlapping matches of pattern in string in opa_list
opb_list = re.findall(regex_operators_boolean,input_string)     # store all non-overlapping matches of pattern in string in opb_list
opr_list = re.findall(regex_operators_other,input_string)       # store all non-overlapping matches of pattern in string in opr_list
keywords_list = re.findall(regex_key_words,input_string)        # store all non-overlapping matches of pattern in string in keywords_list

# combining all these list in a union_list except the identifier_list
union_list= integer_constant_list + char_constant_list + type_list + boolean_list + opa_list + opb_list + opr_list + keywords_list

# coverting the list into a set to remove multiple occurances
s=set(union_list)

# identifier list will contain all tokens except those fall in integer, character, data, boolean, relational and other keywords
diff_list= [x for x in identifier_list if x not in s]

print "Identifiers          ==",diff_list                       # printing identifiers
print "Integer Constants    ==",integer_constant_list           # printing integer  constants
print "Character constants  ==",char_constant_list              # printing character constants
print "Data types           ==",type_list                       # printing data types 
print "Boolean values       ==",boolean_list                    # printing boolean values
print "Arithmetic operators ==",opa_list                        # printing arithmetic operators
print "Relational operators ==",opr_list                        # printing relational operators
print "Boolean operators    ==",opb_list                        # printing boolean operators
print "keywords             ==",keywords_list                   # printing researved keywords
print ""														# printing new line


input_list = re.split(';| |\n|\{|\}|\(|\)',input_string)		# getting token from the input string with delimiter as punctuation and white space
print ""
print "Tokens:"
print input_list 
print ""

# printing tokens which are neither of the above mentioned catagories 
print "Error Words are :- "
error=[]														# will hold those error tokens
for word in input_list:										
	if(word !='' and word not in identifier_list and word not in integer_constant_list and word not in char_constant_list and word not in type_list and word not in boolean_list and word not in opa_list and word not in opr_list and word not in opb_list and word not in keywords_list ):
		print word.rstrip(),									# printitng all words by stripping its trailing new line characters
		error.append(word)										# and adding it to error list	
print ""

# computing symbol table
linecount = 0													# will hold the present line while iterating through the file
symtable = []													# will hold the list of the computed symbol tables
with open (filename, "r") as f:									# opening the file to parse it
        for line in f:                                          # reading from file  line by line
                linecount = linecount + 1						# counting the linecount
                words = line.split()                            # after reading  line by line spliting by whitespaces
                for i, word in enumerate (words):
                        if word == 'int':                       # insert into symbol table iff int was found before the variable
                                if i < (len(words) - 1):
                                        x = symTableNode (word, words[i + 1], 4)
                                        if words[i + 1] not in error:	# iff the word computed doesn't fall in error tokens
                                                symtable.append (x)		# adding the computed symbol table object at the end of the list
                        if word == 'char':                     # insert into symbol table iff char was found before the variable
                                if i < (len(words) - 1):
                                        x = symTableNode (word, words[i + 1], 1)
                                        if words[i + 1] not in error:	# iff the word computed doesn't fall in error tokens
                                                symtable.append (x)		# adding the computed symbol table object at the end of the list
	
		# printing symbol table
        print ('\nSymbol Table :\n')
        print (('{:8s} {:8s} {:12s}'.format ('Type', 'Name', 'Size (in bytes)')))	           # printing the heading of column of symbol table
        for j, symbol in enumerate (symtable):						
                print (('{:8s} {:8s} {:2d}'.format (symbol.type, symbol.name, symbol.size)))   # printing the result in formatted column format
                
