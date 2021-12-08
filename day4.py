import numpy as np
from random import shuffle
inp = list(range(1, 26))
test = np.ndarray((5,5), buffer=np.array(inp), dtype=int)

shuffle(inp)

check = np.ndarray((5,5), buffer = np.array([0] * 25), dtype = int)

class board:
    def __init__(self, boarddata, drawdata):
        self.boardstate = np.ndarray((5,5), buffer = np.array(boarddata), dtype=int)
        self.check = np.ndarray((5,5), buffer = np.array([0] * 25), dtype = int)
        self.winsafter = 0
        self.drawdata = drawdata
    def play(self):
        for i in self.drawdata:
            index = np.where(self.boardstate == i)
            if index[0].size == 0:
                self.winsafter += 1
            else:
                self.check[index[0][0], index[1][0]] = 1
                self.winsafter += 1
            # print(self.check)
            if 5 in np.sum(self.check, axis = 0) or 5 in np.sum(self.check, axis = 1):
                return self.winsafter

testboard = board(boarddata = list(range(1,26)), drawdata = inp)
testboard.play()

f = open("input.txt", "r")
tmp = f.read().splitlines()

from functools import reduce
from operator import add

def parser(inputs):
    draws = tmp[0]
    wot = tmp[2:20]
    boards = []
    buffer = []
    out = []
    for i in wot: 
        if i == '': 
            buf = reduce(add, buffer)
            boards.append(board(boarddata=buf, drawdata=draws))
            buffer = []
            out.append(buf)
        else: 
            buffer.append(i)
            print(buffer)
    return draws, boards

d, b = parser(wot)

numbermoves = [x.play() for x in b]
