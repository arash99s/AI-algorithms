import random as rn
import numpy as np



class Edge :
    def __init__(self , firstNode , secondNode , distance , pheromone = 1) -> None:
        self.firstNode = firstNode
        self.secondNode = secondNode
        self.distance = distance
        self.pheromone = pheromone

    def find_neighbor(self , node):
        if node == self.firstNode:
            return self.secondNode
        if node == self.secondNode:
            return self.firstNode
        return None
    def equal(self , node1 , node2):
        if node1 == self.firstNode and node2 == self.secondNode :
            return True
        if node1 == self.secondNode and node2 == self.firstNode :
            return True
        return False
    def __str__(self) -> str:
        return '('+self.firstNode+self.secondNode+') pheromone: ' + str(self.pheromone)

class Node:
    def __init__(self , name , heuristic , previousNode) -> None:
        self.name = name
        self.heuristic = heuristic
        self.previousNode = previousNode
    def get_total_distance(self):
        return self.heuristic
    def __str__(self) -> str:
        return self.name

edges = [Edge('A', 'B' , 6) , Edge('B', 'C' , 3) , Edge('C', 'D' , 1) , Edge('B', 'D' , 2) , Edge('C', 'E' , 5) ,
        Edge('D', 'E' , 8) , Edge('E', 'J' , 5) , Edge('E', 'I' , 5) , Edge('I', 'J' , 3) , Edge('A', 'F' , 3) ,
        Edge('F', 'G' , 1) , Edge('F', 'H' , 7) , Edge('G', 'I' , 3) , Edge('H', 'I' , 2)]

n_ants = 4
n_best = 2
n_iterations = 40
decay = 0.9

def find_edge_distance(node1 , node2):
    for e in edges:
        if e.equal(node1 , node2):
            return e.distance
    return -1

def find_edge_pheromone(node1 , node2):
    for e in edges:
        if e.equal(node1 , node2):
            return e.pheromone
    return -1

def set_edge_pheromone(node1 , node2 , pheromone):
    for e in edges:
        if e.equal(node1 , node2):
            e.pheromone = pheromone
            return

def decay_edges_pheromone(d):
    for e in edges:
        e.pheromone = e.pheromone * d

def find_neighbors(node):
    neighbors = []
    for e in edges:
        if e.find_neighbor(node) != None:
            neighbors.append(e.find_neighbor(node))
    return neighbors

def gen_all_paths():
    all_paths = []
    for i in range(n_ants):
        path = gen_path('A' , 'J')
        if path[-1][1] == 'J':
            all_paths.append((path, gen_path_dist(path)))
    return all_paths

def gen_path(start, end):
    path = []
    visited = [start]
    prev = start
    while prev != end:
        move = pick_move(prev, visited)
        if move == None:
            break
        path.append((prev, move))
        prev = move
        visited.append(move)
    # path.append((prev, start)) # going back to where we started    
    return path

def pick_move(node, visited_list):
    neighbors = find_neighbors(node)
    valid_moves = []
    for neighbor in neighbors:
        if neighbor in visited_list:
            continue
        valid_moves.append(neighbor)
    
    if len(valid_moves) == 0:
        return None

    max_valid_move = max(valid_moves , key=lambda move : find_edge_pheromone(node , move))
    randThr = 0.3
    if (rn.random() > randThr):
        return max_valid_move
    return rn.choice(valid_moves)

def gen_path_dist(path):
    sum_dist = 0
    for edge in path:
        sum_dist += find_edge_distance(edge[0] , edge[1])
    return sum_dist


def spread_pheronome(all_paths, n_best):
        sorted_paths = sorted(all_paths, key=lambda x: x[1]) # sort by path distance
        for path, dist in sorted_paths[:n_best]:
            for edge in path: # path : list of pair nodes
                prePheromone = find_edge_pheromone(edge[0] , edge[1])
                edgeDist = find_edge_distance(edge[0] , edge[1])
                set_edge_pheromone(edge[0] , edge[1] , prePheromone + (1.0 / edgeDist))
################################################## main loop
shortest_path = None
all_time_shortest_path = ("placeholder", np.inf)
for i in range(n_iterations):
    all_paths = gen_all_paths() 
    spread_pheronome(all_paths, n_best)
    shortest_path = min(all_paths, key=lambda x: x[1]) # path : list of pair nodes + edge distance
    print (shortest_path)
    if shortest_path[1] < all_time_shortest_path[1]:
        all_time_shortest_path = shortest_path            
    decay_edges_pheromone(decay)           

print(all_time_shortest_path)


print('&&&&&&&&&&&&&& edges:')
for e in edges:
    print(e)