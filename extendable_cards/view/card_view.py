from extendable_cards.view.view_utils import break_text
from extendable_cards.view.graphics import Rectangle, Point, Text


class CardView(object):
    def __init__(self, card, graphwin):
        self.card = card
        self.win = graphwin
        self.drawn = False
    
    
    def display_card(self, dx, dy, h, w):
        """
        Takes a basic card, the top left's coordinates's dx, dy
        the height and width of the card an an image to display (not supported)
        draws card at given coordinates
        """
        if self.drawn:
            return False

        left_p = Point(dx,dy)
        right_p = Point(dx+w, dy+h)
        outline = Rectangle(left_p, right_p)
        outline.setFill("white")

        wraped_text = break_text(self.card.name, w)
        text_height = wraped_text.count('\n')*0.5
        text_p = Point(dx+w/2, dy+text_height+max(h/5.0, 0.5))
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

    def is_displayed(self):
        return self.drawn

    def undisplay(self):
        if not self.drawn:
            return False

        self.text.undraw()
        self.outline.undraw()
        self.drawn = False


class DeckBack(object):
    def __init__(self, graphwin):
        self.win = graphwin
        self.drawn = False
        self.back = []

    def display_deck_back(self, p1, p2):
        if self.drawn:
            return False

        lx = min(p1.getX(), p2.getX())
        rx = max(p1.getX(), p2.getX())
        ty = min(p1.getY(), p2.getY())
        by = max(p1.getY(), p2.getY())

        lx = lx + (rx - lx)*0.1
        rx = rx - (rx - lx)*0.05

        ty = ty + (by - ty)*0.1
        by = by - (by - ty)*0.05

        x_unit = (rx - lx)/50.0
        y_unit = (by - ty)/50.0

        left_p1 = Point(lx+x_unit, ty+y_unit)
        right_p1 = Point(rx-3*x_unit, by-3*y_unit)
        bot1 = Rectangle(left_p1, right_p1)
        bot1.setFill("white")
        self.back.append(bot1)

        left_p2 = Point(lx+2*x_unit, ty+2*y_unit)
        right_p2 = Point(rx-2*x_unit, by-2*y_unit)
        bot2 = Rectangle(left_p2, right_p2)
        bot2.setFill("white")
        self.back.append(bot2)

        top_right_p = Point(lx+3*x_unit, ty+3*y_unit)
        top_left_p = Point(rx-x_unit, by-y_unit)
        top = Rectangle(top_left_p, top_right_p)
        top.setFill("red")
        self.back.append(top)

        for r in self.back:
            r.draw(self.win)
        self.drawn = True


    def undisplay(self):
        if not self.drawn:
            return False

        for r in self.back:
            r.undraw()
        self.drawn = False

    def is_displayed(self):
        return self.drawn
