import os


with open(os.path.join(os.path.dirname(__file__), "input.txt")) as f:
    datas = f.read().splitlines()

ans = 0
cube_limit = {"red": 12, "green": 13, "blue": 14}

for i, line in enumerate(datas, 1):
    rgb_cube = {"red": 0, "green": 0, "blue": 0}
    game_num, game_set = line.split(":")
    game_num = int(game_num[5:])
    game_set = game_set.split("; ")
    flag = True

    for game in game_set:
        cubes = game.split(", ")
        for cube in cubes:
            num, color = cube.split()
            rgb_cube[color] = max(rgb_cube[color], int(num))
            if rgb_cube[color] > cube_limit[color]:
                flag = False
                break

        if not flag:
            break

    if flag:
        ans += i

print(ans)
