import random
import sys
from termcolor import colored
from nltk.corpus import words
import nltk
nltk.download('words')


def print_menu():
  print("Lets play wordle: ")
  print("Type a 5 letter word and hit enter!\n")  

def read_random_word():
  with open("words.txt") as f:
    words = f.read().splitlines()
    return random.choice(words)

print_menu()
nltk.data.path.append('/work/words')
word_list = words.words()
words_five = [word for word in word_list if len(word) == 5]

play_again = ""
while play_again != "q":
  #word = read_random_word()  ##Optional import from words.txt file
  word = random.choice(words_five)

  for attempt in range(1,7):
      guess = input().lower()
  
      sys.stdout.write('\x1b[1A')
      sys.stdout.write('\x1b[2K')
    
      for i in range(min(len(guess),5)):
        if guess[i] == word[i]:
          print(colored(guess[i],'green'), end="")
        elif guess[i] in word:
          print(colored(guess[i], 'yellow'), end="")
        else: 
          print(guess[i], end="")
      print()
  
      if guess == word:
  
        if attempt <= 2:
          message = "You are better than 99% of players! "
        elif attempt >2 and attempt <= 4:
          message = "You did a great job! "
        else:
          message = "You finally got it! think smarter the next time"
        print(colored(f" Congrats! You got the wordle in {attempt} attempts. {message} ", 'red'))
        break
      elif attempt == 6:
        print(f"Sorry the word was... {word} \n")
  play_again = input("Want to play again? type q to exit ")
  