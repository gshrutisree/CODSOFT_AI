import math
import random

class Game:
    def __init__(self):
        self.b = [' ' for _ in range(9)]
        self.win = None

    def pb(self):
        for i in range(3):
            print('| ' + ' | '.join(self.b[i*3:i*3+3]) + ' |')

    @staticmethod
    def pbn():
        number_b = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for r in number_b:
            print('| ' + ' | '.join(r) + ' |')

    def am(self):
        return [i for i, s in enumerate(self.b) if s == ' ']

    def es(self):
        return ' ' in self.b

    def nes(self):
        return self.b.count(' ')

    def mm(self, s, l):
        if self.b[s] == ' ':
            self.b[s] = l
            if self.w(s, l):
                self.win = l
            return True
        return False

    def w(self, s, l):
        r = s // 3
        row = self.b[r*3:(r+1)*3]
        if all([spot == l for spot in row]):
            return True

        c = s % 3
        column = [self.b[c+i*3] for i in range(3)]
        if all([spot == l for spot in column]):
            return True

        if s % 2 == 0:
            d1 = [self.b[i] for i in [0, 4, 8]]
            if all([spot == l for spot in d1]):
                return True
            d2 = [self.b[i] for i in [2, 4, 6]]
            if all([spot == l for spot in d2]):
                return True
        return False


def minimax(p, d, m, g):
    if m:
        me = -math.inf
        bm = None
        for mv in g.am():
            g.mm(mv, 'X')
            e = minimax(p, d - 1, False, g)
            g.b[mv] = ' '
            me = max(me, e)
            if e == me:
                bm = mv
        return me if d == 0 else bm
    else:
        me = math.inf
        for mv in g.am():
            g.mm(mv, 'O')
            e = minimax(p, d - 1, True, g)
            g.b[mv] = ' '
            me = min(me, e)
        return me

def play():
    g = Game()
    g.pbn()
    while g.es():
        if g.nes() == 1:
            s = g.am()[0]
        else:
            if g.nes() == 9:
                s = random.choice(g.am())
            else:
                s = minimax(g.b, g.nes(), True, g)
        g.mm(s, 'X')
        g.pb()
        if g.win:
            print(g.win + " wins!")
            break
        if g.es():
            s = int(input("Choose a square to place 'O' (0-8): "))
            while s not in g.am():
                s = int(input("Choose a valid square (0-8): "))
            g.mm(s, 'O')
            g.pb()
            if g.win:
                print(g.win + " wins!")
                break
    if not g.es() and not g.win:
        print("It's a tie!")

play()

