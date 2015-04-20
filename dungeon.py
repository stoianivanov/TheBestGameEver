from hero import Hero


class Dungeon:
    def __init__(self, file_path):
        lines = ""
        with open(file_path) as f:
            lines = f.read().split('\n')
        lines = [line.strip(" ") for line in lines]
        self.__dungeon = [list(line) for line in lines]
        self.__dungeon.pop(-1)
        self.__posX = -1
        self.__posY = -1

    @property
    def dungeon(self):
        return self.__dungeon

    @dungeon.setter
    def dungeon(self, value):
        self.__dungeon = value

    def print_map(self):
        for line in self.dungeon:
            print (''.join(line))

    def spawn(self, hero):

        for x in range(0, len(self.dungeon)):
            for y in range(0, len(self.dungeon[x])):
                if self.dungeon[x][y] == 'S':
                    self.__posX = x
                    self.__posY = y
                    self.dungeon[x][y] = 'H'
                    return True
        return False

    def out_of_map(self, X, Y):
        if X not in range(0, len(self.dungeon[0])):
            return True
        if Y not in range(0, len(self.dungeon)):
            return True
        return False

    def is_obstacle(self, X, Y):
        if self.dungeon[X][Y] == '#':
            return True
        return False

    def move_hero(self, direction):
        pass




# d = Dungeon("level1.txt")
# d.print_map()
# h = Hero(name="Bron",
#             title="Dragonslayer",
#                          health=100, mana=100,
#                          mana_regeneration_rate=2)
# d.spawn(h)
# d.print_map()
