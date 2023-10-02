
import sys
from random import randint
from functools import partial
from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtUiTools import QUiLoader

def about():
    msg_box=QMessageBox(windowTitle="About", text= "each player chooses their own token - an 'X' or an 'O' - and they take turns filling their own tokens into 3x3 squares. The winner is the one who is the first to place his signs vertically, horizontally or diagonally without empty spaces")
    msg_box.exec()

def clear():
    global player
    for i in range(3):
        for j in range(3):
            buttons[i][j].setText("")
            buttons[i][j].setStyleSheet("color: gray; background-color: lightgray")
            player=1    

def new_game():
    global X_score
    global O_score
    global ties
    X_score = O_score = ties = 0
    main_window.btn_x_score.setText("X_score: " + str(X_score))
    main_window.btn_o_score.setText("O_score: " + str(O_score))
    main_window.btn_ties.setText("Ties: " + str(ties))
    

def check():
    global X_score
    global O_score
    global ties
    for i in range(3):
        if buttons[i][0].text()=="X" and buttons[i][1].text()=="X" and buttons[i][2].text()=="X":
            msg_box=QMessageBox(text="Player1 wins")
            msg_box.exec()
            X_score += 1
            main_window.btn_x_score.setText("X_Score: " + str(X_score))
            return

        elif buttons[0][i].text()=="X" and buttons[1][i].text()=="X" and buttons[2][i].text()=="X":
            msg_box=QMessageBox(text="Player1 wins")
            msg_box.exec()
            X_score += 1
            main_window.btn_x_score.setText("X_Score: " + str(X_score))
            return

        elif buttons[i][0].text()=="O" and buttons[i][1].text()=="O" and buttons[i][2].text()=="O":
            msg_box=QMessageBox(text="Player2 wins")
            msg_box.exec()
            O_score += 1
            main_window.btn_o_score.setText("O_Score: " + str(O_score))
            return

        elif buttons[0][i].text()=="O" and buttons[1][i].text()=="O" and buttons[2][i].text()=="O":
            msg_box=QMessageBox(text="Player2 wins")
            msg_box.exec()
            O_score += 1
            main_window.btn_o_score.setText("O_Score: " + str(O_score))
            return

    if buttons[0][0].text()=="X" and buttons[1][1].text()=="X" and buttons[2][2].text()=="X":
        msg_box=QMessageBox(text="Player1 wins")
        msg_box.exec()
        X_score += 1
        main_window.btn_x_score.setText("X_Score: " + str(X_score))
        return

    if buttons[0][2].text()=="X" and buttons[1][1].text()=="X" and buttons[2][0].text()=="X":
        msg_box=QMessageBox(text="Player1 wins")
        msg_box.exec()
        X_score += 1
        main_window.btn_x_score.setText("X_Score: " + str(X_score))
        return

    if buttons[0][0].text()=="O" and buttons[1][1].text()=="O" and buttons[2][2].text()=="O":
        msg_box=QMessageBox(text="Player2 wins")
        msg_box.exec()
        O_score += 1
        main_window.btn_o_score.setText("O_Score: " + str(O_score))
        return

    if buttons[0][2].text()=="O" and buttons[1][1].text()=="O" and buttons[2][0].text()=="O":
        msg_box=QMessageBox(text="Player2 wins")
        msg_box.exec()
        O_score += 1
        main_window.btn_o_score.setText("O_Score: " + str(O_score))
        return

    if buttons[0][0].text()!="" and buttons[0][1].text()!="" and buttons[0][2].text()!="" and buttons[1][0].text()!="" and buttons[1][1].text()!="" and buttons[1][2].text()!="" and buttons[2][0].text()!="" and buttons[2][1].text()!="" and buttons[2][2].text()!="":
        msg_box=QMessageBox(text="Tie!")
        msg_box.exec()
        Ties += 1
        main_window.btn_ties.setText("Ties: " + str(Ties))
        return

def play(row, col):
    global player
    if player==1:
        if buttons[row][col].text()=="":
            buttons[row][col].setText("X")
            buttons[row][col].setStyleSheet("color: orange; background-color: lightpink")
            if cpu==False:
                check()
                player=2
            elif cpu==True:
                while True:
                    row=randint(0,2)
                    col=randint(0,2)
                    if buttons[row][col].text()=="":
                        buttons[row][col].setText("O")
                        buttons[row][col].setStyleSheet("color: blue; background-color: lightblue")
                        check()
                        player=1
                        break
        else:
            msg_box=QMessageBox(windowTitle="error",text="choose an empty box")
            msg_box.exec()

    elif player==2:
        if buttons[row][col].text()=="":
            buttons[row][col].setText("O")
            buttons[row][col].setStyleSheet("color: blue; background-color: lightblue")
            check()
            player=1
        else:
            msg_box=QMessageBox(windowTitle="error",text="please choose empty box")
            msg_box.exec()

def player_player():
    global cpu
    cpu=False
    clear()
    new_game()

def player_cpu():
    global cpu
    cpu=True
    clear()
    new_game()

app = QApplication(sys.argv)

loader = QUiLoader()
main_window = loader.load("main_window.ui")
main_window.show()

player = 1
cpu=False
new_game()

buttons = [[main_window.btn_1,main_window.btn_2,main_window.btn_3 ],
         [main_window.btn_4, main_window.btn_5, main_window.btn_6],
         [main_window.btn_7, main_window.btn_8, main_window.btn_9]]

for i in range (3):
    for j in range(3):
        buttons[i][j].clicked.connect(partial(play, i, j))

main_window.btn_about.clicked.connect(about)
main_window.btn_turn.clicked.connect(new_game)
main_window.radioButton_p_p.pressed.connect(player_player)
main_window.radioButton_p_cpu.pressed.connect(player_cpu)

app.exec()