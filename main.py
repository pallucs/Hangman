import random
import hangman_words

chosen_word = random.choice(hangman_words.word_list)

from hangman_art import logo
print(logo)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

display = []
word_length = len(chosen_word)

for _ in range(word_length):
  display += '_'

print(display)

lives = 6

while '_' in display and lives > 0:
  print(lives)
  guess = input('guess a letter ').lower()

  if guess in display:
    print(f"You've already guessed {guess}")
  for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
      display[position] = letter

  if guess not in chosen_word:
    print(f"you guessed {guess} thats not in the word. you lose a life")
    lives -= 1
    if lives == 0:
      print('you lose')
      break
      
  if '_' not in display and lives > 0:
    print('you won')

  from hangman_art import stages
  print(stages[lives])
  






# def is_prime(num):
#   for n in range(2, num):
#     if num%n == 0:
#       print('Not Prime')
#       break
#   else:
#     print('Prime')

# num = 17
# is_prime(num)

# working_hr = [('kim', 400), ('pallu', 500), ('jivu', 600)]  

# def employee_month(working_hr):

#   current_max = 0
#   best_employee = ''
  
#   for employee, hours in working_hr:
#     if hours > current_max:
#       current_max = hours
#       best_employee = employee

#     else:
#       pass

#   return(best_employee, current_max)

# x, y = employee_month(working_hr)
# print(x)
# print(y)

# def employee_month(working_hr):
  
#   for name, hours in enumerate(working_hr):

#     current_max = hours
#     best_employee = name

#     if hours > current_max:
#       current_max = hours
#       best_employee = name
#     else:
#       pass

#   return best_employee, current_max

# name, hours = employee_month(working_hr)

# print(name)
# print(hours)


# find a ball under a cup

# from random import shuffle

# my_list = [1,2,3,4,5,6,7,8,9]
# print(my_list)

# def shuffle_list(list):
#   nlist = shuffle(list)
#   return nlist

# shuffled_list = shuffle_list(my_list)
# print(shuffled_list)