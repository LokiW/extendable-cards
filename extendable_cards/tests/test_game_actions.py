from extendable_cards.visual_main import card_interaction
from extendable_cards.lib.cards import Card, CardOrganizer, CardController


#=============== TEST DRAW CARDS TO HAND =====================#

def test_draw_none_one():
    obj_cards = [Card("test_card_1"), Card("test_card_2"), Card("crazy_card_name_boogie"), Card("test")]
    standard_deck=CardOrganizer(obj_cards, context={'label': 'deck'})
    control = CardController(deck=standard_deck)

    #draw # or d # -- to draw that many cards
    line = "d "
    result = card_interaction(control, line)
    assert result
    assert control.hand.get_len() == 0
    assert control.deck.get_len() == 4

    line = "d 1"
    result = card_interaction(control, line)
    assert result
    assert control.hand.get_len() == 1
    assert control.deck.get_len() == 3
    assert control.hand.get_card("test_card_1")

def test_draw_many():
    obj_cards = [Card("test_card_1"), Card("test_card_2"), Card("crazy_card_name_boogie"), Card("test")]
    standard_deck=CardOrganizer(obj_cards, context={'label': 'deck'})
    control = CardController(deck=standard_deck)

    #draw # or d # -- to draw that many cards
    line = "draw 3"
    result = card_interaction(control, line)
    assert result
    assert control.hand.get_len() == 3
    assert control.deck.get_len() == 1
    assert control.deck.get_card("test")
    assert not control.deck.get_card("test_card_2")

def test_draw_none_one():
    obj_cards = [Card("test_card_1"), Card("test_card_2"), Card("crazy_card_name_boogie"), Card("test")]
    standard_deck=CardOrganizer(obj_cards, context={'label': 'deck'})
    control = CardController(deck=standard_deck)

    #draw # or d # -- to draw that many cards
    line = "d 8"
    result = card_interaction(control, line)
    assert result
    assert control.hand.get_len() == 4
    assert control.deck.get_len() == 0

#=============== TEST SHUFFLE CARDS =====================#

def test_shuffle():
    obj_cards = [Card("test_card_1"), Card("test_card_2"), Card("crazy_card_name_boogie"), Card("test")]
    standard_deck=CardOrganizer(obj_cards, context={'label': 'deck'})
    control = CardController(deck=standard_deck)

    #shuffle or s -- to shuffle deck
    line = "s"
    shuffled = False
    for i in range(10):
        result = card_interaction(control, line)
        assert result
        
        shuffled = (control.deck.get_top_cards(1)[0].name != "test_card_1") or shuffled

    assert shuffled

#=============== TEST PLAY CARDS =====================#

def test_play_hand_empty():
    obj_cards = [Card("test_card_1"), Card("test_card_2"), Card("crazy_card_name_boogie"), Card("test")]
    standard_deck=CardOrganizer(obj_cards, context={'label': 'deck'})
    control = CardController(deck=standard_deck)

    #ph <card name> -- to play card from hand
    line = "ph test_card_1"
    result = card_interaction(control, line)
    assert result
    assert control.deck.get_len() == 4
    assert control.hand.get_len() == 0
    assert control.in_play.get_len() == 0

def test_play_hand_substring():
    obj_cards = [Card("test_card_1"), Card("test_card_2"), Card("crazy_card_name_boogie"), Card("test")]
    standard_deck=CardOrganizer(obj_cards, context={'label': 'hand'})
    control = CardController(hand=standard_deck)

    #ph <card name> -- to play card from hand
    line = "ph tes"
    result = card_interaction(control, line)
    assert result
    assert control.deck.get_len() == 0
    assert control.hand.get_len() == 4
    assert control.in_play.get_len() == 0

    line = "ph crazy"
    result = card_interaction(control, line)
    assert result
    assert control.deck.get_len() == 0
    assert control.hand.get_len() == 3
    assert control.in_play.get_len() == 1
    assert control.in_play.get_card("crazy_card_name_boogie")


def test_play_hand_fullname():
    obj_cards = [Card("test_card_1"), Card("test_card_2"), Card("crazy_card_name_boogie"), Card("test")]
    standard_deck=CardOrganizer(obj_cards, context={'label': 'hand'})
    control = CardController(hand=standard_deck)

    #ph <card name> -- to play card from hand
    line = "ph test"
    result = card_interaction(control, line)
    assert result
    assert control.deck.get_len() == 0
    assert control.hand.get_len() == 3
    assert control.in_play.get_len() == 1
    assert control.in_play.get_top_cards(1)[0].name == "test"

    #ph <card name> -- to play card from hand
    line = "ph test_card_2"
    result = card_interaction(control, line)
    assert result
    assert control.deck.get_len() == 0
    assert control.hand.get_len() == 2
    assert control.in_play.get_len() == 2
    assert control.in_play.get_card("test_card_2")

