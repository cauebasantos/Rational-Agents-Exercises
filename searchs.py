from node import Node
from node import lowest_cost
from problem import Problem

def search_solution_bfs(state:list, problem:Problem) -> list:
    "" """ Search the sequence of actions that leads to the goal state and puts
    it on self.solve_stack variable 
    """

    # create the root node with the current state
    root = Node(state, 'None', None)  
    frontier = [root]  # create the frontier queue and append the root to it
    # holds the stack sequence of actions the agent is going to do to 
    # achieve his goal
    solve_stack = []

    while frontier:  # while frontier is not empty
        node = frontier.pop(0)  # pop the first node on the frontier
        
        # if this node is the goal state
        if node.content == problem.define_goal(state):
            # append all the nodes parents while it's not the root node
            solve_stack.append(node)  
            while node.parent != None and node.parent.parent != None:  
                node = node.parent
                solve_stack.append(node)
            # since we found a solution
            return solve_stack

        # if the state is not the goal state
        problem.apply_operators(node, frontier)

    # if we don't found any soluction
    return []

def search_solution_dfs(state:list, problem:Problem, threshold=1000, interactive
=False) -> list:
    """ Search the sequence of actions that leads to the goal state and puts
    it on self.solve_stack variable 
    """
    # keep up a history of most recent states viseted
    history = [] 
    # create the root node with the current state
    root = Node(state, 'None', None)  
    frontier = [root]  # create the frontier stack and append the root to it
    # holds the stack sequence of actions the agent is going to do to 
    # achieve his goal
    solve_stack = []

    while frontier:  # while frontier is not empty            
        node = frontier.pop(-1)  # pop the last node on the frontier
        
        # if this node is the goal state
        if node.content == problem.define_goal(state):
            # append all the nodes parents while it's not the root node
            solve_stack.append(node)  
            while node.parent != None and node.parent.parent != None:  
                node = node.parent
                solve_stack.append(node)
            # since we found a solution
            return solve_stack
        
        # if we've crossed the threshold on this node but there is other nodes
        elif node.depth > threshold and frontier:
            continue

        # if we've crossed the threshold
        elif node.depth > threshold and len(frontier) == 0 and interactive == False:
            print(f'No answer was found on a node of depth less than \
            {threshold}')
            return []
        elif node.depth > threshold and len(frontier) == 0 and interactive == True:
            frontier = [root] 
            threshold += 10
            history = []
            print(f'No answer was found on a node of depth less than \
            {threshold}, We are gonna keep looking')


        # if the state is not the goal state
        if node.content not in history:
            problem.apply_operators(node, frontier)
            history.append(node.content)
            if len(history) > 100:
                history.pop(0)

    # if we don't found any soluction
    return []        

def search_solution_uc(state:list, problem:Problem) -> list:
    """ Search the sequence of actions that leads to the goal state and puts
    it on self.solve_stack variable 
    """

    # create the root node with the current state
    root = Node(state, 'None', None)  
    frontier = [root]  # create the frontier stack and append the root to it
    #
    solve_stack = []

    while frontier:  # while frontier is not empty
        index = lowest_cost(frontier)
        node = frontier.pop(index)  # pop the cheaper node on the frontier
        
        # if this node is the goal state
        if node.content == problem.define_goal(state):
            print('Found')
            # append all the nodes parents while it's not the root node
            solve_stack.append(node)  
            while node.parent != None and node.parent.parent != None:  
                node = node.parent
                solve_stack.append(node)
            # since we found a solution
            return solve_stack

        # if the state is not the goal state
        problem.apply_operators(node, frontier)

    # if we don't found any soluction
    return []       
