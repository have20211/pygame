from settings import *

text_map = [
    'WWWWWWWWWWWWWWWWWWWW',
    'W..................W',
    'W.WWW.W..W.WWW.W...W',
    'W..W.....W.W.W.W...W',
    'W..W..W..W.W.W.WWW.W',
    'W..W..W..W.W.W.W.W.W',
    'W..W..W..W.WWW.W.W.W',
    'W..................W',
    'W..WWW........WWW..W',
    'W..WWW........WWW..W',
    'W..................W',
    'WWWWWWWWWWWWWWWWWWWW',
]

world_map = set()
mini_map = set()
for row_index, row in enumerate(text_map):
    for col_index, col in enumerate(row):
        if col == 'W':
            world_map.add((col_index * TILE, row_index * TILE))
            mini_map.add((col_index * MAP_TILE, row_index * MAP_TILE))