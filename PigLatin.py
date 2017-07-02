# Pig Latin Translator

def PigLatin(word):
	if word.isalpha():
		pyg="ay"
		first = word[0]
		new_word = word+first+pyg
		new_word = new_word[1:len(new_word)]
		return new_word.lower()
	else:
		print "Failed"

word = PigLatin("Titties")
print word

def BiggestNumber(TestCase):
	print max(TestCase)
	

TestNum = [10, 20, 30, 1000]
BiggestNumber(TestNum)

from datetime import datetime

print datetime.today()


x = raw_input('Input: ')
print x