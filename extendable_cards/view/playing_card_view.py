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

    """
    def display_card(self, context):
        
        Takes a basic card, the top left's coordinates's dx, dy
        the height and width of the card an an image to display (not supported)
        draws card at given coordinates
        
        dx = context['lx']
        dy = context['ty']
        rx = context['rx']
        by = context['by']

        w = rx - dx
        h = by - dy

        if self.drawn:
            if self.hidden:
                self.outline.setFill("white")
                self.hidden = False
            self.move_display(context)
            return False

        left_p = Point(dx,dy)
        right_p = Point(dx+w, dy+h)
        outline = Rectangle(left_p, right_p)
        outline.setFill("white")

        if self.suit == "<>" or self.suit == "<3":
            color = "red"
        else:
            color = "black"

        suit_p = Point(dx+w/2.0, dy+h/2.0)
        suit_t = Text(suit_p, self.suit)
        suit_t.setTextColor(color)

        num_pl = Point(dx+max(w/5.0, 0.5), dy+h-max(h/5.0, 0.5))
        num_tl = Text(num_pl, "{0}\n{1}".format(self.number, self.suit))
        num_tl.setTextColor(color)

        num_pr = Point(dx+w-max(w/5.0, 0.5), dy+max(h/5.0,0.5))
        num_tr = Text(num_pr, "{0}\n{1}".format(self.number, self.suit))
        num_tr.setTextColor(color)

        outline.draw(self.win)
        suit_t.draw(self.win)
        num_tl.draw(self.win)
        num_tr.draw(self.win)

        self.outline = outline
        self.suit_t = suit_t
        self.num_l = num_tl
        self.num_r = num_tr
        self.drawn = True
        self.visible = True


    def undisplay(self):
        if not self.drawn or not self.visible:
            return False

        self.outline.undraw()
        self.suit_t.undraw()
        self.num_l.undraw()
        self.num_r.undraw()
        self.drawn = False


    def display_back(self, context):
        dx = context['lx']
        dy = context['ty']
        rx = context['rx']
        by = context['by']

        w = rx - dx
        h = by - dy

        self.display_card(context)
        self.outline.setFill("red")

        self.outline.draw(self.win)

        self.visible = True
        self.hidden = True

    def move_display(self, context):
        self.outline.move(context['lx'], context['ty'])
        self.text.move(context['lx'], context['ty'])

        self.outline.draw()
        self.text.draw()
    """

def get_standard_playing_card_deck_view(graphwin):
    cards = get_standard_playing_card_deck()
    view_cards = []
    for card in cards:
        if hasattr(card, 'suit'):
            view_cards.append(PlayingCardView(card.suit, card.number, graphwin))
        else:
            view_cards.append(CardView(card.name, graphwin))

    return view_cards
