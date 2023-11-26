import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


class Agent:
    def __init__(self, agent_id, state='S'):
        self.agent_id = agent_id
        self.state = state  # 'S' for susceptible, 'I' for infected, 'R' for recovered


def sir_model(y, t, beta, gamma):
    S, I, R = y
    dSdt = -beta * S * I / (S + I + R)
    dIdt = beta * S * I / (S + I + R) - gamma * I
    dRdt = gamma * I
    return [dSdt, dIdt, dRdt]


def initialize_agents(num_agents, initial_infected):
    agents = [Agent(agent_id=i, state='S') for i in range(num_agents)]
    # Randomly set some agents as initially infected
    infected_agents = np.random.choice(
        agents, size=initial_infected, replace=False)
    for agent in infected_agents:
        agent.state = 'I'
    return agents


def count_states(agents):
    # Count the number of agents in each state
    count_S = sum(1 for agent in agents if agent.state == 'S')
    count_I = sum(1 for agent in agents if agent.state == 'I')
    count_R = sum(1 for agent in agents if agent.state == 'R')
    return count_S, count_I, count_R


def run_sir_simulation(agents, beta, gamma, days):
    t = np.linspace(0, days, days)
    initial_counts = count_states(agents)
    y0 = [initial_counts[0], initial_counts[1], initial_counts[2]]
    solution = odeint(sir_model, y0, t, args=(beta, gamma))

    for day in range(days):
        # Update agent states based on the SIR model
        for agent in agents:
            if agent.state == 'I':
                agent.state = 'R'

    # Plot the SIR model results
    plt.plot(t, solution[:, 0], label='Susceptible')
    plt.plot(t, solution[:, 1], label='Infected')
    plt.plot(t, solution[:, 2], label='Recovered')
    plt.xlabel('Days')
    plt.ylabel('Population')
    plt.title('SIR Model Simulation')
    plt.legend()
    plt.show()


# Simulation setup
num_agents = 100
initial_infected = 1
beta = 0.3
gamma = 0.1
days = 160

agents = initialize_agents(num_agents, initial_infected)
run_sir_simulation(agents, beta, gamma, days)
