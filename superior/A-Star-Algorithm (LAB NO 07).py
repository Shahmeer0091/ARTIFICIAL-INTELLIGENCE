class Node:
    def __init__(self, value, x, y):
        self.value = value
        self.x = x
        self.y = y
        self.neighbors = []
        self.g = float('inf')
        self.h = float('inf')
        self.f = float('inf')
        self.parent = None

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)


def heuristic(node, goal):
    return abs(node.x - goal.x) + abs(node.y - goal.y)


def a_star_algorithm(start_node, goal_node):
    open_list = [start_node]
    closed_list = []
    
    start_node.g = 0
    start_node.h = heuristic(start_node, goal_node)
    start_node.f = start_node.g + start_node.h
    
    while open_list:
        open_list.sort(key=lambda x: x.f)
        current_node = open_list.pop(0)
        
        if current_node == goal_node:
            return reconstruct_path(current_node)
        
        closed_list.append(current_node)
        
        for neighbor in current_node.neighbors:
            if neighbor in closed_list:
                continue
            
            tentative_g = current_node.g + 1

            if tentative_g < neighbor.g:
                neighbor.parent = current_node
                neighbor.g = tentative_g
                neighbor.h = heuristic(neighbor, goal_node)
                neighbor.f = neighbor.g + neighbor.h

                if neighbor not in open_list:
                    open_list.append(neighbor)

    return None


def reconstruct_path(node):
    path = []
    current = node
    while current is not None:
        path.append(current.value)
        current = current.parent
    return path[::-1]


node_A = Node('A', 0, 0)
node_B = Node('B', 1, 0)
node_C = Node('C', 2, 0)
node_D = Node('D', 0, 1)
node_E = Node('E', 1, 1)
node_F = Node('F', 2, 1)
node_G = Node('G', 0, 2)
node_H = Node('H', 1, 2)
node_I = Node('I', 2, 2)

node_A.add_neighbor(node_B)
node_A.add_neighbor(node_D)

node_B.add_neighbor(node_A)
node_B.add_neighbor(node_C)
node_B.add_neighbor(node_E)

node_C.add_neighbor(node_B)
node_C.add_neighbor(node_F)

node_D.add_neighbor(node_A)
node_D.add_neighbor(node_E)
node_D.add_neighbor(node_G)

node_E.add_neighbor(node_B)
node_E.add_neighbor(node_D)
node_E.add_neighbor(node_F)
node_E.add_neighbor(node_H)

node_F.add_neighbor(node_C)
node_F.add_neighbor(node_E)
node_F.add_neighbor(node_I)

node_G.add_neighbor(node_D)
node_G.add_neighbor(node_H)

node_H.add_neighbor(node_G)
node_H.add_neighbor(node_E)
node_H.add_neighbor(node_I)

node_I.add_neighbor(node_H)
node_I.add_neighbor(node_F)

path = a_star_algorithm(node_A, node_I)
print("Shortest path found by A*:", path)
