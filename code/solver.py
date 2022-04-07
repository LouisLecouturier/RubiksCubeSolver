#    _______________
#   /____/____/____/|
#  /____/____/____/||
# /____/____/____/|||
# |    |    |    ||/|
# |____|____|____|/||
# |    |    |    ||/|
# |____|____|____|/|/
# |    |    |    ||/
# |____|____|____|/


# OOO OOO OOO YYY WWW GGG BBB YYY WWW GGG BBB YYY WWW GGG BBB RRR RRR RRR

#     OOO
#     OOO
#     OOO
# WWW GGG YYY BBB
# BBB WWW GGG YYY
# BBB WWW GGG YYY
#     RRR
#     RRR
#     RRR


#     OOOOOOOOOWWWGGGYYYBBBBBBWWWGGGYYYBBBWWWGGGYYYRRRRRRRRR

# "doc" : https://pypi.org/project/rubik-solver/

from rubik_solver import utils
cube = 'wowgybwyogygybyoggrowbrgywrborwggybrbwororbwborgowryby'
# cube = 'OOOOOOOOOWWWGGGYYYBBBBBBWWWGGGYYYBBBWWWGGGYYYRRRRRRRRR'.lower()
print(cube)
print(utils.solve(cube, 'Beginner'))
print(utils.solve(cube, 'CFOP'))

# utils.solve(cube, 'Kociemba')