import sys


class player:
    # player object is main object that hold information about players
    def __init__(self,txt_file,in_file):
        # formatting of players board
        with open(txt_file, "r") as f:
            board_unformatted = f.readlines()

        for i in range(10):
            board_unformatted[i] = board_unformatted[i].replace("\n", "").split(";")
        
        # reformatting battleships and patrol boats
        i = 0
        num_of_b = 1
        num_of_p = 1
        while i < 10:
            j = 0
            while j < 10:
                if board_unformatted[i][j] == "":
                    board_unformatted[i][j] = "-"

                if board_unformatted[i][j] == "B":
                    if j < 7 and board_unformatted[i][j+1] == "B"\
                            and board_unformatted[i][j+3] == "B":
                        for c in range(4):
                            board_unformatted[i][j+c] = "B" + str(num_of_b)
                        num_of_b += 1
                        j += 3
                        continue
                    else:
                        for c in range(4):
                            board_unformatted[i+c][j] = "B" + str(num_of_b)
                        num_of_b += 1

                if board_unformatted[i][j] == "P":
                    if i == 9:
                        board_unformatted[i][j+1] += str(num_of_p)
                        board_unformatted[i][j] += str(num_of_p)
                        num_of_p += 1
                        j += 1

                    elif j == 9:
                        board_unformatted[i+1][j] += str(num_of_p)
                        board_unformatted[i][j] += str(num_of_p)
                        num_of_p += 1

                    else:
                        if board_unformatted[i][j+1] == "P" and board_unformatted[i+1][j] != "P":
                            board_unformatted[i][j+1] += str(num_of_p)
                            board_unformatted[i][j] += str(num_of_p)
                            num_of_p += 1
                            j += 1

                        elif board_unformatted[i+1][j] == "P" and board_unformatted[i][j+1] != "P":
                            board_unformatted[i+1][j] += str(num_of_p)
                            board_unformatted[i][j] += str(num_of_p)
                            num_of_p += 1

                        else :
                            check = j
                            num_of_p_sts = 0
                            while check < 10 and board_unformatted[i][check] == "P":
                                num_of_p_sts += 1
                                check += 1
                        
                            if num_of_p_sts % 2 == 1:
                                board_unformatted[i+1][j] += str(num_of_p)
                                board_unformatted[i][j] += str(num_of_p)
                                num_of_p += 1

                            else :
                                board_unformatted[i][j+1] += str(num_of_p)
                                board_unformatted[i][j] += str(num_of_p)
                                num_of_p += 1
                                j += 1

                j += 1
            i += 1

        board = board_unformatted
        # reformatting of commands
        with open(in_file, "r") as f:
            commands = f.read().replace("\n","")[:-1].split(";")

        for i in range(len(commands)):
            commands[i] = commands[i].split(",")
        
        # definition of objects
        self.board = board
        self.commands = commands
        self.num_sunk_ships = {"B" : 0, "P" : 0}
        self.num_non_sunk_squares = {"C" : 5, "B1" : 4, "B2" : 4,
                                     "D" : 3, "S" : 3, "P1" : 2, 
                                     "P2" : 2, "P3" : 2, "P4" : 2,}
        self.hidden_board = [["-" for i in range(10)] for j in range(10)]

class RanOutOfCommands(Exception):
    # an exception for the case of player running out of moves
    pass

def print_hidden_board(player_one, player_two):
    # this function prints hidden boards and ship information of players 
    printable_string = "Player1's Hidden Board\t\tPlayer2's Hidden Board\n"
    printable_string += "  A B C D E F G H I J\t\t  A B C D E F G H I J\n"
    for i in range(10):
        printable_string += str(i+1)
        for j in range(10):
            printable_string += " " + player_one.hidden_board[i][j] if (i != 9 or j != 0)\
                else player_one.hidden_board[i][j]
                
        printable_string += " \t\t" + str(i+1)
        for j in range(10):
            printable_string += " " + player_two.hidden_board[i][j] if (i != 9 or j != 0)\
                else player_two.hidden_board[i][j]
        printable_string += "\n"
            
    printable_string += "\nCarrier\t\t" + ("-" if player_one.num_non_sunk_squares["C"] != 0 else "X")
    printable_string += "\t\t\t\tCarrier\t\t" + ("-" if player_two.num_non_sunk_squares["C"] != 0 else "X")
    printable_string += "\nBattleship\t" + ((player_one.num_sunk_ships["B"]*"X ") + ((2 - player_one.num_sunk_ships["B"])*"- "))[:-1]
    printable_string += "\t\t\t\tBattleship\t" + ((player_two.num_sunk_ships["B"]*"X ") + ((2 - player_two.num_sunk_ships["B"])*"- "))[:-1]
    printable_string += "\nDestroyer\t" + ("-" if player_one.num_non_sunk_squares["D"] != 0 else "X")
    printable_string += "\t\t\t\tDestroyer\t" + ("-" if player_two.num_non_sunk_squares["D"] != 0 else "X")
    printable_string += "\nSubmarine\t" + ("-" if player_one.num_non_sunk_squares["S"] != 0 else "X")
    printable_string += "\t\t\t\tSubmarine\t" + ("-" if player_two.num_non_sunk_squares["S"] != 0 else "X")
    printable_string += "\nPatrol Boat\t" + ((player_one.num_sunk_ships["P"]*"X ") + ((4 - player_one.num_sunk_ships["P"])*"- "))[:-1]
    printable_string += "\t\t\tPatrol Boat\t" + ((player_two.num_sunk_ships["P"]*"X ") + ((4 - player_two.num_sunk_ships["P"])*"- "))[:-1]
    return printable_string

