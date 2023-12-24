from read_txt import contents

condition = {'red': 12, 'green': 13, 'blue': 14}
sum_possible_games = 0

for game in contents:

    possible = True
    colors={}
    num_game = int(game.split(':')[0].split(' ')[-1])

    sets = game.split(':')[1].split(';')

    for set in sets:
        cubes = set.split(',')

        for cube in cubes:
            color = cube.split(' ')[-1]
            number_cubes = int(cube.split(' ')[1])

            if color not in colors:
                colors.update({color: number_cubes})
            else:
                colors[color] = number_cubes if number_cubes > colors[color] else colors[color]

    power = 1     
    for color in colors:
        power *= colors[color]

    sum_possible_games+=power

print(sum_possible_games)
