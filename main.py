from agent import Agent
from problem import Problem

problem = Problem()
#initial_state = [1,2,3,8,4,0,7,6,5] # really easy problem (1 step)
#initial_state = [1,2,3,8,6,0,7,5,4] # easy problem (3 steps)
#initial_state = [1,2,3,8,4,7,0,6,5] # mid problem (12 steps)
#initial_state = [1,3,2,4,0,7,8,6,5] 
initial_state = [5,2,8,4,1,7,0,3,6] # hard problem (22 steps) with initial state
                                    # as [1,2,3,4,5,6,7,8,0]

agent = Agent(initial_state)
print('Estado atual:')
agent.print_state(initial_state)
agent.do_action(problem)
print('Resolução:')
while agent.solve_stack:
    agent.do_action(problem)
print('End')