def test_play_deck_invalid_entry():
    obj_cards = [Card("test_card_1"), Card("test_card_2"), Card("crazy_card_name_boogie"), Card("test")]
    standard_deck=CardOrganizer(obj_cards, context={'label': 'deck'})
    control = CardController(deck=standard_deck)

    #pd <card name> -- to play a card from deck
    line = "pd "
    result = card_interaction(control, line)
    assert result
    assert control.deck.get_len() == 4
    assert control.hand.get_len() == 0
    assert control.in_play.get_len() == 0

    #pd <card name> -- to play a card from deck
    line = "pd crazy_test"
    result = card_interaction(control, line)
    assert result
    assert control.deck.get_len() == 4
    assert control.hand.get_len() == 0
    assert control.in_play.get_len() == 0

def test_play_deck_invalid_substring():
    obj_cards = [Card("test_card_1"), Card("test_card_2"), Card("crazy_card_name_boogie"), Card("test")]
    standard_deck=CardOrganizer(obj_cards, context={'label': 'deck'})
    control = CardController(deck=standard_deck)

    #pd <card name> -- to play a card from deck
    line = "pd test_card"
    result = card_interaction(control, line)
    assert result
    assert control.deck.get_len() == 4
    assert control.hand.get_len() == 0
    assert control.in_play.get_len() == 0

    #pd <card name> -- to play a card from deck
    line = "pd te"
    result = card_interaction(control, line)
    assert result
    assert control.deck.get_len() == 4
    assert control.hand.get_len() == 0
    assert control.in_play.get_len() == 0


def test_play_deck_empty():
    obj_cards = [Card("test_card_1"), Card("test_card_2"), Card("crazy_card_name_boogie"), Card("test")]
    standard_deck=CardOrganizer(obj_cards, context={'label': 'hand'})
    control = CardController(hand=standard_deck)
    
    #pd <card name> -- to play a card from deck
    line = "pd "
    result = card_interaction(control, line)
    assert result
    assert control.deck.get_len() == 0
    assert control.hand.get_len() == 4
    assert control.in_play.get_len() == 0


def test_play_deck_substring():
    obj_cards = [Card("test_card_1"), Card("test_card_2"), Card("crazy_card_name_boogie"), Card("test")]
    standard_deck=CardOrganizer(obj_cards, context={'label': 'deck'})
    control = CardController(deck=standard_deck)
    
    #pd <card name> -- to play a card from deck
    line = "pd crazy"
    result = card_interaction(control, line)
    assert result
    assert control.deck.get_len() == 3
    assert control.hand.get_len() == 0
    assert control.in_play.get_len() == 1

def test_play_deck_fullname():
    obj_cards = [Card("test_card_1"), Card("test_card_2"), Card("crazy_card_name_boogie"), Card("test")]
    standard_deck=CardOrganizer(obj_cards, context={'label': 'deck'})
    control = CardController(deck=standard_deck)
    
    #pd <card name> -- to play a card from deck
    line = "pd test"
    result = card_interaction(control, line)
    assert result
    assert control.deck.get_len() == 3
    assert control.hand.get_len() == 0
    assert control.in_play.get_len() == 1
    assert control.in_play.get_top_cards(1)[0].name == "test"


    #pd <card name> -- to play a card from deck
    line = "pd crazy_card_name_boogie"
    result = card_interaction(control, line)
    assert result
    assert control.deck.get_len() == 2
    assert control.hand.get_len() == 0
    assert control.in_play.get_len() == 2
    assert control.in_play.get_top_cards(1)[0].name == "test"
    assert control.in_play.get_card("crazy_card_name_boogie")


def test_play_deck_top():
    obj_cards = [Card("test_card_1"), Card("test_card_2"), Card("crazy_card_name_boogie"), Card("test")]
    standard_deck=CardOrganizer(obj_cards, context={'label': 'deck'})
    control = CardController(deck=standard_deck)

    #pt # -- to play that many cards from top of deck
    line = "pt "
    result = card_interaction(control, line)
    assert result
    assert control.deck.get_len() == 4
    assert control.hand.get_len() == 0
    assert control.in_play.get_len() == 0

    #pt # -- to play that many cards from top of deck
    line = "pt 1"
    result = card_interaction(control, line)
    assert result
    assert control.deck.get_len() == 3
    assert control.hand.get_len() == 0
    assert control.in_play.get_len() == 1
    assert control.in_play.get_top_cards(1)[0].name == "test_card_1"

