from extendable_cards.lib.cards import CardController, CardOrganizer
from extendable_cards.view.graphics import GraphWin
from extendable_cards.view.game_outline import GameOutline
from extendable_cards.view.card_view import CardView, DeckBack, CardOrganizerDisplay
from extendable_cards.view.playing_card_view import PlayingCardView, get_standard_playing_card_deck_view
from tkinter import Button
import pdb

SCREEN = {"height": 100, "width": 100}


def visual_main():
    win = GraphWin("Extendable Cards", 100, 100)
    SCREEN["width"] = win.winfo_screenwidth() * 0.8
    SCREEN["height"] = win.winfo_screenheight() * 0.8

    win.config(width=SCREEN["width"], height=SCREEN["height"])

    pc_b = Button(win, text="Standard Playing Card Deck", command=lambda: pcd_game(win))
    pc_b.place(x=(SCREEN['width']/3.0), y=0)
    print SCREEN['width']/3

    sm_b = Button(win, text="Sentinels of the Multiverse", command=lambda: pcd_game(win))
    sm_b.place(x=(SCREEN['width']*(2.0/3.0)), y=0)

    win.getMouse()
    win.close()


def card_interaction(control, win):
    cont = True
    print_card_game_options()
    update_display(control, deck=True, hand=True, discard=True, in_play=True, selection=True)
    while(cont):
        line = raw_input(">")
        if len(line) < 1:
            print "Invalid Option, Try Again"
        elif line[0:1] == "o":
            print_card_game_options()
        elif line[0:1] == "d":
            try:
                command, num = line.split(" ")
            except:
                print "Invalid draw option, type d then a number, e.g. d 6"
                continue
            control.draw(int(num))
            update_display(control, deck=True, hand=True)

        elif line[0:1] == "p":
            try:
                command, item = line.split(" ")
            except:
                print "Invalid print option, choose p then deck, hand or discard, e.g. p hand"
                continue
            if item == "deck":
                control.deck.display()
            elif item == "hand":
                control.hand.display()
            elif "dis" in item:
                control.discard.display()
            else:
                print "Don't recognize {0} for printing".format(item)
        elif line[0:1] == "s":
            control.deck.shuffle()
        elif line[0:1] == "r":
            try:
                name = get_card_name(line)
            except:
                print "Invalid remove card option"
                continue
            control.remove_from_deck(name)
        elif len(line) > 2:
            if line[0:2] == "th":
                try:
                    name = get_card_name(line)
                except:
                    print "Invalid toss card from hand option"
                    continue
                control.discard_from_hand(name)
                update_display(control, hand=True, discard=True)        

            elif line[0:2] == "td":
                try:
                    num = get_number(line)
                except:
                    print "Invalid toss cards from top of deck option"

                control.discard_from_deck(num)
                update_display(control, discard=True)

            elif line[0:2] == "bh":
                try:
                    name = get_card_name(line)
                except:
                    print "Invalid bring card back to hand option"
                    continue
                control.bring_back_to_hand(name)
                update_display(control, hand=True, discard=True)

            elif line[0:2] == "bd":
                try:
                    name = get_card_name(line)
                except:
                    print "Invalid bring card back to dack option"
                    continue
                control.bring_back_to_deck(name)
                update_display(control, discard=True)
        elif line[0:1] == "q":
            cont = False
            win.close()
        else:
            print "Invalid Option, Try Again (press o to see options)"


def pcd_game(win):
    win.delete("all")

    win_x = win.winfo_x()
    win_y = win.winfo_y()

    standard_deck = get_standard_playing_card_deck_view(win)
    deck_context = {
            'lx': win_x + SCREEN['width'] - (SCREEN['width']/6.0),
            'rx': win_x + SCREEN['width'],
            'ty': win_y + SCREEN['height'] - (SCREEN['height']/3.0),
            'by': win_y + SCREEN['height']
    }

    deck = CardOrganizerDisplay(standard_deck, win, deck_context)

    dis_context = {
            'lx': win_x,
            'rx': win_x + (SCREEN['width']/6.0),
            'ty': deck_context['ty'],
            'by': deck_context['by']
    }

    dis = CardOrganizerDisplay(None, win, dis_context)

    hand_context = {
            'lx': dis_context['rx'],
            'rx': deck_context['lx'],
            'ty': deck_context['ty'],
            'by': deck_context['by']
    }

    hand = CardOrganizerDisplay(None, win, hand_context)

    play_context = {
            'lx': dis_context['lx'],
            'rx': deck_context['rx'],
            'ty': win_y,
            'by': win_y + SCREEN['height'] - (SCREEN['height']*(2.0/3.0))
    }

    play = CardOrganizerDisplay(None, win, play_context)

    sel_context = {
            'lx': hand_context['lx'],
            'rx': hand_context['rx'],
            'ty': play_context['by'],
            'by': hand_context['ty']
    }

    sel = CardOrganizerDisplay(None, win, sel_context)

    pcd = CardController(deck=deck, discard=dis, hand=hand, in_play=play, selected=sel)

    game_outline = GameOutline(win, win_x, win_y, SCREEN['width'], SCREEN['height'])
    game_outline.display_outline_with_labels()

    card_interaction(pcd, win)


def update_display(control, deck=False, discard=False, hand=False, in_play=False, selection=False):
    if deck:
        control.deck.undisplay()
        control.deck.display(hidden=True)

    if discard:
        control.discard.undisplay()
        control.discard.display()

    if hand:
        control.hand.undisplay()
        control.hand.display()

    if in_play:
        control.in_play.undisplay()
        control.in_play.display()

    if selection:
        control.selected.undisplay()
        control.selected.display()


def get_number(input):
    command, number = input.split(" ")
    return int(number)

def get_card_name(input):
    vals = input.split(" ")
    vals = vals[1:]
    name = (" ").join(vals)
    return name


def print_card_game_options():
    print "Choose from the following options at any time:"
    print "options or o -- to print options"
    print "draw # or d # -- to draw that many cards"
    print "print hand, p deck, p discard -- to print cards"
    print "shuffle or s -- to shuffle deck"
    print "th <card name> -- to discard that card from hand"
    print "td # -- to discard that many cards from top of deck"
    print "r <card name> -- to remove card from deck"
    print "bh <card name> -- to bring card from discard to hand"
    print "bd <card name> -- to bring card from discard to deck"
    print "quit or q -- to Quit"


if __name__ == "__main__":
        visual_main()
