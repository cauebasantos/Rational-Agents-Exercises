from agent import Agent

initial_state = [1,2,3,4,0,5,6,7,8]
agent = Agent(initial_state)
print(agent.print_state(initial_state))
print(agent.print_state(agent.move_void_square_up(initial_state)))
print(agent.print_state(agent.move_void_square_down(initial_state)))
print(agent.print_state(agent.move_void_square_left(initial_state)))
print(agent.print_state(agent.move_void_square_right(initial_state)))