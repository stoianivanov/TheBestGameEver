class Hero:
    def __init__(self, name, title, health=100,
                 mana=100, mana_regeneration_rate=2):
        self.__name = name
        self.__title = title
        self.__health = health
        self.__mana = mana
        self.__mana_regeneration_rate = mana_regeneration_rate

    @property
    def name(self):
        return self.__name

    @property
    def title(self):
        return self.__title

    def get_health(self):
        return self.__health

    def get_mana(self):
        return self.__mana

    @property
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

    def take_healing(self, healing_points):
        if self.is_alive() == False:
            return False
        maximum_health = 100
        current_health = self.get_health()
        self.__health += current_health
        if current_health + healing_points > maximum_health:
            self.__health = 100
        return True

    def take_mana(self, mana_points):
        max_mana = 100
        current_mana = self.get_mana()
        if self.get_health() < current_mana:
            self.__health = current_mana
        current_mana += mana_points
        if current_mana > max_mana:
            self.__mana = 100
        return self.get_mana()

# h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
# print(h.take_damage(20))
