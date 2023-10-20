import sys
import random
from functools import partial
from sudoku import Sudoku
from PySide6.QtWidgets import *
from main_window import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.menu_new.triggered.connect(self.new_game)
        self.ui.menu_open_file.triggered.connect(self.open_file)
        self.line_edits = [[None for i in range(9)] for j in range(9)]
        for i in range(9):
            for j in range(9):
                new_cell = QLineEdit()
                self.ui.grid_layout.addWidget(new_cell, i, j)
                new_cell.textChanged.connect(partial(self.validation, i, j))
                self.line_edits[i][j] = new_cell

        self.new_game()
        for i in range(9):
            for j in range(9):
                self.line_edits[i][j].textChanged.connect(self.check)

    def open_file(self):
        file_path = QFileDialog.getOpenFileName(self, "Open file...")[0]
        f = open(file_path, "r")
        big_text = f.read()
        rows = big_text.split("\n")
        puzzle_board = [[None for i in range(9)] for j in range(9)]
        for i in range(len(rows)):
            cells = rows[i].split(" ")
            for j in range(len(cells)):
                puzzle_board[i][j] = int(cells[j])

        for i in range(9):
            for j in range(9):
                self.line_edits[i][j].setReadOnly(False)
                if puzzle_board[i][j] != 0:
                    self.line_edits[i][j].setText(str(puzzle_board[i][j]))
                    self.line_edits[i][j].setReadOnly(True)
                else:
                    self.line_edits[i][j].setText("")

    def new_game(self):
        puzzle = Sudoku(3, seed=random.randint(1, 1000)).difficulty(0.5)
        for i in range(9):
            for j in range(9):
                self.line_edits[i][j].setReadOnly(False)
                if puzzle.board[i][j] is not None:
                    self.line_edits[i][j].setText(str(puzzle.board[i][j]))
                    self.line_edits[i][j].setReadOnly(True)
                else:
                    self.line_edits[i][j].setText("")

    def check(self):
        for i in range(9):
            for j in range(9):
                self.line_edits[i][j].setStyleSheet("background-color: white")
            
                number1 = self.line_edits[i][j].text()
            
                # Check if the entered number is within the valid range (1-9)
                if number1 not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                    self.line_edits[i][j].setStyleSheet("background-color: red")
                    continue  # Continue checking other cells

                if not self.check_row(i, j, number1) or not self.check_column(i, j, number1) or not self.check_square(i, j, number1):
                    continue  # Continue checking other cells
        return True

    def check_row(self, i, j, number):
        for k in range(9):
            if k != j and self.line_edits[i][k].text() == number:
                self.line_edits[i][j].setStyleSheet("background-color: red")
                return False
        return True

    def check_column(self, i, j, number):
        for k in range(9):
            if k != i and self.line_edits[k][j].text() == number:
                self.line_edits[i][j].setStyleSheet("background-color: red")
                return False
        return True

    def check_square(self, i, j, number):
        square_start_row, square_start_col = 3 * (i // 3), 3 * (j // 3)
        for m in range(square_start_row, square_start_row + 3):
            for n in range(square_start_col, square_start_col + 3):
                if m != i and n != j and self.line_edits[m][n].text() == number:
                    self.line_edits[i][j].setStyleSheet("background-color: red")
                    return False
        return True

    def validation(self, i, j, text):
        if text not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            self.line_edits[i][j].setText("")
        
        if self.check() and all(self.line_edits[k][l].text() for k in range(9) for l in range(9)):
            msg_box = QMessageBox()
            msg_box.setText("You win!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
