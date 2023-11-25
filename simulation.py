from typing import List

import matplotlib.pyplot as plt

from agents import Agent, SimAgent
from attributes import States
from config import Config
from meme import Meme
from networks import NetworkBase


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


def simulate(desc: str, i_0: int, s_0: int, meme: Meme, network: NetworkBase, config: Config):

    agent_queue = [Agent(id, States.SUSCEPTIBLE, meme, config) for id in network.nodes()]

    infected = [i_0]
    susceptible = [s_0]
    recovered = [0]

    for i in range(i_0):
        agent_queue[i].state = States.INFECTED

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
    plt.plot(recovered, label='Recovered')
    plt.plot(susceptible, label='Susceptible')
    plt.title(f'SIR Model Simulation ({desc})')
    plt.xlabel('Time (days)')
    plt.ylabel('Population')
    plt.legend()
    plt.grid(True)
    plt.show()
