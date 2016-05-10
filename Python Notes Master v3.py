#Jake Okrent
#4/24/2016
#Python Notes V3

#Defining Functions
def arithmetic_operators():
	print ('''
Arithmetic Operators:
-------------------------------
''')
	print ('Add: 3+ 2 =' , 3 + 2)
	print ('Subtract: 3 - 2 =' , 3 - 2)
	print ('Multiply: 3 * 2 =' , 3 * 2)
	print ('Divide: 3 / 2 =' , 3 / 2)
	print ('Modulus: 3 % 2 =' , 3 % 2)
	print ('Floor: 3 // 2 =' , 3 // 2)
	print ('Exponents: 3 ** 2 =' , 3 ** 2)

def identifiers():
	print ('''
Identifier Names:
--------------------------
Can start with: a..zA..Z_ followed by a..zA..Z_0..9
Identifier names are case sensitive and cannot be a Keyword.
''')
    
def reserved_words():
	print ('''

List of Keywords:
--------------------------
and	del	from	not	while
as	elif	global 	or	with 
assert	else	if 	pass	yield 
break	except	import	print	TRUE
class	exec	in	raise	FALSE
continue	finally	is	return	
def	for	lambda	try	
''')
       
#Program header
print ('Welcome to Jake\'s PYTHON notes database!')
print ('''
Please choose from the following selections:

1. Arithmetic Operators
2. Identifiers
3. Reserved Words
9. Exit Program
''')

#Menu Navigation
user_input = input('Please make a Selection!')
while user_input != '1' and user_input != '2' and user_input != '3' and user_input != '9':
	user_input = input("I'm sorry, that's not an option. Try again.")

if user_input == '1':
    arithmetic_operators()
    user_input = input('''
Please make another Selection! 
(1. Arithmetic Operators, 2. Identifiers, 3. Reserved Words, 9. Exit)
''')
if user_input == '2':
    identifiers()
    user_input = input('''
Please make another Selection! 
(1. Arithmetic Operators, 2. Identifiers, 3. Reserved Words, 9. Exit)
''')
if user_input == '3':
    reserved_words()
    user_input = input('''
Please make another Selection! 
(1. Arithmetic Operators, 2. Identifiers, 3. Reserved Words, 9. Exit)
''')
if user_input == '9':
    print("Exiting Program. Goodbye!")

