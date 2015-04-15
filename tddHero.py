import unittest
from hero import Hero


class HeroTest(unittest.TestCase):

    def setUp(self):
        self.hero = Hero(name="Bron",
                         title="Dragonslayer",
                         health=100, mana=100,
                         mana_regeneration_rate=2)

    def test_exists_class(self):
        self.assertTrue(isinstance(self.hero, Hero))

    def test_hero_known_as(self):
        self.assertTrue(self.hero.known_as(), "Bron the DragonSlayer")

    def test_hero_is_alive(self):
        self.assertTrue(self.hero.is_alive(), True)

    def test_hero_can_cast(self):
        self.assertTrue(self.hero.can_cast(), True)

    def test_hero_take_damage(self):
        damage_points = 20
        self.hero.take_damage(damage_points)
        self.assertEqual(self.hero.get_health(), 80)

    def test_hero_take_healing(self):
        healing_points = 20
        damage_points = 90
        self.hero.take_damage(damage_points)
        self.hero.take_healing(healing_points)
        self.assertTrue(self.hero.get_health(), 30)

    def test_hero_take_mana(self):
        damage_points = 50
        mana_points = 40
        new_mana_points = 20
        self.hero.take_damage(damage_points)
        self.hero.reduce_mana(mana_points)
        self.assertTrue(self.hero.take_mana(new_mana_points), 80)

if __name__ == '__main__':
    unittest.main()
