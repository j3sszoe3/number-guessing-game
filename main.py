from random import randint

#set initial parameters for number of turns/lives
easy_turns = 10
hard_turns = 5

def validate_answer(user_guess, answer, number_of_turns):
  '''function to compare user input with randomly generated integer'''
  if user_guess > answer:
    print("Too high.")
    return number_of_turns -1
  elif user_guess < answer:
    print("Too low.")
    return number_of_turns - 1
  else:
    print(f"Correct! The answer was {answer}.")
  
def set_difficulty():
  '''sets number of turns based on user input'''
  level = input("Choose your difficulty, type 'easy' or 'hard': ")
  if level == "easy":
    return easy_turns
  else:
    return hard_turns

def game_play():
  '''function with while loop to allow the user to keep guessing until the run out of lives/guess correctly'''
  print("Welcome to the number guessing game!")
  print("I am thinking of a random number between 1 and 100.")
  answer = randint(1, 100)

  user_guess = 0
  number_of_turns = set_difficulty()

  while user_guess != answer:
    print(f"You have {number_of_turns} turns remaining.")
    user_guess = int(input("Make a guess: "))

    number_of_turns = validate_answer(user_guess, answer, number_of_turns)

    if number_of_turns == 0:
      print("You lost the game.")
      return
    elif user_guess != answer:
      print("Guess again.")

game_play()
