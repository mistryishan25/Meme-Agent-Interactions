import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

from agents import Agent


class InformationCascadeModel:
    def __init__(self, agents):
        self.agents = agents

    def reset_model(self):
        for agent in self.agents:
            agent.is_active = False

    def run_model(self, source_agent):
        source_agent.activate()  # Seed the information cascade
        active_agents = [source_agent]

        while active_agents:
            current_agent = active_agents.pop(0)

            # Activate neighbors with a certain probability
            for neighbor in self.get_neighbors(current_agent):
                current_agent.try_activate_neighbor(neighbor)
                if neighbor.is_active:
                    active_agents.append(neighbor)

    def get_neighbors(self, agent):
        # You can customize this based on your network structure
        return [neighbor for neighbor in self.agents if neighbor != agent]


class SIRModel:
    def __init__(self, num_agents, initial_infected, beta, gamma, days):
        self.num_agents = num_agents
        self.initial_infected = initial_infected
        self.beta = beta
        self.gamma = gamma
        self.days = days
        self.agents = self.initialize_agents()

    def initialize_agents(self):
        agents = [Agent(agent_id=i, state='S') for i in range(self.num_agents)]
        # Randomly set some agents as initially infected
        infected_agents = np.random.choice(
            agents, size=self.initial_infected, replace=False)
        for agent in infected_agents:
            agent.state = 'I'
        return agents

    def count_states(self):
        # Count the number of agents in each state
        count_S = sum(1 for agent in self.agents if agent.state == 'S')
        count_I = sum(1 for agent in self.agents if agent.state == 'I')
        count_R = sum(1 for agent in self.agents if agent.state == 'R')
        return count_S, count_I, count_R

    def sir_model(self, y, t):
        S, I, R = y
        dSdt = -self.beta * S * I / (S + I + R)
        dIdt = self.beta * S * I / (S + I + R) - self.gamma * I
        dRdt = self.gamma * I
        return [dSdt, dIdt, dRdt]


class ForestFireModel:
    def __init__(self, size, seed_probability, ignition_probability, growth_probability):
        self.size = size
        self.seed_probability = seed_probability
        self.ignition_probability = ignition_probability
        self.growth_probability = growth_probability
        self.grid = self.initialize_grid()

    def initialize_grid(self):
        grid = np.random.choice(['empty', 'tree'], size=(self.size, self.size), p=[
                                1 - self.seed_probability, self.seed_probability])
        return grid

    def plot_grid(self):
        cmap = ListedColormap(['white', 'green', 'red'])
        plt.imshow([[cell == 'tree' for cell in row]
                   for row in self.grid], cmap=cmap)
        plt.title('Forest Fire Model')
        plt.show()

    def is_valid_position(self, i, j):
        return 0 <= i < self.size and 0 <= j < self.size

    def neighbors_burning(self, i, j):
        return any(self.grid[ni, nj] == 'burning' for ni, nj in self.get_neighbors(i, j))

    def get_neighbors(self, i, j):
        neighbors = []
        for ni in range(i - 1, i + 2):
            for nj in range(j - 1, j + 2):
                if (ni != i or nj != j) and self.is_valid_position(ni, nj):
                    neighbors.append((ni, nj))
        return neighbors

    def step(self):
        new_grid = np.copy(self.grid)
        for i in range(self.size):
            for j in range(self.size):
                cell = self.grid[i, j]
                if cell == 'burning':
                    new_grid[i, j] = 'empty'
                elif cell == 'tree' and (self.neighbors_burning(i, j)
                                         or np.random.rand() < self.growth_probability):
                    new_grid[i, j] = 'burning'
                elif cell == 'empty' and np.random.rand() < self.seed_probability:
                    new_grid[i, j] = 'tree'
        self.grid = new_grid

    def run_simulation(self, steps):
        for _ in range(steps):
            self.step()
            self.plot_grid()
