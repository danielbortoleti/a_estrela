import random as rand

import numpy as np
def create_map(array_size,dictionary):
    map = [None] * array_size
    key_list = list(dictionary.keys())
    for i in range(array_size):
        if i == array_size - 1:
            map[i] = key_list[rand.randrange(0,3)]
            return map
        else:
            if i == 0:
                map[i] = "J"
            else:    
                map[i]= key_list[rand.randrange(0,4)]

def create_map_values(array_size,dictionary,map):
    map_val = [None] * array_size
    for i in range(array_size):
        if i == 0:
            map_val[i] = 0
        else:
            map_val[i] = dictionary.get(map[i])
    return map_val

def vertex_path(no):
  path = []
  while no.node_parent is not None:
    no = no.node_parent
    if no.vertex is not None: path.append(no.vertex)
  path.reverse()
  return path