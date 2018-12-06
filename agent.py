""" Agent Class

"""

from game import Game
from node import Node
from problem import Problem
from searchs import search_solution_bfs
from searchs import search_solution_dfs
from searchs import search_solution_uc
from searchs import search_solution_astar

class Agent:
    def __init__(self, state:list):
        # holds the environment the agent is going to manipulate
        self.environment = Game(state)
        # holds the stack sequence of actions the agent is going to do to 
        # achieve his goal
        self.solve_stack = [] 
       

    
    def do_action(self, problem:Problem):
        """ Performs the agent action, it might be search for a solve sequence 
        or execute some state
        """

        state = self.environment.get_state()

        # if we already have a solution
        if self.solve_stack:
            # pop the next step 
            node = self.solve_stack.pop(-1)
            # get the operation needed to get to this state 
            operation = node.action
            # apply the operator on environment
            self.environment.move_void_square(operation)
            # print the current state
            self.print_state(self.environment.get_state())
        else:
            # search for a solution
            #self.solve_stack = search_solution_bfs(state, problem, keep_history=True, history_len=1000)
            #self.solve_stack = search_solution_uc(state, problem, keep_history=True)
            #self.solve_stack = search_solution_dfs(state, problem, threshold=2, interactive=True)
            self.solve_stack = search_solution_astar(state, problem, keep_history=True, history_len=1023)

    def print_state(self, state:list):
        for i in range(3):
            print(f"{state[i*3]} {state[i*3 + 1]} {state[i*3 + 2]}")
        print()
