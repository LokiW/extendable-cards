from cards import Card, CardOrganizer

class PlayingCard(Card):
    def __init__(self, suit, number):
        name = "{0} {1}".format(number, suit)
        super(PlayingCard, self).__init__(name)
        
        self.suit = suit
        self.number = number

    def display_card(self, context=None):
        print '[{0} {1}]'.format(self.number, self.suit)


def get_standard_playing_card_deck(joker=True):
        c = []
        if joker:
            joker = Card("joker")
            c.extend([joker, joker])

        hearts = [PlayingCard("<3", n) for n in range(2, 11)]
        hearts.extend([PlayingCard("<3", "J"),
                        PlayingCard("<3", "Q"),
                        PlayingCard("<3", "K")])
        c.extend(hearts)

        spades = [PlayingCard("spade", n) for n in range(2,11)]
        spades.extend([PlayingCard("spade", "J"),
                        PlayingCard("spade", "Q"),
                        PlayingCard("spade", "K")])
        c.extend(spades)

        clubs = [PlayingCard("club", n) for n in range(2,11)]
        clubs.extend([PlayingCard("club", "J"),
                        PlayingCard("club", "Q"),
                        PlayingCard("club", "K")])
        c.extend(clubs)

        diamond = [PlayingCard("<>", n) for n in range(2, 11)]
        diamond.extend([PlayingCard("<>", "J"),
                        PlayingCard("<>", "Q"),
                        PlayingCard("<>", "K")])
        c.extend(diamond)
        return c



