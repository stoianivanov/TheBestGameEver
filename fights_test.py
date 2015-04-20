from fights import Fights
from enemies import Enemy
from hero import Hero
import unittest

class FightsTest(unittest.TestCase):
    def setUp(self):
        self.h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        self.e =  Enemy(health=100, mana=100, damage=20)
        self.f = Fights(self.h, self.e)

    def test_starting_fight(self):
        self.assertEqual(self.f.start_fights(), "A fight is started between our Hero(health=100, mana=100) and Enemey(health=100, mana=100, damage=20)")


if __name__ == '__main__':
    unittest.main()
