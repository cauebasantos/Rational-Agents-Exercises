import math

class Node:
    def __init__(self, content, action, parent, path_cost=0, depth=0, 
    heuristic=0, cost_with_heuristic=0):
        self.content = content
        self.action = action
        self.parent = parent
        self.path_cost = path_cost
        self.depth = depth
        self.heuristic = heuristic
        self.cost_with_heuristic = cost_with_heuristic

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
    
def insert_sorted(node:Node, arr:list):
    pivot =  int(len(arr)/2)
    if pivot == 0:
        arr.insert(pivot, node)
        return
    elif pivot == len(arr) - 1:
        arr.insert(pivot, node)
        return
    else:
        right = arr[pivot]
        left =  arr[pivot - 1]
        if left.path_cost <= node.path_cost <= right.path_cost:
            arr.insert(pivot - 1, node)
            return
        elif node.path_cost <= left.path_cost:
            insert_sorted(node, arr[:pivot])
        else:
            insert_sorted(node, arr[pivot+1:])

def insert_sorted_astar(node:Node, arr:list):
    pivot =  int(len(arr)/2)
    if pivot == 0:
        arr.insert(pivot, node)
        return
    elif pivot == len(arr) - 1:
        arr.insert(pivot, node)
        return
    else:
        right = arr[pivot]
        left =  arr[pivot - 1]
        if left.cost_with_heuristic <= node.cost_with_heuristic <= \
        right.cost_with_heuristic:
            arr.insert(pivot - 1, node)
            return
        elif node.cost_with_heuristic <= left.cost_with_heuristic:
            insert_sorted_astar(node, arr[:pivot])
        else:
            insert_sorted_astar(node, arr[pivot+1:])