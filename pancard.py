#pan card valid system
import re

while True:
	pattern = r"[A-Z][A-Z][A-Z][A-Z][A-Z][0-9][0-9][0-9][0-9][A-Z]"

	word = input('Enter your pan card number\n\n==>> ')

	if re.search(pattern, word):
		print('This pan card no. \"'+ word + '\" exist' )
		break
	else:
		print('does not exist')
	
