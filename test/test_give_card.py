import unittest
from ..black import givecard, desk



class TestGiveCard(unittest.TestCase):
    def testgivecard(self):
        player = givecard(desk)

        assert player > 0 and player <=10 and player not in (8,9)

    def test_card_given_between_one_to_seven_deleted(self):
        num = 5
        eliminate(num, desk)

        assert desk.count(num) == 3


