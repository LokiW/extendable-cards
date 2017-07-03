from extendable_cards.view.view_utils import break_text, CardDisplayObject
from extendable_cards.view.card_view import CardView
from extendable_cards.view.graphics import Rectangle, Point, Text
from extendable_cards.lib.playing_cards import PlayingCard, get_standard_playing_card_deck


class PlayingCardView(PlayingCard):
    def __init__(self, suit, number, graphwin):
        super(PlayingCardView, self).__init__(suit, number)
        self.win = graphwin
        suitnum = "{0}\n{1}".format(self.number, self.suit)
        if self.suit == "<>" or self.suit == "<3":
            color = "red"
        else:
            color = "black"
        specs = {"center": self.suit,
                "bottom_left": suitnum,
                "bottom_right": suitnum,
                "top_right": suitnum,
                "top_left": suitnum,
                "text_color": color}
        self.display = CardDisplayObject(specs, graphwin)        
    
    def display_card(self, context):
        self.display.display_card(context)

    def is_displayed(self):
        return self.display.is_displayed()

    def undisplay(self):
        self.display.undisplay()

    def display_back(self, context):
        self.display.display_back(context)


def get_standard_playing_card_deck_view(graphwin):
    cards = get_standard_playing_card_deck()
    view_cards = []
    for card in cards:
        if hasattr(card, 'suit'):
            view_cards.append(PlayingCardView(card.suit, card.number, graphwin))
        else:
            view_cards.append(CardView(card.name, graphwin))

    return view_cards
