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
    draws = inputs[0].split(',')
    draws = [int(x) for x in draws]
    boarddata = inputs[2:]
    entries = [words for segments in boarddata for words in segments.split()]
    entries = [int(x) for x in entries]
    chunks = [entries[i:i+25] for i in range(0, len(entries), 25)]
    boards = []
    for i in chunks: 
        boards.append(board(boarddata=i, drawdata=draws))
    return draws, boards

d, b = parser(tmp)

numbermoves = [x.play() for x in b]

ind = numbermoves.index(min(numbermoves))
winningboard = b[ind]

winningboard.boardstate, winningboard.check

state, check, num = winningboard.boardstate, winningboard.check, winningboard.winsafter
unmarked = state[check == 0]
score = sum(unmarked) * d[num-1]

# part 2
ind = numbermoves.index(max(numbermoves))
losingboard = b[ind]
state, check, num = losingboard.boardstate, losingboard.check, losingboard.winsafter
unmarked = state[check == 0]
score = sum(unmarked) * d[num-1]
