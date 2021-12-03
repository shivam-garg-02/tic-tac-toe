import random


def drawBoard(board):
    print(" " + board[1] + " | " + board[2] + " | " + board[3])
    print("---+---+---")
    print(" " + board[4] + " | " + board[5] + " | " + board[6])
    print("---+---+---")
    print(" " + board[7] + " | " + board[8] + " | " + board[9])


def intro():
    print('\nWelcome to Tic Tac Toe!\n')
    print('Reference of numbering on the board')
    board = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    drawBoard(board)
    print('')


def choose():
    while(True):
        print("Do you wanna go first or second? (1/2)")
        choice = input()
        if choice == '1' or choice == '2':
            return int(choice)
        else:
            print("PLease enter either 1 or 2.")
            continue


def assignLetter(choice):
    if (choice == 1):
        print("Your letter is ' X ' and you are gonna go first!")
        return 'X'
    else:
        print("Your letter is ' O ' and you are gonna go second!")
        return 'O'


def returnTurn(playerLetter):
    if playerLetter == 'X':
        return 'player'
    else:
        return 'computer'


def returnLevel():
    print('What level would you like to play:')
    while(True):
        print('Easy: Type 1')
        print('Medium: Type 2')
        print('Hard: Type 3')
        level = input()
        if level == '1' or level == '2' or level == '3':
            return int(level)
        else:
            print('Please enter the correct input')


def isValid(position, board):
    if (board[position] != ' '):
        return False
    else:
        return True


def isFull(board):
    flag = True
    for i in range(9):
        if board[i+1] == ' ':
            flag = False
            break
    return flag


def insertLetter(letter, position, board):
    board[position] = letter


def isWin(board, letter):
    return ((board[7] == board[8] == board[9] and board[7] == letter) or
            (board[4] == board[5] == board[6] and board[4] == letter) or
            (board[1] == board[2] == board[3] and board[1] == letter) or
            (board[1] == board[4] == board[7] and board[1] == letter) or
            (board[2] == board[5] == board[8] and board[2] == letter) or
            (board[3] == board[6] == board[9] and board[3] == letter) or
            (board[1] == board[5] == board[9] and board[1] == letter) or
            (board[3] == board[5] == board[7] and board[3] == letter))


def personPlay(board, playerLetter):
    while True:
        print("Please select a position to place '", playerLetter, "' (1-9): ")
        move = input()
        if not move or not move.isnumeric():
            print("Please type a number.")
            continue
        else:
            move = int(move)
            if move > 0 and move < 10:
                if not isValid(move, board):
                    print("Sorry this place is occupied!")
                else:
                    insertLetter(playerLetter, move, board)
                    break
            else:
                print("Please type a number between 1 to 9.")
                continue


def minimax(board, depth, isMax, alpha, beta, playerLetter, compLetter):
    compScore = isWin(board, compLetter)
    playerScore = isWin(board, playerLetter)
    if compScore == True:
        return 10
    if playerScore == True:
        return -10
    if isFull(board):
        return 0
    if isMax:
        best = -1000
        for i in range(1, 10):
            if isValid(i, board):
                board[i] = compLetter
                best = max(best, minimax(board,
                                        depth + 1,
                                        not isMax,
                                        alpha,
                                        beta,
                                        playerLetter,
                                        compLetter) - depth)
                alpha = max(alpha, best)
                board[i] = ' '
                if alpha >= beta:
                    break
        return best
    else :
        best = 1000
        for i in range(1, 10) :		
            if isValid(i, board) :
                board[i] = playerLetter
                best = min(best, minimax(board,
                                        depth + 1,
                                        not isMax,
                                        alpha,
                                        beta,
                                        playerLetter,
                                        compLetter) + depth)
                beta = min(beta, best)
                board[i] = ' '
                if alpha >= beta:
                    break
        return best


def compPlay3(board, playerLetter, compLetter):
    bestVal = -1000
    bestMove = -1
    for i in range(1, 10):
        if isValid(i, board):
            board[i] = compLetter
            moveVal = minimax(board, 0, False, -1000, 1000, playerLetter, compLetter)
            board[i] = ' '
            if moveVal > bestVal:
                bestMove = i
                bestVal = moveVal
    print("Computer placed '", compLetter, "' at position ", bestMove, ".")
    insertLetter(compLetter, bestMove, board)
    return


