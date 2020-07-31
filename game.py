import random
name = input("Enter your name: ")
print("Hello, " + name + "\n")
score = 0
ratings = open("rating.txt", "r")
for line in ratings:
    if name == line.split()[0]:
        score = line.split()[1]
    else:
        score = 0

user_options = input()
print("Okay, let's start")
user_options_list = user_options.split(",")

if len(user_options_list) < 3:
    options = ["rock", "paper", "scissors"]
else:
    options = user_options_list[::]

while True:
    user_input = input()
    if user_input == "!rating":
        print("Your rating: ", score)
    if user_input == "!exit":
        print("Bye!")
        break
    if user_input not in options:
        print("Invalid input")
        continue
    else:
        computer_choose = random.choice(options)
        user_index = options.index(user_input)
        center_index = len(options) // 2
        n = center_index - user_index
        list_centered = (options[-n:] + options[:-n])
        computer_index = list_centered.index(computer_choose)
        if computer_index == center_index:
            print("There is a draw " + computer_choose)
            score += 50
        elif computer_index < center_index:
            print("Well done. Computer chose " + computer_choose + " and failed")
            score += 100
        else:
            print("Sorry, but computer chose " + computer_choose)
ratings.close()