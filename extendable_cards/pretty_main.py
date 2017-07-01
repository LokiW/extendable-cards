from extendable_cards.view.graphics import GraphWin
from extendable_cards.view.game_view import GameOutline, PlayArea
from extendable_cards.lib.playing_cards import PlayingCardDeck
from extendable_cards.view.card_view import CardView, DeckBack
from extendable_cards.view.playing_card_view import PlayingCardView
from tkinter import Button
import pdb

SCREEN = {"height": 100, "width": 100}


def pretty_main():
    win = GraphWin("Extendable Cards", 100, 100)
    SCREEN["width"] = win.winfo_screenwidth() * 0.8
    SCREEN["height"] = win.winfo_screenheight() * 0.8
    #win.config(width=bigger_width, height=bigger_height)

    pc_b = Button(win, text="Standard Playing Card Deck", command=handle_standard_game(win))
    pc_b.pack()
    sm_b = Button(win, text="Sentinels of the Multiverse", command=handle_standard_game(win))
    sm_b.pack()

    win.getMouse()
    win.close()


def handle_standard_game(win):
    win.config(width=SCREEN["width"], height=SCREEN["height"])
    win_x = win.winfo_x()
    win_y = win.winfo_y()
    print win_x
    print win_y

    print win 
    game_outline = GameOutline(win, win_x, win_y, SCREEN['width'], SCREEN['height'])
    game_outline.display_outline_with_labels()

    cards = PlayingCardDeck()
    cards.shuffle()

    deck_card = DeckBack(win)
    discard_card = DeckBack(win)

    update_deck_display = True
    update_discard_display = True
    update_hand_display = True
    update_in_play_display = True

    while(True):
        if update_deck_display and not cards.deck_empty():
            #pdb.set_trace()
            p1, p2 = game_outline.get_area_points(PlayArea.DECK)
            deck_card.display_deck_back(p1, p2)
            update_deck_display = False
        elif update_deck_display:
            deck_card.undisplay()
            update_deck_display = False

        if update_discard_display and not cards.discard_empty():
            p1, p2 = game_outline.get_area_points(PlayArea.DISCARD)
            discard_card.display_deck_back(p1, p2)
            update_discard_display = False
        elif update_discard_display:
            discard_card.undisplay()
            update_discard_display = False

        if update_hand_display:
            game_outline.undisplay_hand_area()
            game_outline.display_hand_area()
            update_hand_display = False

        if update_in_play_display:
            game_outline.undisplay_play_area()
            game_outline.display_play_area()
            update_in_play_display = False


        mouse_point = win.getMouse()
        mouse_area = game_outline.get_area(mouse_point)
        if mouse_area == PlayArea.DECK:
            new_card = cards.draw(1)
            game_outline.add_to_hand_area(PlayingCardView(new_card[0], win))
            update_hand_display = True
            if cards.deck_empty:
                update_deck_display = True



    win.getMouse()
    print "playing card game"


def handle_sentinels_game(win):
    print "playing sentinels of the multiverse"




if __name__ == "__main__":
        pretty_main()
