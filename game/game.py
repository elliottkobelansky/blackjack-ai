import numpy as np

# TODO implement aces
CARDS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]#, 11]

class Hand:
    def __init__(self):
        self.hand = []
        for i in range(2):
            self.deal()

    def deal(self):
        self.hand.append(np.random.choice(CARDS))

    def sum(self):
        # aces = self.hand.count(11)
        # s = sum(self.hand)
        # if s > 21 and aces:
        #     for i in range(aces):
        #         if s > 21:
        #             return s
        #         else:
        #             s -= 10
        # else:
        #     return s
        return sum(self.hand)

    def is_bj(self):
        return True if self.sum() == 21 else False
    
    def is_bust(self):
        return True if self.sum() > 21 else False

class Game:
    def __init__(self, starting_cash):
        self.cash = starting_cash

    def deal(self):
        # d is dealer, p is player
        self.p = Hand()
        self.d = Hand()
        return

    def d_turn(self):
        # Dealer must stand on 17
        while self.d.sum() < 17:
            print('Dealer:', self.d.hand, self.d.sum(), 'hit')
            self.d.deal()
        print('Dealer:', self.d.hand, self.d.sum())
        return

    def p_turn(self, decision):
        # TODO eventually switch this to binary/numbered idk
        # TODO deal with blackjacks
        if decision == 's':
            return True
        elif decision == 'h':
            self.p.deal()
            if self.p.is_bj() or self.p.is_bust():
                return True
            else:
                return False

    def payout(self):
        p = game.p.sum()
        d = game.d.sum()

        # Bet multiplied by this amount

        # Player busts
        if p > 21:
            return -1
        # Dealer busts (and player doesn't)
        elif d > 21:
            return 1
        # Player has more than dealer (no busts)
        elif p > d:
            return 1
        # Player has less than dealer
        elif p < d:
            return -1
        # Tie
        elif p == d:
            return 0


game = Game(500)
game.deal()
print(f'You: {game.p.hand}\nDealer: {["?", game.d.hand[1]]}\n')

x = False
while not x:
    dec = input('Decision: ')
    x = game.p_turn(dec)
    print('You:', game.p.hand, game.p.sum(), '\n') 
game.d_turn()
print(game.payout())