def test_play_deck_top_many():
    obj_cards = [Card("test_card_1"), Card("test_card_2"), Card("crazy_card_name_boogie"), Card("test")]
    standard_deck=CardOrganizer(obj_cards, context={'label': 'deck'})
    control = CardController(deck=standard_deck)

    #pt # -- to play that many cards from top of deck
    line = "pt 6"
    result = card_interaction(control, line)
    assert result
    assert control.deck.get_len() == 0
    assert control.hand.get_len() == 0
    assert control.in_play.get_len() == 4


def test_play_deck_top_empty():
    obj_cards = [Card("test_card_1"), Card("test_card_2"), Card("crazy_card_name_boogie"), Card("test")]
    standard_deck=CardOrganizer(obj_cards, context={'label': 'hand'})
    control = CardController(hand=standard_deck)

    #pt # -- to play that many cards from top of deck
    line = "pt 1"
    result = card_interaction(control, line)
    assert result
    assert control.deck.get_len() == 0
    assert control.hand.get_len() == 4
    assert control.in_play.get_len() == 0


#=============== TEST TOSS CARD INTO DISCARD =====================#


def test_toss_hand():
    obj_cards = [Card("test_card_1"), Card("test_card_2"), Card("crazy_card_name_boogie"), Card("test")]
    standard_deck=CardOrganizer(obj_cards, context={'label': 'hand'})
    control = CardController(hand=standard_deck)

    #th <card name> -- to discard that card from hand
    line = "th "
    result = card_interaction(control, line)
    assert result
    assert control.deck.get_len() == 0
    assert control.hand.get_len() == 4
    assert control.discard.get_len() == 0

    #th <card name> -- to discard that card from hand
    line = "th test_card_1"
    result = card_interaction(control, line)
    assert result
    assert control.deck.get_len() == 0
    assert control.hand.get_len() == 3
    assert control.discard.get_len() == 1
    assert control.discard.get_card("test_card_1")


def test_toss_hand_empty():
    obj_cards = [Card("test_card_1"), Card("test_card_2"), Card("crazy_card_name_boogie"), Card("test")]
    standard_deck=CardOrganizer(obj_cards, context={'label': 'deck'})
    control = CardController(deck=standard_deck)

    #th <card name> -- to discard that card from hand
    line = "th test_card_1"
    result = card_interaction(control, line)
    assert result
    assert control.deck.get_len() == 4
    assert control.hand.get_len() == 0
    assert control.discard.get_len() == 0


def test_toss_hand_substring():
    obj_cards = [Card("test_card_1"), Card("test_card_2"), Card("crazy_card_name_boogie"), Card("test")]
    standard_deck=CardOrganizer(obj_cards, context={'label': 'hand'})
    control = CardController(hand=standard_deck)

    #th <card name> -- to discard that card from hand
    line = "th crazy"
    result = card_interaction(control, line)
    assert result
    assert control.deck.get_len() == 0
    assert control.hand.get_len() == 3
    assert control.discard.get_len() == 1
 
 

def test_toss_deck_empty():
    obj_cards = [Card("test_card_1"), Card("test_card_2"), Card("crazy_card_name_boogie"), Card("test")]
    standard_deck=CardOrganizer(obj_cards, context={'label': 'hand'})
    control = CardController(hand=standard_deck)


    line = "td 1"
    result = card_interaction(control, line)
    assert result
    assert control.deck.get_len() == 0
    assert control.hand.get_len() == 4
    assert control.discard.get_len() == 0


def test_toss_deck():
    obj_cards = [Card("test_card_1"), Card("test_card_2"), Card("crazy_card_name_boogie"), Card("test")]
    standard_deck=CardOrganizer(obj_cards, context={'label': 'deck'})
    control = CardController(deck=standard_deck)

    #td # -- to discard that many cards from top of deck
    line = "td "
    result = card_interaction(control, line)
    assert result
    assert control.deck.get_len() == 4
    assert control.hand.get_len() == 0
    assert control.discard.get_len() == 0

    #td # -- to discard that many cards from top of deck
    line = "td 1"
    result = card_interaction(control, line)
    assert result
    assert control.deck.get_len() == 3
    assert control.hand.get_len() == 0
    assert control.discard.get_len() == 1
    assert control.discard.get_card("test_card_1")

