from weapon import Weapon
from spell import Spell


class Hero:
    def __init__(self, name, title, health=100,
                 mana=100, mana_regeneration_rate=2):
        self.__name = name
        self.__title = title
        self.__health = health
        self.__mana = mana
        self.__mana_regeneration_rate = mana_regeneration_rate
        self.weapon_equipment = []
        self.learned_spell = []

    def name(self):
        return self.__name

    def title(self):
        return self.__title

    def get_health(self):
        return self.__health

    def get_mana(self):
        return self.__mana

    def mana_regeneration_rate(self):
        return self.__mana_regeneration_rate

    def known_as(self):
        return "{} the {}".format(self.name, self.title)

    def is_alive(self):
        return self.get_health() > 0

    def can_cast(self):
        return self.get_mana() > 0

    def take_damage(self, damage_points):
        current_health = self.get_health()
        damage = current_health - damage_points
        if damage < 0:
            self.__health = 0
        self.__health = damage
        return self.get_health()

    def reduce_mana(self, mana_reducing_points):
        self.__mana -= mana_reducing_points
        return self.get_mana()

    def reduce_health(self, dying_points):
        if dying_points >= self.__health:
            self.__health = 0
            self.is_alive = False
            return 0
        self.__health -= dying_points
        return self.get_health()

    def take_healing(self, healing_points):
        if self.is_alive() == False:
            return False
        maximum_health = 100
        current_health = self.get_health()
        self.__health += current_health
        if current_health + healing_points > maximum_health:
            self.__health = 100
        return True

    def make_move(self):
        pass

    def take_mana(self, mana_points):
        if self.make_move():
            self.__mana += self.__mana_regeneration_rate
        max_mana = 100
        current_mana = self.get_mana()
        if self.get_health() < current_mana:
            self.__health = current_mana
        current_mana += mana_points
        if current_mana > max_mana:
            self.__mana = 100
        return self.get_mana()

    def equip(self, weapon):
        if len(self.weapon_equipment) == 1:
            current_weapon = self.weapon_equipment[0]
            self.weapon_equipment.remove(current_weapon)
        self.weapon_equipment.append(weapon)

    def learn(self, spell):
        if len(self.learned_spell) == 1:
            current_spell = self.learned_spell[0]
            self.learned_spell.remove(current_spell)
        self.learned_spell.append(spell)

    def attack(self, by):
        if by == "weapon":
            if len(self.weapon_equipment) == 1:
                damage = self.weapon_equipment[0].get_damage()
                return damage
        if by == "spell":
            if len(self.learned_spell) == 1:
                self.reduce_mana(self.learned_spell[0].get_mana_cost())
                damage = self.learned_spell[0].get_damage()
                return damage
        return 0


# h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
# spell = Spell(name="Fireball",
#                               damage=30,
#                               mana_cost=50,
#                               cast_range=2)
# h.learn(spell)
# print(h.attack("spell"))
