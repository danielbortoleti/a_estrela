from cmath import sqrt
import random as rand
from map_contructor import *
import numpy as np
from a_star import a_star

class Game:

    def test_obj(self,map,array_size):
        return map[array_size - 1] == 0

    def generate_suc(self, state):
        successors = []

        positions = state.index(0)
        expansions = [self._right, self._left, self._up, self._down]
        rand.shuffle(expansions)
        for expansion in expansions:
            successor = expansion(positions, state)
            if successor is not None: successors.append(successor)

        return successors

    def _left(self, positions, current_state):
        left = []
        for i in range(len(map)):
            if i == 0 or i % N == 0:
                left.append(i)
        if positions not in left and 0 < current_state[positions-1]:
            successor = list(current_state)
            successor[positions] = -2
            successor[positions - 1] = 0
            return (tuple(successor), "⬅️",current_state[(positions - 1)])

    def _up(self, positions, current_state):
        up = []
        for i in range(len(map)):
            if 0 <= i < N:
                up.append(i)
        if positions not in up and 0 < current_state[positions-N]:
            sucesso = list(current_state)
            sucesso[positions] = -2
            sucesso[positions - N] = 0
            return (tuple(sucesso), "⬆️",current_state[(positions - N)])

    def _down(self, positions, current_state):
        down = []
        for i in range(len(map)):
            if len(map) % 2 == 0:
                if i >= (M * N) - M:
                    down.append(i)
            else:
                if i >= (M * N) - N:
                    down.append(i)
        if positions not in down and 0 < current_state[positions+M]:
            successor = list(current_state)
            successor[positions] = -2
            successor[positions + M] = 0
            return (tuple(successor), "⬇️",current_state[(positions + M)])

    def _right(self, positions, current_state):
        right = []
        for i in range(len(map)):
            if (i + 1) % N == 0 :
                right.append(i)
        if positions not in right and 0 < current_state[positions + 1]:      
            successor = list(current_state)
            successor[positions] = -2
            successor[positions + 1] = 0
            return (tuple(successor), "➡️",current_state[(positions + 1)])

    def manhattan(self, state):
        map_matrix = np.reshape(state, (M, N))
        x = 0
        y = 0
        for i in range(len(map_matrix)):
            for j in range(len(map_matrix[i])):
                if map_matrix[i][j] == 0:
                    x = i
                    y = j
                    return self.manhattan_dis(x,y)

    
    def manhattan_dis(self,i, j):
        return abs(i-(M - 1))+abs(j-(N - 1))


    def cost(self, state_origin, state_destiny):
        return state_origin + state_destiny


        

if __name__ == "__main__":
    g = Game()
    terrains = {'T':1,'A': 3,'Am': 6,'B':-1}
    M = int(input("Qual a matriz desejada? "))
    N = M
    array_size = M * N
    map = create_map(array_size,terrains)
    map_values = tuple(create_map_values(array_size,terrains,map))
    map_matrix = np.reshape(map, (M, N))
    map_matrixValues = np.reshape(map_values, (M, N))
    print(map_matrix)
    Manhattan = a_star(map_values, 
                            g.test_obj, 
                            g.generate_suc, 
                            g.manhattan,
                            g.cost,
                            M,
                            N)
    if(Manhattan is None):
        print("\nProblema sem solução :( \n")
    else:
        print("\nResultado:")
        print("\nCusto: " + str(Manhattan[0]))
        print("\npaths: " + str(Manhattan[1]))