def test_toss_deck_many():
    obj_cards = [Card("test_card_1"), Card("test_card_2"), Card("crazy_card_name_boogie"), Card("test")]
    standard_deck=CardOrganizer(obj_cards, context={'label': 'deck'})
    control = CardController(deck=standard_deck)

    #td # -- to discard that many cards from top of deck
    line = "td 6"
    result = card_interaction(control, line)
    assert result
    assert control.deck.get_len() == 0
    assert control.hand.get_len() == 0
    assert control.discard.get_len() == 4


def test_toss_play():
    obj_cards = [Card("test_card_1"), Card("test_card_2"), Card("crazy_card_name_boogie"), Card("test")]
    standard_deck=CardOrganizer(obj_cards, context={'label': 'in play'})
    control = CardController(in_play=standard_deck)

    #tp <card name> -- to discard a card from play
    line = "tp "
    result = card_interaction(control, line)
    assert result
    assert control.deck.get_len() == 0
    assert control.in_play.get_len() == 4
    assert control.discard.get_len() == 0

    #tp <card name> -- to discard a card from play
    line = "tp test_card_1"
    result = card_interaction(control, line)
    assert result
    assert control.deck.get_len() == 0
    assert control.in_play.get_len() == 3
    assert control.discard.get_len() == 1
    assert control.discard.get_card("test_card_1")


def test_toss_play_empty():
    obj_cards = [Card("test_card_1"), Card("test_card_2"), Card("crazy_card_name_boogie"), Card("test")]
    standard_deck=CardOrganizer(obj_cards, context={'label': 'deck'})
    control = CardController(deck=standard_deck)

    #tp <card name> -- to discard a card from play
    line = "tp test_card_1"
    result = card_interaction(control, line)
    assert result
    assert control.deck.get_len() == 4
    assert control.in_play.get_len() == 0
    assert control.discard.get_len() == 0


def test_toss_play_substring():
    obj_cards = [Card("test_card_1"), Card("test_card_2"), Card("crazy_card_name_boogie"), Card("test")]
    standard_deck=CardOrganizer(obj_cards, context={'label': 'in play'})
    control = CardController(in_play=standard_deck)

    #tp <card name> -- to discard a card from play
    line = "tp crazy"
    result = card_interaction(control, line)
    assert result
    assert control.deck.get_len() == 0
    assert control.in_play.get_len() == 3
    assert control.discard.get_len() == 1


#=============== TEST REMOVE CARD FROM GAME =====================#
def test_toss_play_empty():
    obj_cards = [Card("test_card_1"), Card("test_card_2"), Card("crazy_card_name_boogie"), Card("test")]
    standard_deck=CardOrganizer(obj_cards, context={'label': 'deck'})
    control = CardController(deck=standard_deck)

    #kill <card name> or k <card name> -- to remove card from deck
    line = "kill test_card_2"
    result = card_interaction(control, line)
    assert result
    assert control.deck.get_len() == 3
    assert control.in_play.get_len() == 0
    assert control.discard.get_len() == 0
    assert control.hand.get_len() == 0
    assert not control.deck.get_card("test_card_2")

#=============== TEST BRING CARDS BACK FROM DISCARD =====================#

    #bh <card name> -- to bring card from discard to hand

def test_bring_back_to_hand():
    obj_cards = [Card("test_card_1"), Card("test_card_2"), Card("crazy_card_name_boogie"), Card("test")]
    standard_deck=CardOrganizer(obj_cards, context={'label': 'discard'})
    control = CardController(discard=standard_deck)

    #bh <card name> -- to bring card from discard to hand
    line = "bh "
    result = card_interaction(control, line)
    assert result
    assert control.deck.get_len() == 0
    assert control.discard.get_len() == 4
    assert control.hand.get_len() == 0

    #bh <card name> -- to bring card from discard to hand
    line = "bh test_card_1"
    result = card_interaction(control, line)
    assert result
    assert control.deck.get_len() == 0
    assert control.discard.get_len() == 3
    assert control.hand.get_len() == 1
    assert control.hand.get_card("test_card_1")


