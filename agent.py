""" Agent Class

"""

from game import Game
from node import Node
from node import lowest_cost
from problem import Problem
class Agent:
    def __init__(self, state:list):
        # holds the environment the agent is going to manipulate
        self.environment = Game(state)
        # holds the stack sequence of actions the agent is going to do to 
        # achieve his goal
        self.solve_stack = [] 
       

    def search_solution_bfs(self, problem:Problem) -> bool:
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
            if node.content == problem.define_goal(state):
                # append all the nodes parents while it's not the root node
                self.solve_stack.append(node)  
                while node.parent != None and node.parent.parent != None:  
                    node = node.parent
                    self.solve_stack.append(node)
                # since we found a solution
                return True

            # if the state is not the goal state
            problem.apply_operators(node, frontier)

        # if we don't found any soluction
        return False

    def search_solution_dfs(self, problem:Problem) -> bool:
        """ Search the sequence of actions that leads to the goal state and puts
        it on self.solve_stack variable 
        """

        # get the current state of the environment
        state = self.environment.get_state()  
        # create the root node with the current state
        root = Node(state, 'None', None)  
        frontier = [root]  # create the frontier stack and append the root to it

        while frontier:  # while frontier is not empty
            node = frontier.pop(-1)  # pop the last node on the frontier
            
            # if this node is the goal state
            if node.content == problem.define_goal(state):
                # append all the nodes parents while it's not the root node
                self.solve_stack.append(node)  
                while node.parent != None and node.parent.parent != None:  
                    node = node.parent
                    self.solve_stack.append(node)
                # since we found a solution
                return True

            # if the state is not the goal state
            problem.apply_operators(node, frontier)

        # if we don't found any soluction
        return False        
    
    def search_solution_uc(self, problem:Problem) -> bool:
        """ Search the sequence of actions that leads to the goal state and puts
        it on self.solve_stack variable 
        """

        # get the current state of the environment
        state = self.environment.get_state()  
        # create the root node with the current state
        root = Node(state, 'None', None)  
        frontier = [root]  # create the frontier stack and append the root to it

        while frontier:  # while frontier is not empty
            index = lowest_cost(frontier)
            node = frontier.pop(index)  # pop the cheaper node on the frontier
            
            # if this node is the goal state
            if node.content == problem.define_goal(state):
                print('Found')
                # append all the nodes parents while it's not the root node
                self.solve_stack.append(node)  
                while node.parent != None and node.parent.parent != None:  
                    node = node.parent
                    self.solve_stack.append(node)
                # since we found a solution
                return True

            # if the state is not the goal state
            problem.apply_operators(node, frontier)

        # if we don't found any soluction
        return False       

    def do_action(self, problem:Problem):
        """ Performs the agent action, it might be search for a solve sequence 
        or execute some state
        """
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
            self.search_solution_bfs(problem)
   
    def print_state(self, state:list):
        for i in range(3):
            print(f"{state[i*3]} {state[i*3 + 1]} {state[i*3 + 2]}")
        print()
