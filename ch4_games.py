# Spencer Burton
# 10/7/20
# Chapter 4, list/array and tuple examples

# Not necessarily in order
game1  = "Portal 2"
game2  = "The Legend of Zelda: A Link to the Past"
game3  = "Super Mario Galaxy"
game4  = "The Legend of Zelda: Breath of the Wild"
game5  = "Earthbound"
game6  = "Borderlands 2"
game7  = "The Legend of Zelda: A Link between Worlds"
game8  = "A Hat in Time"
game9  = "Star Wars Battlefront 2 (2005)"
game10 = "The Legend of Zelda: Majoras Mask 3D"
game11 = "Super Mario Sunshine"
game12 = "Metal Arms"
game13 = "Mario Kart 8 Deluxe"
game14 = "Minecraft"
game15 = "The Legend of Zelda: Twilight Princess"
game16 = "Lord of the Rings Conquest"
game17 = "Super Smash Bros Ultimate"
game18 = "Super Mario World"
game19 = "Pokemon Emerald"
game20 = "Half Life 2"
game21 = "Fancy Pants Adventure"
game22 = "Super Metriod"
game23 = "Antichamber"
game24 = "Tetris"
game25 = "Super Mario 64"

top_games = [game1,
             game2,
             game3,
             game4,
             game5,
             game6,
             game7,
             game8,
             game9,
             game10,
             game11,
             game12,
             game13,
             game14,
             game15,
             game16,
             game17,
             game18,
             game19,
             game20,
             game21,
             game22,
             game23,
             game24,
             game25]

if "World of Warfcraft" in top_games :
    print("Pass")
else :
    print("Fail")

if top_games[0] != "The Legend of Zelda: A Link to the Past" :
    print("Fail")
else :
    print("Pass")

for i in top_games :
    if "Pokemon" in i or "Halo" in i :
        print("Fail")

# Examples 
# top_games[0] = "something else"
# top_games[1] = "something else"
# top_games[2] = "something else"
# top_games.append("new game")

# print(top_games)

# Tuple, is Immutable, i.e. can't be changed
# CLASS_LIST = ("Bob", "Tim", "Frank", "Eric")

# Functions for lists and tuples
# len(), max(), min()
