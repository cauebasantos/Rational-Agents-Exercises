class Game:
    def __init__(self, state):
        self.state = state
        
    def get_state(self):
        return self.state
    
    def can_move(self, direction:str) -> bool:
            void_index = self.state.index(0)
            if direction == 'UP':
                return void_index >= 3 
            elif direction == 'DOWN':
                return void_index <= 5 
            elif direction == 'LEFT':
                return void_index%3 != 0 
            elif direction == 'RIGHT':
                return (void_index+1)%3 != 0 

    def move_void_square(self, direction:str):
        void_index = self.state.index(0)
        if self.can_move(direction):
            if direction == 'UP':
                self.state[void_index], self.state[void_index-3] = \
                self.state[void_index-3], self.state[void_index]
            elif direction == 'DOWN':
                self.state[void_index], self.state[void_index+3] = \
                self.state[void_index+3], self.state[void_index]
            elif direction == 'LEFT':
                self.state[void_index], self.state[void_index-1] = \
                self.state[void_index-1], self.state[void_index]
            elif direction == 'RIGHT':
                self.state[void_index], self.state[void_index+1] = \
                self.state[void_index+1], self.state[void_index]

