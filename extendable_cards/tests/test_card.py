from extendable_cards.lib.cards import Card


def test_card():
    test_name = "test name"
    c = Card(test_name)

    assert c.name == test_name
    assert str(c) == test_name
    assert False

