from hero import Hero
from enemies import Enemy
from spell import Spell


class Fights:
    START = "A fight is started between our Hero(health={}, mana={}) and Enemey(health={}, mana={}, damage={})"

    def __init__(self, hero, enemey):
        if isinstance(hero, Hero):
            self.hero = hero
        else:
            raise ValueError
        if isinstance(enemey, Enemy):
            self.enemey = enemey
        else:
            raise ValueError

    def start_fights(self):
        return self.START.format(self.hero.get_health(), self.hero.get_mana(), self.enemey.health, self.enemey.mana, self.enemey.damage)

    def hero_attack(self, by):
        if by == "spell":
            if self.hero.get_mana() > self.hero.learned_spell[0].get_mana_cost():
                self.hero.reduce_mana(self.hero.learned_spell[0].get_mana_cost())
                
