""" Agent Class

"""

from game import Game
from node import Node

class Agent:
    def __init__(self, state:list):
        # holds the environment the agent is going to manipulate
        self.environment = Game(state)
        # holds the goal state the agent needs to achieve
        self.goal = [1,2,3,8,0,4,7,6,5]
        # holds the stack sequence of actions the agent is going to do to 
        # achieve his goal
        self.solve_stack = [] 
        # holds possible actions the agent can do
        self.possible_actions = ['UP', 'DOWN', 'LEFT', 'RIGHT']  

    def search_solution(self) -> bool:
        """ Search the sequence of actions that leads to the goal state and puts
        it on self.solve_stack variable 
        """

        # get the current state of the environment
        state = self.environment.get_state()  
        # create the root node with the current state
        root = Node(state, 'None', None)  
        frontier = [root]  # create the frontier queue and append the root to it

        while frontier:  # while frontier is not empty
            node = frontier.pop(0)  # pop the first node on the frontier
            
            # if this node is the goal state
            if node.content == self.goal:
                # append all the nodes parents while it's not the root node
                self.solve_stack.append(node)  
                while node.parent.parent != None:  
                    node = node.parent
                    self.solve_stack.append(node)
                # since we found a solution
                return True

            # if the state is not the goal state
            self.apply_operators(node, frontier)

        # if we don't found any soluction
        return False
            
    
    def do_action(self):
        """ Performs the agent action, it might be search for a solve sequence 
        or execute some state
        """
        # if we already have a solution
        if self.solve_stack:
            # pop the next step 
            state = self.solve_stack.pop(-1).content
            # apply the solution on environment
            self.environment.set_state(state)
            self.print_state(state)
        else:
            # search for a solution
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
    
    def apply_operators(self, node:Node, queue:list):
        for action in self.possible_actions:
            if self.can_move(node.content, action):
                node_content = self.move_void_square(node.content, action)
                node_parent = node
                node_path_cost = 1
                node_action = action
                if node_content != None:
                    queue.append(Node(node_content, node_action, node_parent, 
                    node_path_cost)) 
   
    def print_state(self, state:list):
        for i in range(3):
            print(f"{state[i*3]} {state[i*3 + 1]} {state[i*3 + 2]}")
        print()
