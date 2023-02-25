import random

#HANGMAN
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

                                      
#Generate Random word

WordBank=["beekeper","house","city","lemonade","hangman","tutorial","park","sunday","car","bus","playmaker","mathmatician"]
RandomWord = random.choice(WordBank)
print(RandomWord)


#Generate Blanks

Blanks = ["_"]
x = 0
GameOutput = []
while len(RandomWord) > x:
    GameOutput.append(Blanks[0])
    x += 1
print(GameOutput)

    
#Check if correct  
#Ask User to Guess a letter



end = False
lives = 6
print(logo)
print("Welcome to Hangman")
while not end:
    
    LetterGuess = input(print("Guess a letter: ")).lower()
    for position in range(len(RandomWord)):
        letter = RandomWord[position]
        if letter == LetterGuess:
            GameOutput[position] = letter
            print(GameOutput)
            print("Correct!")
    
    if LetterGuess not in RandomWord:
        lives -= 1
        print("WRONG! LIVES LEFT: ")
        print(stages[lives])
        
    
    if lives < 1:
        end = True
        print("YOU HAVE LOST THE GAME :((((")

    if "_" not in GameOutput:
        end = True
        print("!!!!!!!YOU WIN!!!!!!!")
