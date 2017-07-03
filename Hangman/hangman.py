import random
import sys

print (sys.argv)

min_char = 4
if len(sys.argv) > 1:
	min_char = int(sys.argv[1])
	
def get_selected():
	with open ("words.txt", "r") as f:
		lines = f.readlines()
	for index in range(len(lines)):
		lines[index] = lines[index].strip()
	# lines = [s.strip() for s in lines]
	# print (lines[:10])
	words =[]
	"""for index in range(len(lines)):
		if len(lines[index]) >=4:	
			words.append(lines[index]) """
	for w in lines:
		if len(w) >=min_char:
			words.append(w)

	selected = random.choice(words)
	return selected

selected = get_selected()

def update(selected, guesses, lives):
	guessed = ""
	for i in selected:
		if i in guesses:
			guessed += i
		else:
			guessed += "_"
	print("\nWord so far:",guessed)
	print("All guesses:", guesses)
	print("Current lives:", lives)

def finished(selected, guesses):
	for i in selected:
		if i not in guesses:
			return False
	return True

lives = 6
guesses = []
while lives > 0 and not finished(selected, guesses):
	update(selected, guesses, lives)
	guess = input("Enter a letter:")[0]
	if guess not in selected and guess not in guesses:
		lives -= 1
	if guess in guesses:
		print("You've already entered that")
	guesses.append(guess)

if lives > 0:
	print("Congrats!")
else:
	print("You lose!")


print (selected)