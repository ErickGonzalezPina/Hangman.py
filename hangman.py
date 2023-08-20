import random

def continue_game():
  continuing_game = False

  while continuing_game == False:
    user_response: str = input('Do you want to play again yes/no? ').lower()

    if user_response == 'no':
      print('Thanks for playing :)')
      quit()
    elif user_response == 'yes':
      continuing_game = True
    else:
      print('Invalid answer, respond with yes or no. \n')


def hangman():
  logo = ''' 
     _                                             
    | |                                            
    | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
    | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
    | | | | (_| | | | | (_| | | | | | | (_| | | | |
    |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |                      
                       |____/    '''

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

  word_list = [
    "Dog", "Cat", "Elephant", "Lion", "Tiger", "Giraffe", "Bear", "Wolf", "Monkey", "Horse",
    "Cheetah", "Zebra", "Kangaroo", "Koala", "Panda", "Rhino", "Gorilla", "Hippopotamus", "Dolphin",
    "Whale", "Penguin", "Polar bear", "Seal", "Ostrich", "Peacock", "Eagle", "Falcon", "Owl", "Parrot",
    "Flamingo", "Crocodile", "Alligator", "Snake", "Lizard", "Turtle", "Shark", "Octopus", "Jellyfish",
    "Crab", "Lobster", "Butterfly", "Bee", "Ant", "Spider", "Scorpion", "Bat", "Squirrel", "Rabbit",
    "Hedgehog", "Raccoon", "Fox", "Deer", "Moose", "Bison", "Cow", "Pig", "Sheep", "Goat", "Chicken",
    "Duck", "Turkey", "Swan", "Peacock", "Pigeon", "Hummingbird", "Pelican", "Oyster", "Clam", "Snail",
    "Worm", "Starfish", "Jellyfish", "Dolphin", "Seahorse", "Coral", "Platypus", "Koala", "Tasmanian Devil",
    "Emu", "Wombat", "Quokka", "Kangaroo", "Dingo", "Tasmanian Tiger", "Cassowary", "Wallaby", "Echidna",
    "Kiwi", "Kiwi", "Chimpanzee", "Lemur", "Orangutan", "Gorilla", "Baboon", "Hyena", "Cheetah", "Meerkat",
    "Warthog", "Tapir", "Okapi"
  ]
  
  print(logo)
  chosen_word = random.choice(word_list).lower()
  lengt_word = len(chosen_word)
  USER_LIVES = 6
  MAX_HINTS = 2
  display: str = []

  for letter in chosen_word:
    display += '_'
  
  print("Guess this animal:")
  print(*display)
  print(' ')
  

  def hints(hints):
    while hints > 0:
      random_hint = random.choice(chosen_word)

      if random_hint not in display:
        for position in range(lengt_word):
          letter = chosen_word[position]
          if random_hint == letter:
            display[position] = random_hint
      
        print(*display)
        print(f'you have {hints -1} hints left \n')
        break
      else:
        continue
    


  while '_' in display:
    user_guess: str = input('Enter your guess or type hint(for a hint): ').lower()

    if user_guess == 'hint':
      if MAX_HINTS == 0:
        print(f'you are out of hints \n')
        continue

      hints(hints= MAX_HINTS)
      MAX_HINTS += -1
      continue


    #validate user input
    try:
      if float(user_guess):
        print('Please enter a valid character \n')
        continue
    except ValueError:
      if user_guess in display:
        print(f"you have already guessed the word: {user_guess} \n")
        continue

    #check if user is right
    for position in range(lengt_word):
      letter = chosen_word[position]
      if user_guess == letter:
        display[position] = letter 

    #check if user is wrong
    if user_guess not in chosen_word:
      USER_LIVES += -1
      print(f'wrong answers, you got {USER_LIVES} lives left.')
    
    print(*display)

    #check if user won
    if '_' not in display:
      print(f"You won the game! \n")
      break

    #check if user lost
    print(f'{stages[USER_LIVES]} \n')
    if USER_LIVES <= 0:
      print(f"You lost the game, the word was {chosen_word} \n")
      break

  continue_game()

want_to_play = True
while want_to_play == True:
  hangman()