import unittest
from hero import Hero
from weapon import Weapon
from spell import Spell


class HeroTest(unittest.TestCase):

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

    def test_exists_class(self):
        self.assertTrue(isinstance(self.hero, Hero))

    def test_hero_known_as(self):
        self.assertTrue(self.hero.known_as(), "Bron the DragonSlayer")

    def test_hero_is_alive(self):
        self.assertTrue(self.hero.is_alive(), True)

    def test_is_hero_not_alive(self):
        self.hero.reduce_health(100)
        self.assertFalse(self.hero.is_alive())

    def test_hero_can_cast(self):
        self.assertTrue(self.hero.can_cast(), True)

    def test_hero_can_cast_false(self):
        self.hero.reduce_mana(100)
        self.assertFalse(self.hero.can_cast())

    def test_mana_regeneration_rate(self):
        self.assertEqual(self.hero.mana_regeneration_rate(), 2)

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

    def test_hero_weapon(self):
        weapon_equipment = []
        weapon_equipment.append(self.weapon)
        self.assertEqual(weapon_equipment[0], self.weapon)

    def test_hero_can_equip_with_weapon(self):
        self.hero.equip(self.weapon)
        self.assertEqual(str(self.hero.weapon_equipment[0]),
                         self.weapon.get_name())

    def test_hero_spell(self):
        learned_spell = []
        learned_spell.append(self.spell)
        self.assertEqual(learned_spell[0], self.spell)

    def test_hero_can_learn_new_spell(self):
        self.hero.learn(self.spell)
        self.assertEqual(str(self.hero.learned_spell[0]),
                         self.spell.get_name())

if __name__ == '__main__':
    unittest.main()
