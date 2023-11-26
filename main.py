import random
import networkx as nx
import wandb
from agents import Agent
from lonnberg import Lonnberg
from meme import Meme
from networks import CommunityClusters, PolarizedCrowd, RandomNetwork
import wandb




def main():
    # # Define a set of parameter values to explore
    # parameter_values = {
    #     'strategy': ['random', 'influence_based', 'degree_based'],
    #     'other_parameter': [value1, value2, value3],
    #     # Add more parameters as needed
    # }

    # # Initialize Weights & Biases
    # wandb.init(project='your_project_name', config=parameter_values)

    # # Run simulations for different parameter combinations
    # for config in wandb.config:
    #     run_simulation(config)

    # Run an initial experiment with a Polarized Crowd Network
    num_days = 900
    time_step = 3
    num_steps = int(num_days / time_step)

    network = PolarizedCrowd()
    sim = Lonnberg(num_steps)

    agent_queue = [Agent(id) for id in network.nodes()]

    initial_meme = Meme('Some content')

    for t in range(num_steps):
        expected_e = sim.step(t)  # Modeled engagement at the current time step
        current_e = 0             # Measured engagement

        while current_e < expected_e:
            agent = agent_queue.pop(0)
            if agent.decide_action(initial_meme, network):
                print(f'Agent {agent.agent_id} engaged with the meme')
                current_e += 1
            else:
                print(f'Agent {agent.agent_id} did not engage with the meme')
            agent_queue.append(agent)

        print(f'TIME STEP {t}')

    sim.draw()


if __name__ == '__main__':
    main()