def test_bring_back_to_hand_empty():
    obj_cards = [Card("test_card_1"), Card("test_card_2"), Card("crazy_card_name_boogie"), Card("test")]
    standard_deck=CardOrganizer(obj_cards, context={'label': 'deck'})
    control = CardController(deck=standard_deck)

    #bh <card name> -- to bring card from discard to hand
    line = "bh test_card_1"
    result = card_interaction(control, line)
    assert result
    assert control.deck.get_len() == 4
    assert control.hand.get_len() == 0
    assert control.discard.get_len() == 0


def test_bring_back_to_hand_substring():
    obj_cards = [Card("test_card_1"), Card("test_card_2"), Card("crazy_card_name_boogie"), Card("test")]
    standard_deck=CardOrganizer(obj_cards, context={'label': 'discard'})
    control = CardController(discard=standard_deck)

    #bh <card name> -- to bring card from discard to hand
    line = "bh crazy"
    result = card_interaction(control, line)
    assert result
    assert control.deck.get_len() == 0
    assert control.discard.get_len() == 3
    assert control.hand.get_len() == 1
    

def test_bring_back_to_deck():
    obj_cards = [Card("test_card_1"), Card("test_card_2"), Card("crazy_card_name_boogie"), Card("test")]
    standard_deck=CardOrganizer(obj_cards, context={'label': 'discard'})
    control = CardController(discard=standard_deck)

    #bd <card name> -- to bring card from discard to deck
    line = "bd "
    result = card_interaction(control, line)
    assert result
    assert control.deck.get_len() == 0
    assert control.discard.get_len() == 4

    #bd <card name> -- to bring card from discard to deck
    line = "bd test_card_1"
    result = card_interaction(control, line)
    assert result
    assert control.deck.get_len() == 1
    assert control.discard.get_len() == 3
    assert control.deck.get_card("test_card_1")


def test_bring_back_to_deck_empty():
    obj_cards = [Card("test_card_1"), Card("test_card_2"), Card("crazy_card_name_boogie"), Card("test")]
    standard_deck=CardOrganizer(obj_cards, context={'label': 'deck'})
    control = CardController(deck=standard_deck)

    #bd <card name> -- to bring card from discard to deck
    line = "bd test_card_1"
    result = card_interaction(control, line)
    assert result
    assert control.deck.get_len() == 4
    assert control.discard.get_len() == 0


def test_bring_back_to_deck_substring():
    obj_cards = [Card("test_card_1"), Card("test_card_2"), Card("crazy_card_name_boogie"), Card("test")]
    standard_deck=CardOrganizer(obj_cards, context={'label': 'discard'})
    control = CardController(discard=standard_deck)

    #bd <card name> -- to bring card from discard to deck
    line = "bd crazy"
    result = card_interaction(control, line)
    assert result
    assert control.deck.get_len() == 1
    assert control.discard.get_len() == 3

    #####


def test_bring_back_to_deck_top():
    obj_cards = [Card("test_card_1"), Card("test_card_2"), Card("crazy_card_name_boogie"), Card("test")]
    standard_deck=CardOrganizer(obj_cards, context={'label': 'discard'})
    control = CardController(discard=standard_deck)

    #bdt <card name> -- to bring card from discard to top of deck
    line = "bdt "
    result = card_interaction(control, line)
    assert result
    assert control.deck.get_len() == 0
    assert control.discard.get_len() == 4

    #bdt <card name> -- to bring card from discard to top of deck
    line = "bdt test_card_1"
    result = card_interaction(control, line)
    assert result
    assert control.deck.get_len() == 1
    assert control.discard.get_len() == 3
    assert control.deck.get_top_cards(1)[0].name == "test_card_1"


def test_bring_back_to_deck_top_empty():
    obj_cards = [Card("test_card_1"), Card("test_card_2"), Card("crazy_card_name_boogie"), Card("test")]
    standard_deck=CardOrganizer(obj_cards, context={'label': 'deck'})
    control = CardController(deck=standard_deck)

    #bdt <card name> -- to bring card from discard to top of deck
    line = "bdt test_card_1"
    result = card_interaction(control, line)
    assert result
    assert control.deck.get_len() == 4
    assert control.discard.get_len() == 0


def test_bring_back_to_deck_top_substring():
    obj_cards = [Card("test_card_1"), Card("test_card_2"), Card("crazy_card_name_boogie"), Card("test")]
    standard_deck=CardOrganizer(obj_cards, context={'label': 'discard'})
    control = CardController(discard=standard_deck)

    #bdt <card name> -- to bring card from discard to top of deck
    line = "bdt crazy"
    result = card_interaction(control, line)
    assert result
    assert control.deck.get_len() == 1
    assert control.discard.get_len() == 3



