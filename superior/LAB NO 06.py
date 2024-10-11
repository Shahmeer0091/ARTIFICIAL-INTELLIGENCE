# BFS without Queue & without Node

def bfs(graph, start):
    visited = []
    level = [start]
    
    while level:
        next_level = []
        for node in level:
            if node not in visited:
                visited.append(node)
                next_level.extend(graph[node])
        level = next_level
    
    return visited


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

print("BFS Traversal: ", bfs(graph, 'A'))

#TASK NO 02

# BFS with Queue & Node
from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []

    def add_neighbor(self, neighbor_node):
        self.neighbors.append(neighbor_node)


def bfs_with_queue(start_node):
    visited = set()
    queue = deque([start_node])
    result = []
    
    while queue:
        current_node = queue.popleft()
        
        if current_node not in visited:
            visited.add(current_node)
            result.append(current_node.value)
            
            for neighbor in current_node.neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)
    
    return result


node_A = Node('A')
node_B = Node('B')
node_C = Node('C')
node_D = Node('D')
node_E = Node('E')
node_F = Node('F')
node_G = Node('G')

node_A.add_neighbor(node_B)
node_A.add_neighbor(node_C)
node_B.add_neighbor(node_D)
node_B.add_neighbor(node_E)
node_C.add_neighbor(node_F)
node_C.add_neighbor(node_G)

print("BFS Traversal: ", bfs_with_queue(node_A))

