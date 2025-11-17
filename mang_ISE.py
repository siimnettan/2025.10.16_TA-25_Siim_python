# Samm 1: Mänguvälja printimine

# Näita, kuidas teha print_grid() funktsioon.
# Harjutus: muuda sümboleid ja vaata, mis juhtub.

grid = [
    ### tyhi plats
    # list("#####"),  # ülemine sein
    # list("#...#"),  # tühi väli
    # list("#...#"),  # tühi väli
    # list("#...#"),  # tühi väli
    # list("#####")   # alumine sein
    ### level 1 plats
    # list("#####"),  # ülemine sein
    # list("#...#"),  # tühi väli
    # list("#YBF#"),  # üks käik paremale
    # list("#...#"),  # tühi väli
    # list("#####")   # alumine sein
    ### level 2 plats
    list("#######"),  # ülemine sein
    list("#.....#"),  # tühi väli
    list("#Y.B.F#"),  # kolm käiku paremale
    list("#.....#"),  # tühi väli
    list("#######")   # alumine sein
    ### level 8 plats
    # list("#######"),
    # list("#F.####"),
    # list("#FB...#"),
    # list("#YB.B.#"),
    # list("###F..#"),
    # list("#######")
]

def print_grid():
    for row in grid:          # copilot õpetuses oli i asemel row
        print(" ".join(row))    # tavaliselt tsüklites i, mitte row
    print()

print_grid()

# Samm 2: Leia mängija ja eesmärgid

player_pos = (3, 1)
goals = [(i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == "F"]
print(goals)
# ISE õppimiseks lisan
print("F asukoht platsil", goals)
print("platsi mõõtmed", len(grid))
print("F asukoht platsil", player_pos)


# Samm 3: Liikumine ilma kastideta

def move(dx, dy):
    global player_pos
    x, y = player_pos
    nx, ny = x + dx, y + dy
    if grid[nx][ny] in [".", "F"]:
        grid[nx][ny] = "Y"
        grid[x][y] = "." if (x, y) not in goals else "F"
        player_pos = (nx, ny)

if grid[nx][ny] == "#": 
    return
