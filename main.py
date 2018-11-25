from agent import Agent

initial_state = [1,2,3,4,0,5,6,7,8]
agent = Agent(initial_state)
print(agent.print_state(initial_state))
print(agent.do_action())