#Jake Okrent
#4/20/2016
#Fun with For

begin_range = int (input ('Please enter a starting number'))
end_range = int (input ('Please enter an ending number'))
step_value = int (input ('Please enter an interval value'))

for num in range (begin_range, end_range, step_value):
	print (num, 'Green Python')
print ('Ah Ah Ah')