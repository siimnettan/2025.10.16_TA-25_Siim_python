# Sokoban terminaliversioon
# Sümbolid: # = sein, . = tühi, F = eesmärk, B = kast, Y = mängija

grid = [
    list("#######"),
    list("#F.####"),
    list("#FB...#"),
    list("#YB.B.#"),
    list("###F..#"),
    list("#######")
    
]

player_pos = (3, 1)  # Y algpositsioon

def print_grid():
    for row in grid:
        print(" ".join(row))
    print()

def move(dx, dy):
    global player_pos
    x, y = player_pos
    nx, ny = x + dx, y + dy  # uus mängija positsioon

    # Kui järgmine ruut on sein
    if grid[nx][ny] == "#":
        return

    # Kui järgmine ruut on kast
    if grid[nx][ny] == "B":
        bx, by = nx + dx, ny + dy  # kasti uus positsioon
        if grid[bx][by] in [".", "F"]:  # saab lükata
            grid[bx][by] = "B"
            grid[nx][ny] = "Y"
            grid[x][y] = "." if (x, y) not in goals else "F"
            player_pos = (nx, ny)
    elif grid[nx][ny] in [".", "F"]:
        grid[nx][ny] = "Y"
        grid[x][y] = "." if (x, y) not in goals else "F"
        player_pos = (nx, ny)

def is_win():
    return all(grid[x][y] == "B" for (x, y) in goals)

# Leia eesmärgid
goals = [(i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == "F"]

print("Sokoban terminaliversioon. Liigu WASD-ga. Eesmärk: kõik kastid F-ruutudele!")
print_grid()

while True:
    cmd = input("Käsk (W/A/S/D): ").lower()
    if cmd == "w": move(-1, 0)
    elif cmd == "s": move(1, 0)
    elif cmd == "a": move(0, -1)
    elif cmd == "d": move(0, 1)
    else:
        print("Vale käsk!")
        continue

    print_grid()
    if is_win():
        print("Tubli! Kõik kastid on kohal!")
        break