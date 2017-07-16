from extendable_cards.lib.cards import Card, CardController, CardOrganizer
from extendable_cards.lib.playing_cards import PlayingCard, get_standard_playing_card_deck
from extendable_cards.lib.sentinels import SentinelTag
from extendable_cards.view.graphics import GraphWin, Point
from extendable_cards.view.game_outline import GameOutline
from extendable_cards.view.card_view import CardView, CardOrganizerDisplay
from extendable_cards.view.playing_card_view import PlayingCardView, get_standard_playing_card_deck_view
from extendable_cards.view.sentinels_card_view import SentinelCardView, get_grand_warlord_voss_hero_view, get_lady_of_the_woods_hero_view
from tkinter import Button, Entry
import sys
import pdb

SCREEN = {"height": 100, "width": 100}
INTRO_UI = []

def visual_main(argv):
    if argv:
        if argv[0] == 'console':
            console_game_input_loop()
            sys.exit(0)
            
    
    win = GraphWin("Extendable Cards", 100, 100)
    SCREEN["width"] = win.winfo_screenwidth() * 0.8
    SCREEN["height"] = win.winfo_screenheight() * 0.8

    win.config(width=SCREEN["width"], height=SCREEN["height"])

    pc_b = Button(win, text="Standard Playing Card Deck", command=lambda: pcd_game(win))
    INTRO_UI.append(pc_b)
    pc_b.place(x=(SCREEN['width']/3.0), y=0)

    rd_b = Button(win, text="Rainek the Disgraced", command=lambda: sentinels_game(win, 'rainek'))
    INTRO_UI.append(rd_b)
    rd_b.place(x=(SCREEN['width']/3.0), y=30)

    lw_b = Button(win, text="Lady of the Wood", command=lambda: sentinels_game(win, 'lady'))
    INTRO_UI.append(lw_b)
    lw_b.place(x=(SCREEN['width']/3.0), y=60)

    win.mainloop()


def console_game_input_loop():
    cards = get_standard_playing_card_deck()
    obj_cards = []
    for card in cards:
        if hasattr(card, 'suit'):
            obj_cards.append(PlayingCard(card.suit, card.number))
        else:
            obj_cards.append(Card(card.name))
    standard_deck=CardOrganizer(obj_cards, context={'label': 'deck'})
    control = CardController(deck=standard_deck)
    print_card_game_options()
    cont = True
    while(cont):
        line = raw_input("> ")
        cont = card_interaction(control, line)

    return False


def visual_game_input_loop(control, win):
    print_card_game_options()
    update_display(control, deck=True, hand=True, discard=True, in_play=True, selection=True)
    entry_width = 15
    entry_offpoint = SCREEN['width'] / 12
    
    e = Entry(win, width=int(entry_width))
    e.place(x=win.winfo_x() + entry_offpoint, y=win.winfo_y()+10)
    e.bind('<Return>', lambda event: card_interaction(control, e.get()))
    

def card_interaction(control, line):
    #line = raw_input(">")
    while(len(line) < 1):
        print "Invalid Option, Now waiting for terminal input"
        line = raw_input(">")

    if line[0:1] == "o":
        print_card_game_options()
    elif line[0:1] == "d":
        num = get_number(line)
        if num:
            control.draw(num)
            update_display(control, deck=True, hand=True)

    elif line[0:1] == "s":
        control.deck.shuffle()
    elif line[0:1] == "k":
        name = get_card_name(line)
        if name:
            control.remove_from_deck(name)
            update_display(control, deck=True)
    elif len(line) > 2:
        if line[0:2] == "ph":
            #play specific card from hand
            name = get_card_name(line)
            if name:
                control.play_from_hand(name)
                update_display(control, hand=True, in_play=True)
        elif line[0:2] == "pd":
            #play specific card from deck
            name = get_card_name(line)
            if name:
                control.play_from_deck(name)
                update_display(control, deck=True, in_play=True)
        elif line[0:2] == "pt":
            #play top card of deck
            num = get_number(line)
            if num:
                control.play_top_from_deck(num)
                update_display(control, deck=True, in_play=True)
        elif line[0:2] == "th":
            #discard specific card from hand
            name = get_card_name(line)
            if name:
                control.discard_from_hand(name)
                update_display(control, hand=True, discard=True)        
        elif line[0:2] == "td":
            #discard a number of cards from top of deck
            num = get_number(line)
            if num:
                control.discard_from_deck(num)
                update_display(control, deck=True, discard=True)
        elif line[0:2] == "tp":
            #discard a card from play
            name = get_card_name(line)
            if name:
                control.discard_from_play(name)
                update_display(control, discard=True, in_play=True)
        elif line[0:2] == "bh":
            #bring back card from discard into hand
            name = get_card_name(line)
            if name:
                control.bring_back_to_hand(name)
                update_display(control, hand=True, discard=True)
        elif line[0:2] == "bd":
            #bring back card from discard to bottom of deck
            name = get_card_name(line)
            if name:
                control.bring_back_to_deck(name)
                update_display(control, discard=True, deck=True)
        elif line[0:2] == "bdt":
            #bring back card from discard to top of deck
            name = get_card_name(line)
            if name:
                control.bring_back_to_deck_top(name)
                update_display(control, discard=True, deck=True)
        elif line[0:2] == "rh":
            #return card from play to hand
            name = get_card_name(line)
            if name:
                control.return_from_play_to_hand(name)
                update_display(control, in_play=True, hand=True)
        elif line[0:2] == "rd":
            #return card from play to hand
            name = get_card_name(line)
            if name:
                control.return_from_play_to_deck_top(name)
                update_display(control, in_play=True, deck=True)
    elif line[0:1] == "u":
        update_display(control, deck=True, discard=True, hand=True, in_play=True, selection=True)
    elif line[0:1] == "q":
        sys.exit(0)
        return False 
    else:
        print "Invalid Option, Try Again (press o to see options)"
    
    return True

