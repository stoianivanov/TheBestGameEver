class Weapon:
    def __init__(self, name, damage):
        self.__name = name
        self.__damage = damage

    def get_name(self):
        return self.__name

    def get_damage(self):
        return self.__damage

    def __str__(self):
        return "{}".format(self.get_name())

    def __repr__(self):
        return str(self.__name)
