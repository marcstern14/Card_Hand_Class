from ch07.positional_list import PositionalList

class CardHand:

    def __init__(self):
        self.hand = {'spades': [], 'hearts': [], 'clubs': [], 'diamonds': []}
        self.valid = {'spades': set(), 'hearts': set(), 'clubs': set(), 'diamonds': set()}
        self.r = {2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'}
        self.p = PositionalList()

    def add_card(self, r, s):
        new_card = (r, s)

        if s not in self.valid:
            raise KeyError('suit is not valid')

        if r not in self.r:
            raise ValueError(f'rank is not valid\nchoose from below:\n{self.r}')

        if r in self.valid[s]:
            raise ValueError('card is already in hand or has already been played')

        if s == 'spades':
            pos = self.p.add_first(new_card)

        if s == 'hearts':
            if len(self.hand['hearts']) > 0:
                pos = self.p.add_after(self.hand['hearts'][-1], new_card)
            elif len(self.hand['spades']) > 0:
                pos = self.p.add_after(self.hand['spades'][-1], new_card)
            else:
                pos = self.p.add_first(new_card)

        if s == 'clubs':
            if len(self.hand['clubs']) > 0:
                pos = self.p.add_after(self.hand['clubs'][-1], new_card)
            elif len(self.hand['hearts']) > 0:
                pos = self.p.add_after(self.hand['hearts'][-1], new_card)
            elif len(self.hand['spades']) > 0:
                pos = self.p.add_after(self.hand['spades'][-1], new_card)
            else:
                pos = self.p.add_first(new_card)

        if s == 'diamonds':
            pos = self.p.add_last(new_card)

        self.hand[s].append(pos)
        self.valid[s].add(r)

    def play(self, s):
        if s in self.hand:
            if not len(self.hand[s]) == 0:
                card = self.hand[s].pop()
                e = card.element()
                self.p.delete(card)
                return e

        if not self.p.is_empty():
            i = self.p.last()
            e = i.element()
            self.hand[e[1]].pop()
            self.p.delete(i)
            return e

        return 'hand is empty'

    def __iter__(self):
        for card in self.p:
            yield card.element()

    def all_of_suit(self, s):
        l = []
        for card in self.p:
            if card.element()[1] == s:
                l.append(card.element())
        return l

c = CardHand()
c.add_card(9, 'diamonds')
c.add_card('K', 'diamonds')
c.add_card(6, 'hearts')
c.add_card(10, 'spades')

a = c.all_of_suit('diamonds')
print(a)

p = c.play('clubs')
print(p)

a = c.all_of_suit('diamonds')
print(a)

p = c.play('clubs')
print(p)

p = c.play('clubs')
print(p)

p = c.play('clubs')
print(p)

p = c.play('clubs')
print(p)