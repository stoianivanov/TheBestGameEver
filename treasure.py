from random import randint
treasures = {
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
list_of_treasures = ["spell", "weapon", "mana", "health"]
pick = randint(0, len(list_of_treasures)-1)
if list_of_treasures[pick] == "spell":
    print(treasures["spell"]["Imperio"])
elif list_of_treasures[pick] == "mana":
    print(treasures["mana"])
elif list_of_treasures[pick] == "health":
    print(treasures["health"])
elif list_of_treasures[pick] == "weapon":
    print(treasures["weapon"]["Bomb"])


