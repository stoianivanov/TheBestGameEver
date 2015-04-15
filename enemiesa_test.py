import unittest
from enemies import *


class EnemiesTest(unittest.TestCase):
    def setUp(self):
        self.enemy = Enemy(health=100, mana=100, damage=20)

    def test_create_enemy(self):
        self.assertTrue(isinstance(self.enemy, Enemy))

    def test_is_alive_false(self):
        self.enemy.health = 0
        self.assertFalse(self.enemy.is_alive())

    def test_is_alive_true(self):
        self.assertTrue(self.enemy.is_alive())

    def test_can_cast_true(self):
        self.assertTrue(self.enemy.can_cast())

    def test_can_cast_false(self):
        self.enemy.mana = 0
        self.assertFalse(self.enemy.can_cast())

    def test_get_health(self):
        self.assertEqual(self.enemy.get_health(), 100)

    def test_get_mana(self):
        self.assertEqual(self.enemy.get_mana(), 100)

    def test_take_healing_enemy_dead(self):
        self.enemy.health = 0
        self.assertFalse(self.enemy.take_healing(50))

    def test_take_healing_enemy_alive(self):
        self.enemy.health = 10
        self.assertTrue(self.enemy.take_healing(50))

    def test_take_healing_enemy_with_more_health(self):
        self.enemy.health = 90
        self.enemy.take_healing(50)
        self.assertEqual(self.enemy.health, 100)

    def test_take_mana(self):
        self.enemy.mana = 20
        self.enemy.take_mana(20)
        self.assertEqual(self.enemy.mana, 40)


if __name__ == '__main__':
    unittest.main()
