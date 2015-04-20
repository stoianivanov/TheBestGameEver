from hero import Hero
from enemies import Enemy
from spell import Spell


class Fights:
    START = "A fight is started between our Hero(health={}, mana={}) and Enemy(health={}, mana={}, damage={})"
    SPELL_ATTACK = "Hero casts a {}, hits enemy for {} dmg. Enemy health is {}"
    def __init__(self, hero, enemy):
        if isinstance(hero, Hero):
            self.hero = hero
        else:
            raise ValueError
        if isinstance(enemy, Enemy):
            self.enemy = enemy
        else:
            raise ValueError

    def start_fights(self):
        return self.START.format(self.hero.get_health(), self.hero.get_mana(), self.enemy.health, self.enemy.mana, self.enemy.damage)

    def hero_attack(self, by):
        if by == "spell":
            if self.hero.get_mana() > self.hero.learned_spell[0].get_mana_cost():
                self.hero.reduce_mana(self.hero.learned_spell[0].get_mana_cost())
                self.enemy.health -= self.hero.learned_spell[0].get_damage()
                spell = self.hero.learned_spell[0]
                self.enemy -= spell.get_damage()
                return self.SPELL_ATTACK.format(spell.get_name(), spell.get_damage(), self.enemy.health)
            else :
                by = "weapon"
        if by == "weapon":
            pass
