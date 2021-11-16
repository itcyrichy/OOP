import random
import types

class Fool:
    def __init__(self,n_players,*args,trump_card = 'random',**kwargs):
        card_suits = ['spades','clubs','hearts','diamonds']
        self.n_players = n_players
        self.trump_card = card_suits[random.randint(0,3)] if trump_card == 'random' else trump_card
        if self.trump_card == 'hearts':
            self._hearts = {'six_hearts':15,'seven_hearts':16,'eight_hearts':17,'nine_hearts':18,'ten_hearts':19,'jack_hearts':20,'queen_hearts':21,'king_hearts':22,'ace_hearts':23}
        else:
            self._hearts = {'six_hearts': 6, 'seven_hearts': 7, 'eight_hearts': 8, 'nine_hearts': 9, 'ten_hearts': 10, 'jack_hearts': 11, 'queen_hearts': 12,
                             'king_hearts': 13, 'ace_hearts': 14}
        if self.trump_card == 'spades':
            self._spades = {'six_spades':15,'seven_spades':16,'eight_spades':17,'nine_spades':18,'ten_spades':19,'jack_spades':20,'queen_spades':21,'king_spades':22,'ace_spades':23}
        else:
            self._spades = {'six_spades': 6, 'seven_spades': 7, 'eight_spades': 8, 'nine_spades': 9, 'ten_spades': 10, 'jack_spades': 11, 'queen_spades': 12,
                             'king_spades': 13, 'ace_spades': 14}
        if self.trump_card == 'clubs':
            self._clubs = {'six_clubs':15,'seven_clubs':16,'eight_clubs':17,'nine_clubs':18,'ten_clubs':19,'jack_clubs':20,'queen_clubs':21,'king_clubs':22,'ace_clubs':23}
        else:
            self._clubs = {'six_clubs': 6, 'seven_clubs': 7, 'eight_clubs': 8, 'nine_clubs': 9, 'ten_clubs': 10, 'jack_clubs': 11, 'queen_clubs': 12,
                             'king_clubs': 13, 'ace_clubs': 14}
        if self.trump_card == 'diamonds':
            self._diamonds = {'six_diamonds':15,'seven_diamonds':16,'eight_diamonds':17,'nine_diamonds':18,'ten_diamonds':19,'jack_diamonds':20,'queen_diamonds':21,'king_diamonds':22,'ace_diamonds':23}
        else:
            self._diamonds = {'six_diamonds': 6, 'seven_diamonds': 7, 'eight_diamonds': 8, 'nine_diamonds': 9, 'ten_diamonds': 10, 'jack_diamonds': 11, 'queen_diamonds': 12,
                             'king_diamonds': 13, 'ace_diamonds': 14}
        self.deck = self._clubs|self._diamonds|self._spades|self._hearts
        self.deck = random.sample([x for x in self.deck.items()],36)
    def rround(self):
        print('Начните игру')
        # if self.n_players<=6:
        #     for i in range(1,self.n_players+1):
        #         k=0
        #         globals()['self.player'+str(i)] = self.deck[k:6*i]
        #         k+=6
        # else:
        #     print('Too many players, game\'s impossible. Set another ammount of players')
        # self.deck = self.deck[k:]

    # def dealing_out_a_deck(self):
f = Fool(3)
if f.n_players > 6 or f.n_players < 1:
    print('Выберите кол-во игроков от 1-го до 6')
else:
    k = 0
    for i in range(1,f.n_players+1):
        setattr(Fool,'pl'+str(i),f.deck[k:i*6])
        k+=6
f.deck = f.deck[k:]
print(f.pl1,'\n',f.pl2,'\n',f.pl3,'\n',f.deck)




def real_round(self):
    bita=[]
    print(self.pl1,f'Козырь: {self.trump_card}')
    card1 = input('Выберите карту: ')
    bita.append(self.pl1.pop(int(card1)))

    print(self.pl2,f'Козырь: {self.trump_card}')
    card2 = input('Выберите карту или заберите ("забрать"): ')
    if card2 == 'забрать':
        self.pl2=self.pl2+bita
    else:
        bita = bita + self.pl2.pop(int(card2))
    try:
        print(self.pl3,f'Козырь: {self.trump_card}')
        card3 = input('Выберите карту или заберите ("забрать"): ')
        if card3 == 'забрать':
            self.pl3 = self.pl3 + bita
        else:
            bita = bita + self.pl3.pop(int(card3))
    except:
        pass

    try:
        print(self.pl4,f'Козырь: {self.trump_card}')
        card4 = input('Выберите карту или заберите ("забрать"): ')
        if card4 == 'забрать':
            self.pl4 = self.pl4 + bita
        elif card4 == 'пасс':
            pass
        else:
            bita = bita + self.pl4.pop(int(card4))
    except:
        pass

    try:
        print(self.pl5,print(f'Козырь: {self.trump_card}'))
        card5 = input('Выберите карту или заберите ("забрать"): ')
        if card5 == 'забрать':
            self.pl5 = self.pl5 + bita
        elif card5 == 'пасс':
            pass
        else:
            bita = bita + self.pl5.pop(int(card5))
    except:
        pass

    try:
        print(self.pl6,print(f'Козырь: {self.trump_card}'))
        card6 = input('Выберите карту или заберите ("забрать"): ')
        if card6 == 'забрать':
            self.pl6 = self.pl6 + bita
        elif card6 == 'пасс':
            pass
        else:
            bita = bita + self.pl6.pop(int(card6))
    except:
        pass




f.rround = types.MethodType(real_round, f)

f.rround()

print(f.pl1,'\n',f.pl2,'\n',f.pl3)
