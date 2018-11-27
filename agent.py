'''

'''

from game import Game
from node import Node

class Agent:
    def __init__(self, state:list):
        self.environment = Game(state)  # holds the environment the agent is going to manipulate
        self.goal = [1,2,3,8,0,4,7,6,5]  # holds the goal state the agent needs to achieve
        self.solve_stack = []  # holds the stack sequence of actions the agent is going to do to achieve his goal
        self.possible_actions = ['UP', 'DOWN', 'LEFT', 'RIGHT']  # holds possible actions the agent can do

    def search_solution(self) -> bool:
        ''' Search the sequence of actions that leads to the goal state and puts it on self.solve_stack variable '''

        state = self.environment.get_state()  # get the current state of the environment
        root = Node(state, 'None', None)  # create the root node with the current state
        frontier = [root]  # create the frontier queue and append the root to it

        while frontier:  # while frontier is not empty
            node = frontier.pop(0)  # pop the first node on the frontier
            
            # if this node is the goal state
            if node.content == self.goal:  
                self.solve_stack.append(node) # 
                while node.parent.parent != None:
                    node = node.parent
                    self.solve_stack.append(node)
                return True

            # if the state is not the goal state
            self.apply_operators(node, frontier)

        # if we don't found any soluction
        return False
            
    
    def do_action(self):
        if self.solve_stack:
            state = self.solve_stack.pop(-1).content
            self.environment.set_state(state)
            self.print_state(state)
        else:
            self.search_solution()


    def can_move(self, state:list, direction:str) -> list:
        void_index = state.index(0)
        if direction == 'UP':
            return void_index >= 3 
        elif direction == 'DOWN':
            return void_index <= 5 
        elif direction == 'LEFT':
            return void_index%3 != 0 
        elif direction == 'RIGHT':
            return (void_index+1)%3 != 0 

    def move_void_square(self, state:list, direction:str) -> list:
        state = state.copy()
        void_index = state.index(0)
        if self.can_move(state, direction):
            if direction == 'UP':
                state[void_index], state[void_index-3] = state[void_index-3], state[void_index]
            elif direction == 'DOWN':
                state[void_index], state[void_index+3] = state[void_index+3], state[void_index]
            elif direction == 'LEFT':
                state[void_index], state[void_index-1] = state[void_index-1], state[void_index]
            elif direction == 'RIGHT':
                state[void_index], state[void_index+1] = state[void_index+1], state[void_index]
            return state
    
        return None
    
    def apply_operators(self, node:Node, queue:list):
        for action in self.possible_actions:
            if self.can_move(node.content, action):
                node_content = self.move_void_square(node.content, action)
                node_parent = node
                node_path_cost = 1
                node_action = action
                if node_content != None:
                    queue.append(Node(node_content, node_action, node_parent, node_path_cost)) 
   
    def print_state(self, state:list):
        for i in range(3):
            print(f"{state[i*3]} {state[i*3 + 1]} {state[i*3 + 2]}")
        print()
