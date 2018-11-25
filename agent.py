from game import Game

class Agent:
    def __init__(self, state):
        self.environment = Game(state)
        self.goal = [0,1,2,3,4,5,6,7,8]
        self.seq = None

    def search_solution(self, state):
        if state == self.goal:
            return 'Found'
    
    def do_action(self):
        self.environment.set_state(self.move_void_square_up(self.environment.get_state()))
        self.print_state(self.environment.get_state())


    def can_move_up(self, state):
        void_index = state.index(0)
        return void_index >= 3

    def can_move_down(self, state):
        void_index = state.index(0)
        return void_index <= 5

    def can_move_left(self, state):
        void_index = state.index(0)
        return void_index%3 != 0

    def can_move_right(self, state):
        void_index = state.index(0)
        return (void_index+1)%3 != 0

    def move_void_square_up(self, state):
        state = state.copy()
        void_index = state.index(0)
        if self.can_move_up(state):
            state[void_index], state[void_index-3] = state[void_index-3], state[void_index]
        return state

    def move_void_square_down(self, state):
        state = state.copy()
        void_index = state.index(0)
        if self.can_move_down(state):
            state[void_index], state[void_index+3] = state[void_index+3], state[void_index]
        return state

    def move_void_square_left(self, state):
        state = state.copy()
        void_index = state.index(0)
        if self.can_move_left(state):
            state[void_index], state[void_index-1] = state[void_index-1], state[void_index]
        return state

    def move_void_square_right(self, state):
        state = state.copy()
        void_index = state.index(0)
        if self.can_move_right(state):
            state[void_index], state[void_index+1] = state[void_index+1], state[void_index]
        return state

    def print_state(self, state):
        for i in range(3):
            print(f"{state[i*3]} {state[i*3 + 1]} {state[i*3 + 2]}")