def disable_intro_ui():
    for widget in INTRO_UI:
        widget.place_forget()

def pcd_game(win):
    win.delete("all")
    disable_intro_ui()
    y_padding = 50

    win_x = win.winfo_x()
    win_y = win.winfo_y()+y_padding
    width = SCREEN['width']
    height = SCREEN['height']-y_padding

    standard_deck = get_standard_playing_card_deck_view(win)
    contexts = _get_card_organizer_tkinter_contexts(win_x, win_y, width, height)

    deck = CardOrganizerDisplay(standard_deck, win, contexts['deck_context'])

    dis = CardOrganizerDisplay(None, win, contexts['dis_context'])

    hand = CardOrganizerDisplay(None, win, contexts['hand_context'])

    play = CardOrganizerDisplay(None, win, contexts['play_context'])

    sel = CardOrganizerDisplay(None, win, contexts['sel_context'])

    pcd = CardController(deck=deck, discard=dis, hand=hand, in_play=play, selected=sel)

    game_outline = GameOutline(win, win_x, win_y, width, height)
    game_outline.display_outline_with_labels()

    visual_game_input_loop(pcd, win)



def sentinels_game(win, deck_choice):
    win.delete("all")
    disable_intro_ui()

    y_padding = 50

    win_x = win.winfo_x()
    win_y = win.winfo_y()+y_padding
    width = SCREEN['width']
    height = SCREEN['height']-y_padding
    contexts = _get_card_organizer_tkinter_contexts(win_x, win_y, width, height)

    if 'lady' in deck_choice.lower():
        hero_deck = get_lady_of_the_woods_hero_view(win)
    else:
        hero_deck = get_grand_warlord_voss_hero_view(win)

    character_cards = []
    for card in hero_deck[:]:
        if SentinelTag.HERO in card.tags:
            print card
            character_cards.append(card)
            print character_cards
            hero_deck.remove(card)

    deck = CardOrganizerDisplay(hero_deck, win, contexts['deck_context'])

    dis = CardOrganizerDisplay(None, win, contexts['dis_context'])

    hand = CardOrganizerDisplay(None, win, contexts['hand_context'])

    play = CardOrganizerDisplay(None, win, contexts['play_context'])

    sel = CardOrganizerDisplay(character_cards, win, contexts['sel_context'])

    pcd = CardController(deck=deck, discard=dis, hand=hand, in_play=play, selected=sel)

    game_outline = GameOutline(win, win_x, win_y, width, height)
    game_outline.display_outline_with_labels()

    visual_game_input_loop(pcd, win)



def _get_card_organizer_tkinter_contexts(lx, ty, w, h):
    deck_context = {
            'lx': lx + w - (w/6.0),
            'rx': lx + w,
            'ty': ty + h - (h/3.0),
            'by': ty + h
    }
    dis_context = {
            'lx': lx,
            'rx': lx + (w/6.0),
            'ty': deck_context['ty'],
            'by': deck_context['by']
    }
    hand_context = {
            'lx': dis_context['rx'],
            'rx': deck_context['lx'],
            'ty': deck_context['ty'],
            'by': deck_context['by']
    }
    play_context = {
            'lx': dis_context['lx'],
            'rx': deck_context['rx'],
            'ty': ty,
            'by': ty + h - (h*(2.0/3.0))
    }
    sel_context = {
            'lx': hand_context['lx'],
            'rx': hand_context['rx'],
            'ty': play_context['by'],
            'by': hand_context['ty']
    }
    contexts = {
        'deck_context': deck_context,
        'dis_context': dis_context,
        'hand_context': hand_context,
        'play_context': play_context,
        'sel_context': sel_context
    }
    return contexts
    



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
    try:
        command, number = input.split(" ")
        num = int(number)
    except:
        print "Unable to get number from intput."
        return False
    return num

def get_card_name(input):
    try:
        vals = input.split(" ")
        vals = vals[1:]
        name = (" ").join(vals)
    except:
        print "Unable to decifer name from input."
        return False
    return name


def print_card_game_options():
    print "Choose from the following options at any time:"
    print "options or o -- to print options"
    print "draw # or d # -- to draw that many cards"
    print "shuffle or s -- to shuffle deck"
    
    print "ph <card name> -- to play card from hand"
    print "pd <card name> -- to play a card from deck"
    print "pt # -- to play that many cards from top of deck"

    print "th <card name> -- to discard that card from hand"
    print "td # -- to discard that many cards from top of deck"
    print "tp <card name> -- to discard a card from play"
    
    print "kill <card name> or k <card name> -- to remove card from deck"
    
    print "bh <card name> -- to bring card from discard to hand"
    print "bd <card name> -- to bring card from discard to deck"
    print "bdt <card name> -- to bring card from discard to top of deck"

    print "rd <card name> -- to return card from play to top of deck"
    print "rh <card name> -- to return card from play to hand"
    print "quit or q -- to Quit"


if __name__ == "__main__":
    visual_main(sys.argv[1:])
