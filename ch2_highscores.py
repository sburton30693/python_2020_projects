# create and initialize three name variables
# (name1, name2, name3)
name1  = "BossLady"
name2  = "Jerry   "
name3  = "syrup   "
name4  = "Orange  "
name5  = "Juice   "
name6  = "Pelican "
name7  = "Lemonade"
name8  = "child   "
name9  = "banana  "
name10 = "apple   "

# create and initialize three score variables
# (score1, score2, score3)
score1  = 1000
score2  = 999
score3  = 812
score4  = 765
score5  = 600
score6  = 544
score7  = 432
score8  = 431
score9  = 399
score10 = 100

# print a title for the high scores list
print("|     High Scores    |")
print("|====================|")

# print each of the three score lines in the pattern "name = score"

seperator = "-"
begin_wall = "|"
end_wall = "   " + begin_wall

print(begin_wall, name1 , seperator, str(score1) , end_wall)
print(begin_wall, name2 , seperator, str(score2) , " " + end_wall)
print(begin_wall, name3 , seperator, str(score3) , " " + end_wall)
print(begin_wall, name4 , seperator, str(score4) , " " + end_wall)
print(begin_wall, name5 , seperator, str(score5) , " " + end_wall)
print(begin_wall, name6 , seperator, str(score6) , " " + end_wall)
print(begin_wall, name7 , seperator, str(score7) , " " + end_wall)
print(begin_wall, name8 , seperator, str(score8) , " " + end_wall)
print(begin_wall, name9 , seperator, str(score9) , " " + end_wall)
print(begin_wall, name10, seperator, str(score10), " " + end_wall)

print("\\____________________/")