def compPlay2(board, playerLetter, compLetter):
    possibleMoves = []
    for i in range(10):
        if board[i] == ' ':
            possibleMoves.append(i)
    possibleMoves.remove(0)
    winMove = False
    winOpp = False
    for move in possibleMoves:
        boardCopy = board.copy()
        insertLetter(compLetter, move, boardCopy)
        if isWin(boardCopy, compLetter):
            winMove = True
            break
    if winMove:
        print("Computer placed '", compLetter, "' at position move.")
        insertLetter(compLetter, move, board)
        return
    for move in possibleMoves:
        boardCopy = board.copy()
        insertLetter(playerLetter, move, boardCopy)
        if isWin(boardCopy, playerLetter):
            winOpp = True
            break
    if winOpp:
        print("Computer placed '", compLetter, "' at position move.")
        insertLetter(compLetter, move, board)
        return

    move = random.choice(possibleMoves)
    print("Computer placed '", compLetter, "' at position ", move, ".")
    insertLetter(compLetter, move, board)
    return


def compPlay1(board, compLetter):
    possibleMoves = []
    for i in range(10):
        if board[i] == ' ':
            possibleMoves.append(i)
    possibleMoves.remove(0)
    move = random.choice(possibleMoves)
    print("Computer placed '", compLetter, "' at position ", move, ".")
    insertLetter(compLetter, move, board)
    return


def main():
    intro()
    myBoard = [' ' for x in range(10)]
    myChoice = choose()
    print('')
    level = returnLevel()
    print('')
    playerLetter = assignLetter(myChoice)
    if playerLetter == 'X':
        compLetter = 'O'
    else:
        compLetter = 'X'
    print('')
    turn = returnTurn(playerLetter)
    while(True):
        # personPlay(myBoard, playerLetter)
        # drawBoard(myBoard)
        # if isWin(myBoard):
        #     print("Congratulations! You win!")
        #     break
        # elif isFull(myBoard):
        #     print("It is a tie!")
        #     break
        # else:
        #     print("Computer is thinking of a move.")
        #     time.sleep(1)
        #     compPlay(myBoard, playedComp)
        #     drawBoard(myBoard)
        #     if isWin(myBoard):
        #         print("Computer wins! Better luck next time.")
        #         break
        #     elif isFull(myBoard):
        #         print("It is a tie!")
        #         break
        #     else:
        #         continue
        if turn == 'player':
            personPlay(myBoard, playerLetter)
            print('')
            drawBoard(myBoard)
            print('')
            if isWin(myBoard, playerLetter):
                print("Congratulations! You won! :)")
                break
            elif isFull(myBoard):
                print("It's a tie! :(")
                break
            else:
                turn = 'computer'

        # elif turn == 'computer':
        #     print("Computer is thinking of a killer move.")
        #     time.sleep(2)
        #     compPlay(myBoard, playedComp, compLetter, playerLetter)
        #     drawBoard(myBoard)
        #     if isWin(myBoard):
        #         print("Lol computer won! You lost! :_)")
        #         break
        #     elif isFull(myBoard):
        #         print("It's a tie! :(")
        #         break
        #     else:
        #         turn = 'player'

        elif turn == 'computer':
            # print("Computer is thinking of a move.")
            if level == 3:
                compPlay3(myBoard, playerLetter, compLetter)
            elif level == 2:
                compPlay2(myBoard, playerLetter, compLetter)
            else:
                compPlay1(myBoard, compLetter)
            print('')
            drawBoard(myBoard)
            print('')
            if isWin(myBoard, compLetter):
                print("Computer won! You lost! :_(")
                break
            elif isFull(myBoard):
                print("It's a tie! :(")
                break
            else:
                turn = 'player'

    while(True):
        print("\nDo you wanna play again? (y/n)")
        playAgain = input()
        if playAgain.lower() == 'y':
            main()
            break
        elif playAgain.lower() == 'n':
            print('')
            break
        else:
            print("Please enter the correct input!")
            continue
    
main()