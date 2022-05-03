# write your code here
#cells = list(input("Enter cells: ", ))
cells = list("         ")
cell_value = 'O'
empty_cells = len([x for x in cells if x == " "])

def print_board():
    print("---------")
    j = 0
    for i in range(len(cells)):
        j += 1
        if j % 3 == 1:
            print("|", end=" ")
        # if j % 3 == 2:
        #     print("|")

        print(cells[i], end=" ")
        if i == 2 or i == 5 or i == 8:
            print("|")
            # print()
    print("---------")


#print_board()


def fill_cell(new_cell, cells):
    if new_cell[0] == 1 and new_cell[1] == 1:
        i = 0
        # print("isempty:", is_empty(i))
        return is_empty(i)
    elif new_cell[0] == 1 and new_cell[1] == 2:
        i = 1
        return is_empty(i)
    elif new_cell[0] == 1 and new_cell[1] == 3:
        i = 2
        return is_empty(i)
    elif new_cell[0] == 2 and new_cell[1] == 1:
        i = 3
        return is_empty(i)
    elif new_cell[0] == 2 and new_cell[1] == 2:
        i = 4
        return is_empty(i)
    elif new_cell[0] == 2 and new_cell[1] == 3:
        i = 5
        return is_empty(i)
    elif new_cell[0] == 3 and new_cell[1] == 1:
        i = 6
        return is_empty(i)
    elif new_cell[0] == 3 and new_cell[1] == 2:
        i = 7
        return is_empty(i)
    elif new_cell[0] == 3 and new_cell[1] == 3:
        i = 8
        return is_empty(i)


def is_empty(i):
    # cell_value = 'X'
    if cells[i] == " " or cells[i] == "_":
        global cell_value
        cell_value = 'O' if cell_value == 'X' else "X"
        cells[i] = cell_value


        #print_board()
        return True
    else:
        return False


def whowon(coin):
    if (cells[0] == cells[1] == cells[2] == coin):
        return True
    elif (cells[3] == cells[4] == cells[5] == coin):
        return True
    elif (cells[6] == cells[7] == cells[8] == coin):
        return True
    elif (cells[0] == cells[3] == cells[6] == coin):
        return True
    elif (cells[1] == cells[4] == cells[7] == coin):
        return True
    elif (cells[2] == cells[5] == cells[8] == coin):
        return True
    elif (cells[0] == cells[4] == cells[8] == coin):
        return True
    elif (cells[0] == cells[1] == cells[2] == coin):
        return True
    elif (cells[2] == cells[4] == cells[6] == coin):
        return True
    else:
        return False


print_board()
while (True):

    input_ = input("Enter the coordinates: ", ).split()
    # print("input:", input_)
    if len(input_) == 1:
        if not isinstance(input_[0], int):
            print("You should enter numbers!")
    elif len(input_) == 2:
        # print("cc:", isinstance(int(input_[0]), int))
        if isinstance(int(input_[0]), int) and isinstance(int(input_[1]), int):
            #print("newcell")
            new_cell = [int(input_[0]), int(input_[1])]
            if new_cell[0] < 1 or new_cell[0] > 3 or new_cell[1] < 1 or new_cell[1] > 3:
                print("Coordinates should be from 1 to 3!")
            elif fill_cell(new_cell, cells):
                print_board()
                if any([whowon("X"), whowon("O")]):
                    print(cell_value,"wins")
                    break
                elif len([x for x in cells if x == " "]) == 0:
                    print("Draw")
                    break
            else:
                print("This cell is occupied! Choose another one!")
        else:
            print("You should enter numbers!")
