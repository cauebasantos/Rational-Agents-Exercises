from agent import Agent

initial_state = [1,2,3,8,4,0,7,6,5]
agent = Agent(initial_state)
print('Estado atual:')
agent.print_state(initial_state)
agent.do_action()
print('Resolução:')
while agent.solve_stack:
    agent.do_action()
print('End')
