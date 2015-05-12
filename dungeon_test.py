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

    def test_out_of_map(self):
        self.assertTrue(self.d.out_of_map(12, 20))

    def test_in_the_map(self):
        self.assertFalse(self.d.out_of_map(2, 3))

    def test_obrancle(self):
        self.assertTrue(self.d.is_obstacle(2, 3))

    def test_position_of_hero(self):
        self.d.spawn(self.hero)
        self.d.print_map()
        print(self.d.return_position(self.d))
    # def test_can_spawn_hero(self):
        # self.d.spawn(self.hero)

if __name__ == '__main__':
    unittest.main()
