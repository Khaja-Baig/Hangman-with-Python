# # ///### HANGMAN-----   ////
# from random import choice

# print("Welcome!!!\nReady to play Hangman:: :)")
# print("-------guessed the word------")

# hangman_pics = ['''
#  +---+
#      |
#      |
#      |
#     ===''',
#     '''
#  +---+
#  o   |
#      |
#      |
#     ===''','''
#  +---+
#  o   |
#  |   |
#      |
#     ===''','''
#  +---+
#  o   |
# /|   |
#      |
#     ===''','''
#  +---+
#  o   |
# /|\  |
#      |
#     ===''','''
#  +---+
#  o   |
# /|\  |
# /    |
#     ===''','''
#  +---+
#  o   |
# /|\  |
# / \  |
#     ===''']

# words = ['opposite']
# secret_word = choice(words)
# word_list = [l for l in secret_word]
# word_len = len(secret_word)
# blanks = "_"*word_len
# guessed = False
# c=0
# counter = 1
# lives = 6

# print(f"--------{blanks}-------->>>--------{hangman_pics[0]}")

# while not guessed:

#     input_letter  = input("----------guess the letter: please enter only one letter: ").lower()

#     if input_letter in secret_word:
#         for letter in secret_word:
#             if input_letter == letter:
#                 if input_letter in word_list:
#                     letter_index = word_list.index(letter)
#                     word_list[letter_index] = "_"
#                     blanks = "".join((blanks[:letter_index],input_letter,blanks[letter_index+1:]))
#                     c+=1
#     else:
#         lives-=1
#         if lives == 0:
#             print(f"---------oops...you lost------{hangman_pics[-1]}...Game Over..!!---------")
#             break
#         print(f"--------Wrong Guess....you have {lives} live(s) left--------{hangman_pics[counter]}")
#         counter+=1
    
#     if c == word_len:
#         guessed = True
#         print("-------WOW!!!....You Won....!!--------")
#         break
#     print(f"---------{blanks}-------you have {lives} live(s) left--------\n")
