from extendable_cards.view.graphics import GraphWin
from extendable_cards.view.view_utils import draw_basic_card
from extendable_cards.lib.cards import Card

def display():
    win = GraphWin()
    win.setCoords(0,0,10,10)
    c = Card("test card")
    draw_basic_card(c, 3, 4, 3, 2, win)


    win.getMouse()
    win.close()


if __name__ == "__main__":
    display()
