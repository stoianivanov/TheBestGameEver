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
        self.assertEqual(self.f.start_fights(), "A fight is started between our Hero(health=100, mana=100) and Enemy(health=100, mana=100, damage=20)")

    def test_enemy_attack(self):
        self.f.enemy_attack()
        self.assertEqual(self.h.get_health(), 80)

    def test_hero_attack_with_weapon_zero_dmg(self):
        self.f.hero_attack(by='weapon')
        self.assertEqual(self.e.health, 100)

    def test_hero_attack_with_weapon_non_zero_dmg(self):
        self.h.weapon_equipment[0] = Weapon("Pistol", damage=10)
        f2 = Fights(self.h, self.e)
        f2.hero_attack(by='weapon')
        self.assertEqual(self.e.health, 100)
if __name__ == '__main__':
    unittest.main()
