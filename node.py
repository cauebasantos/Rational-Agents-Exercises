import math
class Node:
    def __init__(self, content, action, parent, path_cost=0, depth=0):
        self.content = content
        self.action = action
        self.parent = parent
        self.path_cost = path_cost
        self.depth = depth


    def __repr__(self):
        return f'<Node Object> state: {self.content}, action: {self.action}, \
        path_cost: {self.path_cost}, depth: {self.depth}'

def lowest_cost(arr:list):
    lowest = math.inf
    index = 0
    aux_index = 0
    for node in arr:
        if node.path_cost < lowest:
            lowest = node.path_cost
            index = aux_index
        aux_index += 1
    return index
    