from agent import Agent
from problem import Problem

problem = Problem()
#initial_state = [1,2,3,8,6,0,7,5,4]
initial_state = [1,2,3,8,4,7,0,6,5]

agent = Agent(initial_state)
print('Estado atual:')
agent.print_state(initial_state)
agent.do_action(problem)
print('Resolução:')
while agent.solve_stack:
    agent.do_action(problem)
print('End')
