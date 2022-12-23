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
    def __init__(self):
        self.deal()

    def deal(self):
        # d is dealer, p is player
        self.p = Hand()
        ####self.d = Hand()
        # This is the face up card that the player can see.
        ####self.dealer_card = self.d.hand[0]
        return

    def turn(self, decision):
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
        p = self.p.sum()
        d = self.d.sum()

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

INFO = []
def play(game):
    game.deal()
    # print(f'You: {game.p.hand}\nDealer: {["?", game.d.hand[1]]}\n')

    while True:
        dec = np.random.choice(('h', 's'))
        x = game.p.sum()
        a = game.turn(dec)
        INFO.append((x, dec))

        if a:
            break
    # print(game.p.hand, game.p.sum())

    # while game.d.sum() < 17:
    #     # print(game.d.hand, game.d.sum())
    #     game.d.deal()
    # print(game.d.hand, game.d.sum())

    # x.append(game.payout())
    return

if __name__ == "__main__":
    game = Game()
    for i in range(100000):
        play(game)
    [print(i) for i in INFO]

