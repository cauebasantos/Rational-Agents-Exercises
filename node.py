class Node:
    def __init__(self, content, action, parent, path_cost=1):
        self.content = content
        self.action = action
        self.parent = parent
        self.path_cost = path_cost


    def __repr__(self):
        return f'<Node Object> state: {self.content}, action: {self.action}, path_cost: {self.path_cost}'
    