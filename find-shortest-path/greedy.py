class Edge :
    def __init__(self , firstNode , secondNode , distance) -> None:
        self.firstNode = firstNode
        self.secondNode = secondNode
        self.distance = distance
    def find_distance (self , node1 , node2):
        if node1 == self.firstNode and node2 == self.secondNode :
            return self.distance
        if node2 == self.firstNode and node1 == self.secondNode :
            return self.distance
        return -1
    def find_neighbor(self , node):
        if node == self.firstNode:
            return self.secondNode
        if node == self.secondNode:
            return self.firstNode
        return None

class Node:
    def __init__(self , name , heuristic , previousNode) -> None:
        self.name = name
        self.heuristic = heuristic
        self.previousNode = previousNode
    def get_total_distance(self):
        return self.heuristic
    def __str__(self) -> str:
        return self.name

heuristics = {'A':10 , 'B':8 , 'C':5 , 'D':7 , 'E':3 , 'F':6 , 'G':5 , 'H':3 , 'I':1 , 'J':0}
edges = [Edge('A', 'B' , 6) , Edge('B', 'C' , 3) , Edge('C', 'D' , 1) , Edge('B', 'D' , 2) , Edge('C', 'E' , 5) ,
        Edge('D', 'E' , 8) , Edge('E', 'J' , 5) , Edge('E', 'I' , 5) , Edge('I', 'J' , 3) , Edge('A', 'F' , 3) ,
        Edge('F', 'G' , 1) , Edge('F', 'H' , 7) , Edge('G', 'I' , 3) , Edge('H', 'I' , 2)]



def find_edge_distance(node1 , node2):
    for e in edges:
        if e.find_distance(node1 , node2) != -1:
            return e.find_distance(node1 , node2)
    return -1

def find_neighbors(node):
    neighbors = []
    for e in edges:
        if e.find_neighbor(node) != None:
            neighbors.append(e.find_neighbor(node))
    return neighbors


openNodes = []
currentNode = Node('A' , heuristics['A'] , None)
while True:
    neighbors = find_neighbors(currentNode.name)
    for node in neighbors:
        neighborNode = Node(node , heuristics[node], currentNode)
        openNodes.append(neighborNode)

    minTotoal = 1000
    minIndex = 0
    for node , index in zip(openNodes , range(len(openNodes))):
        if minTotoal > node.get_total_distance():
            minTotoal = node.get_total_distance()
            minIndex = index

    currentNode = openNodes.pop(minIndex)

    print('min total : ' , minTotoal)
    #print('open nodes : ' , openNodes)
    print('current node : ' , currentNode)

    if currentNode.name == 'J':
        break

path = []
while currentNode != None:
    path.append(currentNode.name)
    currentNode = currentNode.previousNode

path.reverse()
print('path:' , path)