from extendable_cards.view.graphics import GraphWin
from extendable_cards.view.card_view import CardView
from extendable_cards.view.playing_card_view import PlayingCardView
from extendable_cards.lib.cards import Card
from extendable_cards.lib.playing_cards import PlayingCard

def display():
    win = GraphWin()
    win.setCoords(0,0,10,10)
    c = Card("test card")
    cv = CardView(c, win)
    cv.draw_card(3, 4, 3, 2)

    pc = PlayingCard('<3', 4)
    pcv = PlayingCardView(pc, win)
    pcv.draw_card(6, 4, 3, 2)


    win.getMouse()
    win.close()


if __name__ == "__main__":
    display()
