#Jake Okrent
# 4/18/2016
# IT 102 - Pick a  Pet

input("ADVENTURER, you have found the COMPANION TREE! Answer my questions and I'll grant you a powerful ally. PRESS ENTER TO CONTINUE")
gender = input("Well now, are ye a BOY or a GIRL?")
while gender != 'BOY' and gender != 'GIRL':
	gender = input("You'll have to speak up! Now, are ye a BOY or a GIRL?")
if gender == 'BOY':
	age = int(input("How old are ya, laddie?"))
elif gender == 'GIRL':
	age = int(input("How old are ya, lass?"))

if gender == 'BOY' and (0 < age < 15):
	print ("You, young sir, shall have a GRYPHON!")
elif gender == 'BOY' and (15< age < 40):
	print ("A mighty DRAGON for you, ser!")
elif gender == 'BOY' and (age >= 40):
	print (" An WISE OWL for a venerable elder!")
elif gender == 'GIRL' and (0 < age < 15):
	print ("You young lass shall have a FAIRY LIZARD!")
elif gender == 'GIRL' and (15< age < 40):
	print ("A UNICORN for you great Lady!")
elif gender == 'GIRL' and (age >= 40):
	print ("Your companion shall be a DIRE BEAR, wise woman.")	