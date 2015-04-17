class Enemy:
    def __init__(self, health=100, mana=100, damage=20):
        self.__health = health
        self.__mana = mana
        self.__damage = damage

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        self.__health = value

    @property
    def mana(self):
        return self.__mana

    @mana.setter
    def mana(self, value):
        self.__mana = value

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    def is_alive(self):
        return self.health > 0

    def can_cast(self):
        return self.mana > 0

    def get_health(self):
        return self.health

    def get_mana(self):
        return self.mana

    def take_healing(self, healing_points):
        if not self.is_alive():
            return False
        else:
            self.health += healing_points
            if self.health > 100:
                self.health = 100
            return True

    def take_mana(self, mana_points):
        max_mana = 100
        if self.health < self.mana:
            self.health = self.mana
        self.mana += mana_points
        if self.mana > max_mana:
            self.mana = max_mana
        return self.mana

    def attack(self):
        return self.damage

    def take_damage(self, damage_points):
        self.health -= damage_points
        if self.health < 0:
            self.health = 0
