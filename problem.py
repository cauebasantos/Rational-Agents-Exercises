from node import Node
from node import insert_sorted
from node import insert_sorted_astar

class Problem:
    def __init__(self):
         # holds possible actions the agent can do
        self.possible_actions = ['UP', 'DOWN', 'LEFT', 'RIGHT']  

    @staticmethod
    def define_goal(state:list) -> list:
        #return [1,2,3,8,0,4,7,6,5]
        return [1,2,3,4,5,6,7,8,0]

    @staticmethod
    def can_move(state:list, direction:str) -> bool:
            void_index = state.index(0)
            if direction == 'UP':
                return void_index >= 3 
            elif direction == 'DOWN':
                return void_index <= 5 
            elif direction == 'LEFT':
                return void_index%3 != 0 
            elif direction == 'RIGHT':
                return (void_index+1)%3 != 0 

    @staticmethod
    def move_void_square(state:list, direction:str) -> list:
        state = state.copy()
        void_index = state.index(0)
        if Problem.can_move(state, direction):
            if direction == 'UP':
                state[void_index], state[void_index-3] = \
                state[void_index-3], state[void_index]
            elif direction == 'DOWN':
                state[void_index], state[void_index+3] = \
                state[void_index+3], state[void_index]
            elif direction == 'LEFT':
                state[void_index], state[void_index-1] = \
                state[void_index-1], state[void_index]
            elif direction == 'RIGHT':
                state[void_index], state[void_index+1] = \
                state[void_index+1], state[void_index]

            return state
    
        return None

    def apply_operators(self, node:Node, frontier:list, searchUC=False, 
        heuristic=False, cost_with_heuristic=False):
        for action in self.possible_actions:
            if Problem.can_move(node.content, action):
                node_content = Problem.move_void_square(node.content, action)
                node_parent = node
                node_path_cost = node.path_cost + 1
                node_action = action
                node_depth = node.depth + 1
                if node_content != None:
                    new_node = Node(node_content, node_action, node_parent, 
                        node_path_cost, node_depth)
                    
                    if heuristic or cost_with_heuristic:
                        self.apply_heuristic(new_node)

                    if cost_with_heuristic:
                        self.apply_cost_with_heuristic(new_node)
                        insert_sorted_astar(new_node, frontier)
                        return

                    if searchUC:
                        insert_sorted(new_node, frontier)
                    else:
                        frontier.append(new_node) 

                   


                
    def apply_heuristic(self, node:Node):
        score = 0
        state = node.content
        goal = self.define_goal(state)
        for i in range(len(state)):
            if state[i] == goal[i]:
                score += 1
        node.heuristic = score

    def apply_cost_with_heuristic(self, node:Node):
        node.cost_with_heuristic = node.path_cost + node.heuristic

