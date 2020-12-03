from tkinter import *
from random import randint

PIECE_I = [
    [True, True, True, True]
]

PIECE_O = [
    [True, True],
    [True, True]
]

PIECE_J = [
    [True, False, False],
    [True, True, True]
]

PIECE_L = [
    [False, False, True],
    [True, True, True]
]

PIECE_T = [
    [False, True, False],
    [True, True, True]
]

PIECE_S = [
    [False, True, True],
    [True, True, False]
]

PIECE_Z = [
    [True, True, False],
    [False, True, True]
]

PIECES = [PIECE_I, PIECE_J, PIECE_L, PIECE_O, PIECE_S, PIECE_T, PIECE_Z]
COLORS = ["orange", "red", "yellow", "green", "magenta", "cyan", "pink"]


class Game(Canvas):
    def __init__(self, master, **options):
        master.bind("<Key>", self.keyBinds)
        super().__init__(master, **options)

        class Data:
            pass

        self.data = Data()

        self.data.ROWS = 15
        self.data.COLUMNS = 10

        self.start()
        self.grid()
        self.animation()

    def start(self):
        self.setBoard()
        self.data.score = 0
        self.data.isGG = False
        self.setPiece()
        self.redraw()

    def redraw(self):
        self.delete("all")
        self.draw()

    def draw(self):
        self.data.cel = self.data.CELLS
        self.drawBoard()
        self.drawPiece()
        text = "Score: " + str(self.data.score) if not self.data.isGG else "Score: " + str(
            self.data.score) + " | Game Over!"
        self.create_text(200, 25, text=text)

    def drawBoard(self):
        board = self.data.board
        for row in range(len(board)):
            for column in range(len(board[0])):
                color = board[row][column]
                self.drawCell(row, column, color)

    def drawCell(self, row, column, color, flag=False):
        board = self.data.board
        indent = 50
        size = 30

        x1 = indent + column * size
        y1 = indent + row * size

        x2 = x1 + size
        y2 = y1 + size

        if not flag:
            c = self.create_rectangle(x1, y1, x2, y2, fill=color, width=2)
            self.data.cel[int(row)][int(column)] = c
        else:
            self.itemconfig(self.data.cel[int(row)][int(column)], fill=color)

    def setBoard(self):
        rows = self.data.ROWS
        columns = self.data.COLUMNS
        board = []
        cells = []

        for r in range(rows):
            row = []
            cell_row = []
            for c in range(columns):
                row.append("white")
                cell_row.append(None)
            board.append(row)
            cells.append(cell_row)

        self.data.board = board
        self.data.CELLS = cells

    def setPiece(self):
        pIndex = randint(0, 6)
        self.data.fPiece = PIECES[pIndex]
        self.data.fPieceColor = COLORS[pIndex]
        self.data.fPieceRow = 0
        self.data.fPieceColumn = self.data.COLUMNS / 2 - len(self.data.fPiece[0]) / 2

    def drawPiece(self):
        board = self.data.board
        fPiece = self.data.fPiece
        for row in range(len(fPiece)):
            for column in range(len(fPiece[0])):
                if fPiece[row][column]:
                    self.drawCell(self.data.fPieceRow + row, self.data.fPieceColumn + column,
                                  self.data.fPieceColor, flag=True)

    def movePiece(self, row, column):
        self.data.fPieceRow += row
        self.data.fPieceColumn += column
        if self.isLegal():
            return True
        else:
            self.data.fPieceRow -= row
            self.data.fPieceColumn -= column
            return False

    def rotatePiece(self):
        fPiece = self.data.fPiece
        PieceRow = self.data.fPieceRow
        PieceColumn = self.data.fPieceColumn
        rPiece = []

        for column in range(len(fPiece[0]) - 1, -1, -1):
            rows = []
            for row in range(len(fPiece)):
                rows.append(fPiece[int(row)][int(column)])
            rPiece.append(rows)

        self.data.fPiece = rPiece
        if not self.isLegal():
            self.data.fPiece = fPiece

    def placePiece(self):
        board = self.data.board
        fPiece = self.data.fPiece
        for row in range(len(fPiece)):
            for column in range(len(fPiece[0])):
                if fPiece[row][column]:
                    board[int(self.data.fPieceRow + row)][int(self.data.fPieceColumn + column)] = \
                        self.data.fPieceColor

    def isLegal(self):
        board = self.data.board
        rows = self.data.ROWS
        cols = self.data.COLUMNS
        fPiece = self.data.fPiece

        for row in range(len(fPiece)):
            for col in range(len(fPiece[0])):
                if fPiece[row][col]:
                    pieceRow = self.data.fPieceRow + row
                    pieceCol = self.data.fPieceColumn + col
                    if pieceRow >= rows or pieceRow < 0:
                        return False
                    if pieceCol >= cols or pieceCol < 0:
                        return False
                    if self.data.board[int(pieceRow)][int(pieceCol)] != "white":
                        return False

        return True

    def removeRow(self):
        board = self.data.board
        availableIndex = len(board) - 1
        score = 0

        for row in range(len(board) - 1, -1, -1):
            notFull = False
            newRow = []
            for col in range(len(board[0])):
                if board[row][col] == "white":
                    notFull = True

            if notFull:
                for color in board[row]:
                    newRow.append(color)
                board[availableIndex] = newRow
                availableIndex -= 1
            else:
                score += 1

        self.data.score += score ** 2

    def keyBinds(self, event):
        if event.keysym == "Up":
            self.rotatePiece()
        elif event.keysym == "Down":
            self.movePiece(1, 0)
        elif event.keysym == "Right":
            self.movePiece(0, 1)
        elif event.keysym == "Left":
            self.movePiece(0, -1)
        elif event.keysym == "n":
            self.setPiece()
        elif event.keysym == "r":
            self.start()
        self.redraw()

    def animation(self):
        if not self.movePiece(1, 0):
            self.placePiece()
            if not self.data.isGG:
                self.setPiece()
            if not self.isLegal():
                self.data.isGG = True

        self.removeRow()
        self.redraw()
        delay = 500
        self.after(delay, self.animation)


if __name__ == '__main__':
    root = Tk()
    root.title("Tetris")
    game = Game(root, width=400, height=600, bg="white")
    root.mainloop()
