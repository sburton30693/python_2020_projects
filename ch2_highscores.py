# Spencer Burton

# create and initialize ten name variables
name0 = "BossLady"
name1 = "Jerry"
name2 = "syrup"
name3 = "Orange"
name4 = "Juice"
name5 = "Pelican"
name6 = "Lemonade"
name7 = "child"
name8 = "banana"
name9 = "apple"

# create and initialize ten score variables
score0  = 1000
score1  = 999
score2  = 812
score3  = 765
score4  = 600
score5  = 544
score6  = 432
score7  = 431
score8  = 399
score9  = 100

seperator = "-"
wall = "|"

# print a title for the high scores list
print(str.format(wall + "{0:^18.18}" + wall, "High Score"))
print(str.format(wall + "{0:^18.18}" + wall, "=================="))

# print each of the score lines, using string formatting
format_string = wall + " {:^8.8} " + seperator + " {:>5,} " + wall

print(str.format(format_string, name0, score0))
print(str.format(format_string, name1, score1))
print(str.format(format_string, name2, score2))
print(str.format(format_string, name3, score3))
print(str.format(format_string, name4, score4))
print(str.format(format_string, name5, score5))
print(str.format(format_string, name6, score6))
print(str.format(format_string, name7, score7))
print(str.format(format_string, name8, score8))
print(str.format(format_string, name9, score9))
print(str.format("\\{0:^18.18}/", "__________________"))
