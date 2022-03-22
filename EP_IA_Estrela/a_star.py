import numpy as np
import random as rand
import heapq
from map_contructor import *

class No:
      def __init__(self, state, node_parent=None, vertex=None, cost=0.0, heuristic=0.0,total=0.0):
        self.state = state
        self.node_parent = node_parent
        self.vertex = vertex
        self.cost = cost
        self.heuristic = heuristic
        self.total = self.cost + self.heuristic

def a_star(init_state, test_obj, generate_suc, heuristic, cost,M , N):
  queue = queue_P()
  queue.push(No(init_state, None, None, 0.0, heuristic(init_state),0.0))
  exit = [0,[]]
  cost_t = 0

  while not queue.empty():
    node_current = queue.pop()
    current_state = node_current.state
    
    print("\n\n")
    print(np.reshape(current_state, (M, N)))
    if(test_obj(current_state,len(current_state))):
      return exit
    
    #Função successora
    state_vertex_suc = generate_suc(current_state)
    movement = None
    for state_vet_suc in state_vertex_suc:
      no = No(state_vet_suc[0], node_current, state_vet_suc[1],state_vet_suc[2], heuristic(state_vet_suc[0]))
      if movement == None: 
        movement = no
      else:
        if no.state[-1] == 0:
          movement = no
        elif no.total < movement.total:
          movement = no
    try:
      cost_t += movement.cost
      exit[0] = cost_t
      exit[1].append(movement.vertex)
      queue.push(movement)
    except:
      return None
  return None

class queue_P:
  def __init__(self):
    self.queue = []
  
  def push(self, item):
    heapq.heappush(self.queue, item)
  
  def pop(self):
    if(self.empty()):
        return None
    else:
        return heapq.heappop(self.queue)

  def empty(self):
    return len(self.queue) == 0

    