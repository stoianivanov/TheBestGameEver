from hero import Hero
from random import randint


class Dungeon:

    TREASURE = {
        "spell": {"Fireball": {"damage" : 30,
                               "mana_cost" : 50,
                               "cast_range": 2},
                  "Avada Kedavra": {"damage":100,
                                    "mana_cost":100,
                                    "cost_range":100},
                  "Crucio": {"damage":50,
                             "mana_cost":60,
                             "cost_range":10},
                  "Expelliarmus": {"damage":10,
                             "mana_cost":10,
                             "cost_range":5},
                  "Imperio": {"damage":30,
                             "mana_cost":10,
                             "cost_range":5},
                  "Oppugno": {"damage":20,
                             "mana_cost":10,
                             "cost_range":2}
                               },
        "mana": {"mana_points": 10},
        "weapon": {
                   "The Axe of Destiny": 20,
                   "Bomb": 35,
                   "Pistol": 10,
                   "Dual Pistols": 20,
                   "Lazer Gun": 15,
                   "Pipe Bombs": 10
                   },
        "health": {"healing_points": 20},
    }

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
        if X not in range(0, len(self.dungeon)):
            return True
        if Y not in range(0, len(self.dungeon[0])):
            return True
        return False

    def is_obstacle(self, X, Y):
        if self.dungeon[X][Y] == '#':
            return True
        return False

    def end_of_dungeon(self, pos_x, pos_y):
        if self.__dungeon[pos_x][pos_y] == 'G':
            print("You win")

    def move_hero(self, direction):
        new_pos_Y = self.__posY
        new_pos_X = self.__posX
        if direction == 'up':
            new_pos_X -= 1
        if direction == 'down':
            new_pos_X += 1
        if direction == 'left':
            new_pos_Y -= 1
        if direction == 'right':
            new_pos_Y += 1
        if self.is_obstacle(new_pos_X, new_pos_Y)\
           or self.out_of_map(new_pos_X, new_pos_Y):
            return False

        self.end_of_dungeon(new_pos_X, new_pos_Y)
        self.__dungeon[self.__posX][self.__posY] = '.'
        self.__posX = new_pos_X
        self.__posY = new_pos_Y
        self.__dungeon[self.__posX][self.__posY] = 'H'
        return True

    def pick_treasure(self):
        list_of_TREASURE = ["spell", "weapon", "mana", "health"]
        pick = randint(0, len(list_of_TREASURE)-1)
        if list_of_TREASURE[pick] == "spell":
            return self.TREASURE["spell"]["Imperio"]
        elif list_of_TREASURE[pick] == "mana":
            return self.TREASURE["mana"]
        elif list_of_TREASURE[pick] == "health":
            return self.TREASURE["health"]
        elif list_of_TREASURE[pick] == "weapon":
            return self.TREASURE["weapon"]["Bomb"]

    def hero_attack(by):
        pass

d = Dungeon("level1.txt")
d.print_map()
h = Hero(name="Bron",
         title="Dragonslayer",
         health=100, mana=100,
         mana_regeneration_rate=2)
d.spawn(h)
d.print_map()
"""d.move_hero('right')
d.print_map()
d.move_hero('right')"""
d.move_hero('down')
d.pick_treasure()
