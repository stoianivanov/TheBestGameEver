from hero import Hero
from random import randint
from spell import Spell
from weapon import Weapon
import random
from fights import *


class Dungeon:

    TREASURE = {
        "spell": [ Spell("Fireball",damage=30, mana_cost=50, cast_range=2),
                   Spell("Avada Kedavra",damage=100, mana_cost=100, cast_range=100),
                   Spell("Crucio",damage=50, mana_cost=60, cast_range=10),
                   Spell("Expelliarmus",damage=10, mana_cost=10, cast_range=5)],
        "mana": [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
        "weapon": [
                   Weapon("The Axe of Destiny", damage=20),
                   Weapon("Bomb", damage=35),
                   Weapon("Pistol", damage=10),
                   Weapon("Dual Pistols", damage=20),
                   Weapon("Lazer Gun", damage=15),
                   Weapon("Pipe Bombs", damage=10)
                   ],
        "health": [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
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
        self.hero = None
        self.enemy = Enemy(100, 50, 10)

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
        self.hero = hero
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

    def find_treasure(self, pos_x, pos_y):
        if self.__dungeon[pos_x][pos_y] == 'T':
            self.pick_treasure()

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
        if self.__dungeon[new_pos_X][new_pos_Y] == 'T':
            print(self.pick_treasure())
            print(self.hero.get_health())
            print(self.hero.get_mana())
        if self.__dungeon[new_pos_X][new_pos_Y] == 'E':
            self.hero_attack('spell')
            if not self.hero.is_alive():
                self.__dungeon[self.__posX][self.__posY] = '.'
                print("Game Over!!!!")
                return ''
        self.end_of_dungeon(new_pos_X, new_pos_Y)
        self.__dungeon[self.__posX][self.__posY] = '.'
        self.__posX = new_pos_X
        self.__posY = new_pos_Y
        self.__dungeon[self.__posX][self.__posY] = 'H'
        return True

    def hero_attack(self, by):
        fights = Fights(self.hero, self.enemy)
        while self.hero.is_alive() and self.enemy.is_alive():
            print(fights.hero_attack(by))
            if not self.enemy.is_alive() and self.hero.is_alive():
                break
            print(fights.enemy_attack())

        return True

    def pick_treasure(self):
        list_of_TREASURE = ["spell", "weapon", "mana", "health"]
        pick = randint(0, len(list_of_TREASURE)-1)
        if list_of_TREASURE[pick] == "spell":
            new_spell = random.choice(self.TREASURE["spell"])
            self.hero.learn(new_spell)
            string = "Learned a new spell: {}.".format(new_spell.get_name())
        elif list_of_TREASURE[pick] == "mana":
            mana_points = random.choice(self.TREASURE["mana"])
            self.hero.take_mana(mana_points)
            string = "Found mana potion. Hero mana is {}.".format(
                self.hero.get_mana())
        elif list_of_TREASURE[pick] == "health":
            healing_points = random.choice(self.TREASURE["health"])
            self.hero.take_healing(healing_points)
            string = "Found healing potion. Hero health is {}.".format(
                self.hero.get_health())
        elif list_of_TREASURE[pick] == "weapon":
            new_weapon = random.choice(self.TREASURE["weapon"])
            self.hero.equip(new_weapon)
            string = "Hero found new weapon: {}.".format(new_weapon.get_name())
        return string


d = Dungeon("level1.txt")
d.print_map()
h = Hero(name="Bron",
            title="Dragonslayer",
                         health=100, mana=100,
                         mana_regeneration_rate=2)
d.spawn(h)
d.print_map()
d.move_hero("right")
d.move_hero('down')
d.print_map()
d.move_hero('down')
d.move_hero('down')
d.move_hero("right")
d.print_map()
d.move_hero("right")
d.move_hero("right")
d.move_hero("right")
d.move_hero("up")