def print_pone_turn(round_number):
    # this function prints player1's turn 
    printable_string = "\nPlayer1's Move\n\n"
    printable_string += "Round : " + str(round_number) + "\t\t\t\t\tGrid Size: 10x10\n\n"
    printable_string +=  print_hidden_board(player_one, player_two) + "\n\n"
    return printable_string

def print_ptwo_turn(round_number):
    # this function prints player2's turn
    printable_string = "\nPlayer2's Move\n\n"
    printable_string += "Round : " + str(round_number) + "\t\t\t\t\tGrid Size: 10x10\n\n"
    printable_string += print_hidden_board(player_one, player_two) + "\n\n"
    return printable_string
            
def player_miss(defender, row, column):
    # this function is called when a player has missed a ship
    defender.hidden_board[row][column] = "O"
    defender.board[row][column] = "O"

def player_hit(defender, row, column):
    # this function is called when a player has hit a ship
    ship_name = defender.board[row][column]
    defender.num_non_sunk_squares[ship_name] -= 1
    if defender.num_non_sunk_squares[ship_name] == 0 and (ship_name[0] == "P" or ship_name[0] == "B"):
        defender.num_sunk_ships[ship_name[0]] += 1
    defender.hidden_board[row][column] = "X"
    defender.board[row][column] = "X"

def check_commands(player, command):
    # function for checking if player have any moves left
    if len(player.commands) <= command:
        raise(RanOutOfCommands)
    
    else:
        return None

def player_turn(player, defender, command):
    # this function executes players turn
    did_not_finish = True
    # while loop checks for incorrect inputs then executes correct input
    while did_not_finish:    
        try:
            error_message = ""
            check_commands(player, command)
            demand_move = "Enter your move: " + ",".join(player.commands[command]) + "\n"
            print(demand_move[:-1])
            output_file.write(demand_move)
            # error checking
            if  len(player.commands[command]) < 2 or\
                    player.commands[command][0] == "" or\
                    player.commands[command][1] == "":
                command += 1
                raise(IndexError)

            if len(player.commands[command]) > 2 or\
                    player.commands[command][0] in allowed_letters or\
                    player.commands[command][1] in allowed_numbers:
                command +=1    
                raise(ValueError)

            if player.commands[command][0] not in allowed_numbers or\
                    player.commands[command][1] not in allowed_letters:
                command +=1
                raise(AssertionError)
            # unnecessary definitions to improve readability
            command_row = int(player.commands[command][0]) - 1
            command_column = allowed_letters_numarised[player.commands[command][1]]
            if  defender.board[command_row][command_column] == "X" or\
                    defender.board[command_row][command_column] == "O":
                command += 1
                raise(AssertionError)

            # execution portion
            if defender.board[command_row][command_column] != "-":
                    player_hit(defender, command_row, command_column)
                    did_not_finish = False

            else:
                player_miss(defender, command_row, command_column)
                did_not_finish = False

        except IndexError:
            error_message = "IndexError: player did not give x and y cordinates properly.\n"       
        
        except ValueError:
            error_message = "ValueError: player did not give the right values for the cordinates.\n"

        except AssertionError:
            error_message = "AssertionError: Invalid Operation.\n"
        
        except RanOutOfCommands:
            error_message = "kaBOOM: run for your life!\n" # since there isn't any defined error message
            did_not_finish = False

        except:
            error_message = "kaBOOM: run for your life!\n"

        finally:
            #printing of error message
            if error_message != "": 
                print(error_message[:-1])
                output_file.write(error_message)
        
    return command


output_file = open("Battleship.out", "w")
print("Battle of Ships Game")
output_file.write("Battle of Ships Game\n")
can_continue = True # this veriable is here as a placeholder for else block.
try:
    # checking for IOErrors
    faulty_inputs = []
    for i in range(1,5):
        # finding which inputs are corrupted.
        try:
            pone_txt = open(sys.argv[i], "r")
            pone_txt.close()
    
        except IOError:
            faulty_inputs.append(sys.argv[i])

    if len(faulty_inputs) != 0:
        raise(IOError)
    
    # general definitions
    allowed_numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    allowed_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    allowed_letters_numarised = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9}
    player_one = player(sys.argv[1], sys.argv[3])
    player_two = player(sys.argv[2], sys.argv[4])
    round =1
    pone_command = 0
    ptwo_command = 0

