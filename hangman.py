import random

# hangman body parts
hangman1 = ['''
 +---+
     |
     |
     
    ===''','''
 +---+
     |
     |
     |
    ===''','''
 +---+
 o   |
 |   |
     |
    ===''','''
 +---+
 o   |
/|   |
     |
    ===''','''
 +---+
 o   |
/|\  |
     |
    ===''','''
 +---+
 o   |
/|\  |
/    |
    ===''','''
 +---+
 o   |
/|\  |
/ \  |    
    ==='''
]
# for i in range(7):
#     print(hangman1[i])

list1=['blue','orange','red','green','purple']
word=random.choice(list1).upper()
# to hold the letters guessed correctly
guessed=[] 
# to hold the letters guessed wrong
wrong=[]
tries=7
while tries>0:
   output=''
   for letter in word:
      if letter in guessed:
         output+=letter
      else:
         output+='_ '
   if output==word:
      break
   print("Guess the letter: ",output)
   print(tries, " chances left ")
   guess=input().upper()
   if guess in guessed or guess in wrong:
      print("Already guessed ", guess)
   elif guess in word:
      print('Yeah... You guessed it right ')
      guessed.append(guess)
   else:
      print('Oops... Try again ')
      print(hangman1[7-tries])
      tries-=1
      wrong.append(guess)
   print()

if tries>0:
   print("You guessed it right and you won  ")
else:
   print("You lost the game & the word is: ", word)
