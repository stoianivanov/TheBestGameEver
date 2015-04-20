import unittest
from hero import Hero
from weapon import Weapon
from spell import Spell
from dungeon import Dungeon


class DungeonTest(unittest.TestCase):

    def setUp(self):
        self.hero = Hero(name="Bron",
                         title="Dragonslayer",
                         health=100, mana=100,
                         mana_regeneration_rate=2)
        self.weapon = Weapon(name="The Axe of Destiny", damage=20)
        self.spell = Spell(name="Fireball",
                           damage=30,
                           mana_cost=50,
                           cast_range=2)
        self.d = Dungeon("level1.txt")

    # def test_out_of(self):
    #     d1 = Dungeon("level1.txt")
    #     self.assertTrue(d1.spawn(self.hero))
    def test_obrancle(self):
        self.assertTrue(self.d.is_obstacle(2, 3))
if __name__ == '__main__':
    unittest.main()
