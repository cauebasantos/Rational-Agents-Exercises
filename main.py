from agent import Agent

initial_state = [1,2,3,8,4,7,0,6,5]
agent = Agent(initial_state)
print('Estado atual:')
agent.print_state(initial_state)
agent.do_action()
print('Resolução:')
while agent.seq:
    agent.do_action()
print('End')