except IndexError:
    error_message = "IndexError: Program did not start with enough arguments\n"
    print(error_message[:-1])
    output_file.write((error_message))
    can_continue = False

except IOError:
    error_message = "IOError: input file(s) "
    for i in faulty_inputs:
        error_message += i + " "
    error_message += """is/are not reachable." or "IOError: input\n"""
    print(error_message[:-1])
    output_file.write(error_message)
    can_continue = False

except:
    error_message = "kaBOOM: run for your life!\n"
    print(error_message[:-1])
    output_file.write(error_message)
    can_continue = False

if can_continue:
    # while loop for running through commands
    while (pone_command < len(player_one.commands) and ptwo_command < len(player_two.commands)):
        # try part checks if commands are valid
        pone_turn_str = print_pone_turn(round)
        print(pone_turn_str[:-1])
        output_file.write(pone_turn_str)
        pone_command = player_turn(player_one, player_two, pone_command)
            
        ptwo_turn_str = print_ptwo_turn(round)
        print(ptwo_turn_str[:-1])
        output_file.write(ptwo_turn_str)
        ptwo_command = player_turn(player_two, player_one, ptwo_command)
                         
        # checking if game is finished
        num_none_sunk_squares_pone = 0
        num_none_sunk_squares_ptwo = 0
        for i in player_one.num_non_sunk_squares:
                num_none_sunk_squares_pone += player_one.num_non_sunk_squares[i]

        for i in player_two.num_non_sunk_squares:
            num_none_sunk_squares_ptwo += player_two.num_non_sunk_squares[i]

        # finishing the game
        if num_none_sunk_squares_pone == 0 and\
                num_none_sunk_squares_ptwo == 0:
            status = "It is a Draw!"
            break

        elif num_none_sunk_squares_pone == 0:
            status = "Player2 Wins!"
            break

        elif num_none_sunk_squares_ptwo == 0:
            status ="Player1 Wins!"
            break

        round += 1
        pone_command += 1
        ptwo_command += 1

    # checking if the game finished properly
    if num_none_sunk_squares_pone != 0  and\
            num_none_sunk_squares_ptwo != 0:
        status = "The game did not finish properly!"
            
    #final print that prints players boards and declares who has won
    final_string = status + "\n\n"
    final_string += "Final Information\n\n"
    final_string += "Player1's Board\t\t\t\tPlayer2's Board\n"
    final_string += "  A B C D E F G H I J\t\t  A B C D E F G H I J\n"
    for i in range(10):
        final_string += str(i+1)
        for j in range(10):
            final_string += " " + player_one.board[i][j][0] if (i != 9 or j != 0)\
                else player_one.board[i][j][0]
                
        final_string += " \t\t" + str(i+1)
        for j in range(10):
            final_string += " " + player_two.board[i][j][0] if (i != 9 or j != 0)\
                else player_two.board[i][j][0]
        final_string += "\n"
            
    final_string += "\nCarrier\t\t" + ("-" if player_one.num_non_sunk_squares["C"] != 0 else "X")
    final_string += "\t\t\t\tCarrier\t\t" + ("-" if player_two.num_non_sunk_squares["C"] != 0 else "X")
    final_string += "\nBattleship\t" + ((player_one.num_sunk_ships["B"]*"X ") + ((2 - player_one.num_sunk_ships["B"])*"- "))[:-1]
    final_string += "\t\t\t\tBattleship\t" + ((player_two.num_sunk_ships["B"]*"X ") + ((2 - player_two.num_sunk_ships["B"])*"- "))[:-1]
    final_string += "\nDestroyer\t" + ("-" if player_one.num_non_sunk_squares["D"] != 0 else "X")
    final_string += "\t\t\t\tDestroyer\t" + ("-" if player_two.num_non_sunk_squares["D"] != 0 else "X")
    final_string += "\nSubmarine\t" + ("-" if player_one.num_non_sunk_squares["S"] != 0 else "X")
    final_string += "\t\t\t\tSubmarine\t" + ("-" if player_two.num_non_sunk_squares["S"] != 0 else "X")
    final_string += "\nPatrol Boat\t" + ((player_one.num_sunk_ships["P"]*"X ") + ((4 - player_one.num_sunk_ships["P"])*"- "))[:-1]
    final_string += "\t\t\tPatrol Boat\t" + ((player_two.num_sunk_ships["P"]*"X ") + ((4 - player_two.num_sunk_ships["P"])*"- "))[:-1] 
    print(final_string)
    output_file.write(final_string)

output_file.close()