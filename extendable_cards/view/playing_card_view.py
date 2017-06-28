from extendable_cards.view.view_utils import break_text
from extendable_cards.view.card_view import CardView
from extendable_cards.view.graphics import Rectangle, Point, Text


class PlayingCardView(CardView):
    def __init__(self, playing_card, graphwin):
        super(PlayingCardView, self).__init__(playing_card, graphwin)

    def draw_card(self, dx, dy, h, w):
        """
        Takes a basic card, the top left's coordinates's dx, dy
        the height and width of the card an an image to display (not supported)
        draws card at given coordinates
        """
        left_p = Point(dx,dy)
        right_p = Point(dx+w, dy+h)
        outline = Rectangle(left_p, right_p)

        suit_p = Point(dx+w/2.0, dy+h/2.0)
        suit_t = Text(suit_p, self.card.suit)

        num_pl = Point(dx+0.5, dy+h-0.5)
        num_tl = Text(num_pl, self.card.number)

        num_pr = Point(dx+w-0.5, dy+0.5)
        num_tr = Text(num_pr, self.card.number)

        outline.draw(self.win)
        suit_t.draw(self.win)
        num_tl.draw(self.win)
        num_tr.draw(self.win)

        self.outline = outline
        self.suit = suit_t
        self.num_l = num_tl
        self.num_r = num_tr
        self.drawn = True
