#task no 1
class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []

    def add_neighbor(self, neighbor_node):
        self.neighbors.append(neighbor_node)


def dfs_with_stack(start_node):
    stack = [start_node]
    visited = set()
    
    while stack:
        current_node = stack.pop()
        
        if current_node not in visited:
            visited.add(current_node)
            print(current_node.value)
            
            for neighbor in current_node.neighbors:
                if neighbor not in visited:
                    stack.append(neighbor)


node_A = Node('A')
node_B = Node('B')
node_C = Node('C')
node_D = Node('D')
node_E = Node('E')

node_A.add_neighbor(node_B)
node_A.add_neighbor(node_C)
node_B.add_neighbor(node_D)
node_C.add_neighbor(node_E)

dfs_with_stack(node_A)


#task no 02

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def preorder_traversal(root):
    if root:
        print(root.value, end=" ")
        preorder_traversal(root.left)
        preorder_traversal(root.right)


def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.value, end=" ")
        inorder_traversal(root.right)


def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.value, end=" ")


root = Node('A')
root.left = Node('B')
root.right = Node('C')
root.left.left = Node('D')
root.left.right = Node('E')
root.right.left = Node('F')
root.right.right = Node('G')

print("Preorder Traversal: ")
preorder_traversal(root)

print("\nInorder Traversal: ")
inorder_traversal(root)

print("\nPostorder Traversal: ")
postorder_traversal(root)
