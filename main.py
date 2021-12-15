#Step 1 
import random as rnd
word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

chosen_word = word_list[rnd.randint(0,len(word_list)-1)]
print (type(chosen_word))   # 1
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input ("Guess a letter, pls. ")
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
print (type(chosen_word))  #2 
# print (guess.lower)
n=0
counter=0
chosen_word = list(chosen_word)
for letter in chosen_word:
  if guess == chosen_word[n]:
    counter += 1
    print("Your letter " + guess + " is " + str(counter) + " times in the word.")
  else:
    print("Your letter " + guess + " is " + str(counter) + " times in the word.")
  n += 1

