import unittest
from spell import Spell


class SpellTest(unittest.TestCase):
    def setUp(self):
        self.my_spell = Spell(name="Fireball",
                              damage=30,
                              mana_cost=50,
                              cast_range=2)

    def test_create_spell(self):
        self.assertTrue(isinstance(self.my_spell, Spell))

    def test_get_name(self):
        self.assertEqual(self.my_spell.get_name(), "Fireball")

    def test_get_damage(self):
        self.assertEqual(self.my_spell.get_damage(), 30)

    def test_get_mana_cost(self):
        self.assertEqual(self.my_spell.get_mana_cost(), 50)

    def test_get_cast_range(self):
        self.assertEqual(self.my_spell.get_cast_range(), 2)

    def test_dunder_str(self):
        self.assertEqual(str(self.my_spell), "Fireball")

    def test_dunder_repr(self):
        self.assertEqual(repr(self.my_spell), "Fireball")
if __name__ == '__main__':
    unittest.main()
