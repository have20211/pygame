from settings import *

text_map = [
    '11111111111111111111',
    '1..................1',
    '1..1111.2222.3333..1',
    '1.....1....2.......1',
    '1.1.3.2..1.........1',
    '1.3.1.23.2..232131.1',
    '1...3....1..1....3.1',
    '1..1312..2..231..1.1',
    '1..2..3..........3.1',
    '1..1..132.3121...2.1',
    '1..................1',
    '11111111111111111111',
]

world_map = {}
mini_map = set()
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char != '.':
            mini_map.add((i * MAP_TILE, j * MAP_TILE))
            if char == '1':
                world_map[(i * TILE, j * TILE)] = '1'
            elif char == '2':
                world_map[(i * TILE, j * TILE)] = '2'
            elif char == '3':
                world_map[(i * TILE, j * TILE)] = '3'
