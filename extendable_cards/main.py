from extendable_cards.lib.playing_cards import get_standard_playing_card_deck
from extendable_cards.lib.cards import CardController, CardOrganizer
import fileinput
import pdb

def main():
    cont = True
    while(cont):
        print "Choose a Deck to Play: "
        print "pcd for Standard Playing Card Deck"
        print "quit to Quit"

        line = raw_input(">")
        if "pcd" in line:
            pcd_game()
        elif "q" in line or "quit" in line:
            cont = False
        else:
            print "Invalid Option, Try Again"

def card_interaction(control):
    cont = True
    print_card_game_options()
    while(cont):
        line = raw_input(">")
        if len(line) < 1:
            print "Invalid Option, Try Again"
        elif line[0:1] == "o":
            print_card_game_options()
        elif line[0:1] == "d":
            try:
                command, num = line.split(" ")
                control.draw(int(num))
            except:
                print "Invalid draw option, type d then a number, e.g. d 6"
        elif line[0:1] == "p":
            try:
                command, item = line.split(" ")
                if item == "deck":
                    print control.deck
                elif item == "hand":
                    print control.hand
                elif "dis" in item:
                    print control.discard
                else:
                    print "Don't recognize {0} for printing".format(item)
            except:
                print "Invalid print option, choose p then deck, hand or discard, e.g. p hand"
        elif line[0:1] == "s":
            control.deck.shuffle()
        elif line[0:1] == "r":
            try:
                name = get_card_name(line)
                result = control.remove_from_deck(name)
                if not result:
                    print "Couldn't remove card {0} from deck".format(name)
            except:
                print "Invalid remove card option"
        elif len(line) > 2:
            if line[0:2] == "th":
                try:
                    name = get_card_name(line)
                    result = control.discard_from_hand(name)
                    if not result:
                        print "Couldn't discard {0}".format(name)
                except:
                    print "Invalid toss card from hand option"
            elif line[0:2] == "td":
                try:
                    num = get_number(line)
                    control.discard_from_deck(num)
                except:
                    print "Invalid toss cards from top of deck option"
            elif line[0:2] == "bh":
                try:
                    name = get_card_name(line)
                    result = control.bring_back_to_hand(name)
                    if not result:
                        print "Couldn't bring card back to hand"
                except:
                    print "Invalid bring card back to hand option"
            elif line[0:2] == "bd":
                try:
                    name = get_card_name(line)
                    result = control.bring_back_to_deck(name)
                    if not result:
                        print "Couldn't bring card back to deck"
                except:
                    print "Invalid bring card back to dack option"
        elif line[0:1] == "q":
            cont = False
        else:
            print "Invalid Option, Try Again (press o to see options)"


def pcd_game():
    cont = True
    standard_deck = CardOrganizer(get_standard_playing_card_deck())
    pcd = CardController(deck=standard_deck)
    card_interaction(pcd)

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
        main()
