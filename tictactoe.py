field = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
count = 0
index = None
new_field = [13, 23, 33, 12, 22, 32, 11, 21, 31]
def field_printing():
    print("---------")
    print("|", field[0], field[1], field[2], "|")
    print("|", field[3], field[4], field[5], "|")
    print("|", field[6], field[7], field[8], "|")
    print("---------")

while True:
    field_printing()
    coordinates = input("Enter the coordinates: ")
    coordinates = coordinates.replace(" ", "")
    move = list(coordinates)
    x, y = move[0], move[1]
    if not coordinates.isdigit():
        print("You should enter numbers!")
        continue
    elif int(x) not in [1, 2, 3] or int(y) not in [1, 2, 3]:
        print("Coordinates should be from 1 to 3!")
        continue
    for number in range(9):
        if int(coordinates) == new_field[number]:
            index = number
    if "X" in field[index] or "O" in field[index]:
        print("This cell is occupied! choose another one!")
        continue
    else:
        count += 1
        if count % 2 == 0:
            field[index] = "O"
        else:
            field[index] = "X"
        if (field[0] == "X" and field[1] == "X" and field[2] == "X") or \
            (field[3] == "X" and field[4] == "X" and field[5] == "X") or \
            (field[6] == "X" and field[7] == "X" and field[8] == "X") or \
            (field[0] == "X" and field[3] == "X" and field[6] == "X") or \
            (field[1] == "X" and field[4] == "X" and field[7] == "X") or \
            (field[2] == "X" and field[5] == "X" and field[8] == "X") or \
            (field[0] == "X" and field[4] == "X" and field[8] == "X") or \
            (field[2] == "X" and field[4] == "X" and field[6] == "X"):
            field_printing()
            print("X wins")
            break
        elif (field[0] == "O" and field[1] == "O" and field[2] == "O") or \
            (field[3] == "O" and field[4] == "O" and field[5] == "O") or \
            (field[6] == "O" and field[7] == "O" and field[8] == "O") or \
            (field[0] == "O" and field[3] == "O" and field[6] == "O") or \
            (field[1] == "O" and field[4] == "O" and field[7] == "O") or \
            (field[2] == "O" and field[5] == "O" and field[8] == "O") or \
            (field[0] == "O" and field[4] == "O" and field[8] == "O") or \
            (field[2] == "O" and field[4] == "O" and field[6] == "O"):
            field_printing()
            print("O wins")
            break
    if count == 9:
        field_printing()
        print("Draw")
        break