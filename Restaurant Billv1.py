#Jake Okrent
#4/1/2016
#Restaurant Bill

print ('''
JAKE'S TIP CALCULATOR V1.0
---------------------------
''')

Restaurant = input('Enter the Restaurant Name:')
Party = int(input('Enter the Number of guests:'))
Subtotal = float(input('Enter your bill amount:'))
Tip = float(input('Enter Tip Percentage as a whole number:'))/ 100
Tax = float(input('Enter the Tax Rate:'))/100
Total = Subtotal + (Subtotal * Tax) + (Subtotal * Tip)

print ('''
BILL BREAKDOWN
-------------------
''')
	

print (Restaurant.upper())

print ('Subtotal: $%.2f' %Subtotal)
print ('Tax: $%.2f' %(Subtotal*Tax))
print ('Tip: $%.2f' %(Subtotal*Tip))
print ('''
-------------------''')
print ('Total: $%.2f' %Total)
print ('Per Person: $%.2f' %(Total / Party))
input('''
----------------------------------
Press ENTER to exit the program...
----------------------------------
''')
