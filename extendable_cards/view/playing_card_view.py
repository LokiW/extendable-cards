from extendable_cards.view.view_utils import break_text
from extendable_cards.view.card_view import CardView
from extendable_cards.view.graphics import Rectangle, Point, Text


class PlayingCardView(CardView):
    def __init__(self, playing_card, graphwin):
        super(PlayingCardView, self).__init__(playing_card, graphwin)

    def display_card(self, dx, dy, h, w):
        """
        Takes a basic card, the top left's coordinates's dx, dy
        the height and width of the card an an image to display (not supported)
        draws card at given coordinates
        """
        if self.drawn:
            return False

        if not hasattr(self.card, 'suit'):
            super(PlayingCardView, self).display_card(dx, dy, h, w)
            return True

        left_p = Point(dx,dy)
        right_p = Point(dx+w, dy+h)
        outline = Rectangle(left_p, right_p)
        outline.setFill("white")

        suit_p = Point(dx+w/2.0, dy+h/2.0)
        print self.card
        suit_t = Text(suit_p, self.card.suit)

        num_pl = Point(dx+max(w/5.0, 0.5), dy+h-max(h/5.0, 0.5))
        num_tl = Text(num_pl, self.card.number)

        num_pr = Point(dx+w-max(w/5.0, 0.5), dy+max(h/5.0,0.5))
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


    def undisplay(self):
        if not self.drawn:
            return False

        if not hasattr(self.card, 'suit'):
            super(PlayingCardView, self).undisplay()
            return True

        self.outline.undraw()
        self.suit.undraw()
        self.num_l.undraw()
        self.num_r.undraw()
        self.drawn = False
