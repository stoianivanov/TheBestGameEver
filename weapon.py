class Weapon:
    def __init__(self, name, damage):
        self.__name = name
        self.__damage = damage

    def get_name(self):
        return self.__name

    def get_damage(self):
        return self.__damage
