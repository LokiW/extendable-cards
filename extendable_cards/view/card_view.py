from extendable_cards.view.view_utils import break_text
from extendable_cards.view.graphics import Rectangle, Point, Text


class CardView(object):
    def __init__(self, card, graphwin):
        self.card = card
        self.win = graphwin
        self.drawn = False
    
    
    def draw_card(self, dx, dy, h, w):
        """
        Takes a basic card, the top left's coordinates's dx, dy
        the height and width of the card an an image to display (not supported)
        draws card at given coordinates
        """
        left_p = Point(dx,dy)
        right_p = Point(dx+w, dy+h)
        outline = Rectangle(left_p, right_p)

        wraped_text = break_text(self.card.name, w)
        text_height = wraped_text.count('\n')*0.5
        text_p = Point(dx+w/2, dy+text_height)
        card_t = Text(text_p, wraped_text)
        card_t.setSize(9)

        corner_p = Point(dx, dy)
        one_p = Point(dx+1, dy+1)
        one_r = Rectangle(corner_p, one_p)

        outline.draw(self.win)
        card_t.draw(self.win)
        one_r.draw(self.win)

        self.outline = outline
        self.text = card_t
        self.drawn = True


