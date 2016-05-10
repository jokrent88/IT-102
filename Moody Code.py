#Jake Okrent
#4/11/2016
#Moody

Mood_Number = int(input('Pick any number between 1 and 3:'))
while Mood_Number != 1 and 2 and 3:
	Mood_Number = int(input('Invalid. Please pick any number between 1 and 3:'))
if Mood_Number == 1:
	print(":) You are Happy!!! :)")
elif Mood_Number == 2:
	print(":| You are Neutral... :|")
else:
	print(":( You are Sad! :(")
	