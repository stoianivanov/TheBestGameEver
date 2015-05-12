from hero import Hero
from enemies import Enemy
from spell import Spell
from weapon import Weapon


class Fights:

    START ="A fight is started between our Hero(health={}, mana={}) and Enemy(health={}, mana={}, damage={})"
    SPELL_ATTACK = "Hero casts a {}, hits enemy for {} dmg. Enemy health is {}"
    ENEMY_ATTACK = "Enemy hits hero for {} dmg. Hero health is {}."
    WEAPON_ATTACK = "Hero hits with {} for {} dmg. Enemy health is {}"

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
        return self.START.format(
            self.hero.get_health(),
            self.hero.get_mana(),
            self.enemy.health,
            self.enemy.mana,
            self.enemy.damage
            )

    def enemy_attack(self):
        self.hero.reduce_health(self.enemy.damage)
        return self.ENEMY_ATTACK.format(
                self.enemy.damage,
                self.hero.get_health()
            )

    def hero_attack(self, by):
        if by == "spell":
            if len(self.hero.learned_spell) == 0:
                by = 'weapon'
            elif self.hero.get_mana() > self.hero.learned_spell[0].get_mana_cost():
                self.enemy.take_damage(self.hero.attack(by='spell'))
                spell = self.hero.learned_spell[0]
                return self.SPELL_ATTACK.format(
                                    spell.get_name(),
                                    spell.get_damage(),
                                    self.enemy.health
                                )
            else:
                by = "weapon"
        if by == "weapon":
            if len(self.hero.weapon_equipment) == 0:
                self.hero.reduce_health(100)
                return ''
            else:
                self.enemy.take_damage(self.hero.attack(by='weapon'))
                weapon = self.hero.weapon_equipment[0]
                return self.WEAPON_ATTACK.format(
                        weapon.get_name(),
                        weapon.get_damage(),
                        self.enemy.get_health()
                    )
