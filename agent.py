from game import Game
from node import Node
class Agent:
    def __init__(self, state):
        self.environment = Game(state)
        self.goal = [1,2,3,8,0,4,7,6,5]
        self.seq = []
        self.possible_actions = ['UP', 'DOWN', 'LEFT', 'RIGHT']

    def search_solution(self):
        state = self.environment.get_state()
        root = Node(state, 'None', None)
        frontier = []
        frontier.append(root)

        while frontier:
            node = frontier.pop(0)
            if node.content == self.goal:
                self.seq.append(node)
                while node.parent.parent != None:
                    node = node.parent
                    self.seq.append(node)
                return True

            # if the state is not the goal state
            self.apply_operators(node, frontier)

            
    
    def do_action(self):
        if self.seq:
            state = self.seq.pop(-1).content
            self.environment.set_state(state)
            self.print_state(state)
        else:
            self.search_solution()


    def can_move(self, state, direction):
        void_index = state.index(0)
        if direction == 'UP':
            return void_index >= 3 
        elif direction == 'DOWN':
            return void_index <= 5 
        elif direction == 'LEFT':
            return void_index%3 != 0 
        elif direction == 'RIGHT':
            return (void_index+1)%3 != 0 

    def move_void_square(self, state, direction):
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
    
    def apply_operators(self, node, queue):
        for action in self.possible_actions:
            if self.can_move(node.content, action):
                node_content = self.move_void_square(node.content, action)
                node_parent = node
                node_path_cost = 1
                node_action = action
                if node_content != None:
                    queue.append(Node(node_content, node_action, node_parent, node_path_cost)) 
   
    def print_state(self, state):
        for i in range(3):
            print(f"{state[i*3]} {state[i*3 + 1]} {state[i*3 + 2]}")
        print()