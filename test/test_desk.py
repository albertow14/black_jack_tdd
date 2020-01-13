import unittest
from ..black import desk



class TestDesk(unittest.TestCase):
    def test_number_of_cards(self):
        for num in range(1,8):         
            assert desk.count(num) == 4
        assert desk.count(10) == 12