from extendable_cards.lib.cards import Card
from mock import Patch, Mock, MagicMock
from StringIO import StringIO

@patch('sys.stdout', new_callable=StringIO)
def test_card(mock_stdout):
    test_name = "test name"
    c = Card(test_name)

    assert c.name == test_name
    assert str(c) == test_name
    c.display_card
    assert mock_stdout.getValue() == "[test_name]"

