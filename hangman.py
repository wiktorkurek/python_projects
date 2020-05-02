import random

print("H A N G M A N")
words_list = ['python', 'java', 'kotlin', 'javascript']
computer_choice = random.choice(words_list)
player_letters = []
word = set(computer_choice)
lives = 8
while True:
    print('Type "play" to play the game, "exit" to quit: ')
    choice = input()
    if choice == "play":
        while lives >0:
            print()
            for letter in computer_choice:
                if letter in word:
                    print('-', end='')
                else:
                    print(letter, end='')
            print()
            player_letter = input("Input a letter: ")
            if len(player_letter) != 1:
                print("You should print a single letter")
                continue
            if player_letter.isalpha():
                if player_letter.isupper():
                    print("It is not an ASCII lowercase letter")
                    continue
                if player_letter not in player_letters:
                    player_letters.append(player_letter)
                else:
                    print("You already typed this letter")
                    continue
                if player_letter in word:
                    word.remove(player_letter)
                else:
                    print("No such letter in the word")
                    lives -= 1
                if player_letters == set(computer_choice):
                    print("You guessed the word", computer_choice)
                    print("You survived!")
                    break
            else:
                print("It is not an ASCII lowercase letter")
        else:
            print("You are hanged!")
    elif choice == "exit":
        break
    else:
        continue