from agents import Agent, SimAgent
from typing import List
from lonnberg import Lonnberg
from meme import Meme
from networks import CommunityClusters, PolarizedCrowd, RandomNetwork
from attributes import States, Ideology, Racism
from config import Config
import networkx as nx
import matplotlib.pyplot as plt


def num_infected(agents: List[SimAgent]):
    i = 0
    for agent in agents:
        if agent.state == States.INFECTED:
            i += 1
    return i


def num_susceptible(agents: List[SimAgent]):
    i = 0
    for agent in agents:
        if agent.state == States.SUSCEPTIBLE:
            i += 1
    return i


def num_recovered(agents: List[SimAgent]):
    i = 0
    for agent in agents:
        if agent.state == States.RECOVERED:
            i += 1
    return i


def get_agent(agents, id):
    for agent in agents:
        if agent.id == id:
            return agent
    raise ValueError(f'Agent with id {id} not found!')


def main():

    # num_days = 900
    # time_step = 3
    # num_steps = int(num_days / time_step)
    # sim = Lonnberg(num_steps)

    network = RandomNetwork()
    initial_meme = Meme('A racist meme', Ideology.ALT_RIGHT, 0.2, Racism.HARD)

    agent_queue = [Agent(id, States.SUSCEPTIBLE, initial_meme, Config(verbose=True)) for id in network.nodes()]

    infected = [10]
    susceptible = [90]
    recovered = [0]

    for i in range(10):
        agent_queue[i].state = States.INFECTED

    print('\n********\n')

    while num_infected(agent_queue) > 0:
        current_agent = agent_queue.pop(0)
        neighbors = network.neighbors(current_agent.id)
        current_agent.decide_action([get_agent(agent_queue, id) for id in neighbors])
        agent_queue.append(current_agent)
        infected.append(num_infected(agent_queue))
        susceptible.append(num_susceptible(agent_queue))
        recovered.append(num_recovered(agent_queue))

    # Plot the results
    plt.figure(figsize=(10, 6))
    plt.plot(infected, label='Interest')
    plt.plot(susceptible, label='Susceptible')
    plt.plot(recovered, label='Recovered')
    plt.title('SIR Model Simulation')
    plt.xlabel('Time (days)')
    plt.ylabel('Population')
    plt.legend()
    plt.grid(True)
    plt.show()

    #  for t in range(num_steps):
    #      expected_e = sim.step(t)  # Modeled engagement at the current time step
    #      current_e = 0             # Measured engagement

    #      while current_e < expected_e:
    #          agent = agent_queue.pop(0)
    #          if agent.decide_action(initial_meme, network):
    #              print(f'Agent {agent.agent_id} engaged with the meme')
    #              current_e += 1
    #          else:
    #              print(f'Agent {agent.agent_id} did not engage with the meme')
    #          agent_queue.append(agent)

    #      print(f'TIME STEP {t}')

    #  sim.draw()


if __name__ == '__main__':
    main()