#=============== TEST RETURN CARD FROM IN PLAY =====================#

def test_return_to_deck():
    obj_cards = [Card("test_card_1"), Card("test_card_2"), Card("crazy_card_name_boogie"), Card("test")]
    standard_deck=CardOrganizer(obj_cards, context={'label': 'in play'})
    control = CardController(in_play=standard_deck)

    #rd <card name> -- to return card from play to top of deck
    line = "rd "
    result = card_interaction(control, line)
    assert result
    assert control.deck.get_len() == 0
    assert control.in_play.get_len() == 4
    assert control.discard.get_len() == 0

    #rd <card name> -- to return card from play to top of deck
    line = "rd test_card_1"
    result = card_interaction(control, line)
    assert result
    assert control.deck.get_len() == 1
    assert control.in_play.get_len() == 3
    assert control.discard.get_len() == 0
    assert control.deck.get_card("test_card_1")


def test_return_to_deck_empty():
    obj_cards = [Card("test_card_1"), Card("test_card_2"), Card("crazy_card_name_boogie"), Card("test")]
    standard_deck=CardOrganizer(obj_cards, context={'label': 'deck'})
    control = CardController(deck=standard_deck)

    #rd <card name> -- to return card from play to top of deck
    line = "rd test_card_1"
    result = card_interaction(control, line)
    assert result
    assert control.deck.get_len() == 4
    assert control.in_play.get_len() == 0
    assert control.discard.get_len() == 0


def test_return_to_deck_substring():
    obj_cards = [Card("test_card_1"), Card("test_card_2"), Card("crazy_card_name_boogie"), Card("test")]
    standard_deck=CardOrganizer(obj_cards, context={'label': 'in play'})
    control = CardController(in_play=standard_deck)

    #rd <card name> -- to return card from play to top of deck
    line = "rd crazy"
    result = card_interaction(control, line)
    assert result
    assert control.deck.get_len() == 1
    assert control.in_play.get_len() == 3
    assert control.discard.get_len() == 0


def test_return_to_hand():
    obj_cards = [Card("test_card_1"), Card("test_card_2"), Card("crazy_card_name_boogie"), Card("test")]
    standard_deck=CardOrganizer(obj_cards, context={'label': 'in play'})
    control = CardController(in_play=standard_deck)

    #rh <card name> -- to return card from play to hand
    line = "rh "
    result = card_interaction(control, line)
    assert result
    assert control.deck.get_len() == 0
    assert control.in_play.get_len() == 4
    assert control.discard.get_len() == 0

    #rh <card name> -- to return card from play to hand
    line = "rh test_card_1"
    result = card_interaction(control, line)
    assert result
    assert control.deck.get_len() == 0
    assert control.in_play.get_len() == 3
    assert control.hand.get_len() == 1
    assert control.hand.get_card("test_card_1")


def test_return_to_hand_empty():
    obj_cards = [Card("test_card_1"), Card("test_card_2"), Card("crazy_card_name_boogie"), Card("test")]
    standard_deck=CardOrganizer(obj_cards, context={'label': 'deck'})
    control = CardController(deck=standard_deck)

    #rh <card name> -- to return card from play to hand
    line = "rh test_card_1"
    result = card_interaction(control, line)
    assert result
    assert control.deck.get_len() == 4
    assert control.in_play.get_len() == 0
    assert control.discard.get_len() == 0


def test_return_to_hand_substring():
    obj_cards = [Card("test_card_1"), Card("test_card_2"), Card("crazy_card_name_boogie"), Card("test")]
    standard_deck=CardOrganizer(obj_cards, context={'label': 'in play'})
    control = CardController(in_play=standard_deck)

    #rh <card name> -- to return card from play to hand
    line = "rh crazy"
    result = card_interaction(control, line)
    assert result
    assert control.deck.get_len() == 0
    assert control.in_play.get_len() == 3
    assert control.hand.get_len() == 1


#=============== TEST QUIT GAME =====================#
def test_toss_play_empty():
    obj_cards = [Card("test_card_1"), Card("test_card_2"), Card("crazy_card_name_boogie"), Card("test")]
    standard_deck=CardOrganizer(obj_cards, context={'label': 'deck'})
    control = CardController(deck=standard_deck)

    #quit or q -- to Quit
    line = "q"
    #TODO figure out how to capture sys.exit 

