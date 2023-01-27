#Это доска, отсчет идёт с левого нижнего угла.
theBoard = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '}

board_keys = []

for key in theBoard:
    board_keys.append(key)

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])


def game():
    turn = 'X'
    count = 0

    for i in range(10):
        printBoard(theBoard)
        print("Ваш ход," + turn + ".Куда ставим?")

        move = input()

        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print("Уже занято.\nКуда переместим?")
            continue

        # Проверять кто-то победил после 5 ходов
        if count >= 5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':
                printBoard(theBoard)
                print("\nКОНЕЦ.\n")
                print(" **** " + turn + " победил. ****")
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':
                printBoard(theBoard)
                print("\nКОНЕЦ.\n")
                print(" **** " + turn + " победил. ****")
                break
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':
                printBoard(theBoard)
                print("\nКОНЕЦ.\n")
                print(" **** " + turn + " победил. ****")
                break
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ':
                printBoard(theBoard)
                print("\nКОНЕЦ.\n")
                print(" **** " + turn + " победил. ****")
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ':
                printBoard(theBoard)
                print("\nКОНЕЦ.\n")
                print(" **** " + turn + " победил. ****")
                break
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ':
                printBoard(theBoard)
                print("\nКОНЕЦ.\n")
                print(" **** " + turn + " победил. ****")
                break
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ':
                printBoard(theBoard)
                print("\nКОНЕЦ.\n")
                print(" **** " + turn + " победил. ****")
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':
                printBoard(theBoard)
                print("\nКОНЕЦ.\n")
                print(" **** " + turn + " победил. ****")
                break

                # Если никто не победил, то ничья.
        if count == 9:
            print("\nИгра окончена.\n")
            print("Это ничья, братан!")

        # Каждый ход меняется игрок
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

            # Ну и в конце можно начать заново
    restart = input("{Еще сыграем?}?(Да/Нет)")
    if restart == "Да" or restart == "Нет":
        for key in board_keys:
            theBoard[key] = " "

        game()


if __name__ == "__main__":
    game()

input("Нажмите Enter для выхода!")