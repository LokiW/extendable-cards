from extendable_cards.lib.cards import Card
from extendable_cards.view.graphics import Rectangle, Point, Text

def draw_card(card, dx, dy, h, w, graphwin, image=None):
    """
    Takes a basic card, the top left's coordinates's dx, dy
    the height and width of the card an an image to display (not supported)
    draws card at given coordinates
    """
    left_p = Point(dx,dy)
    right_p = Point(dx+w, dy+h)
    outline = Rectangle(left_p, right_p)

    text_p = Point(dx+w/2, dy)
    card_t = Text(text_p, card.name)

    outline.draw(graphwin)
    card_t.draw(graphwin)
    return outline
