import matplotlib.pyplot as plt
import numpy as np


class Lonnberg:
    """A SIR model based off the work of Lonnberg et al."""

    def __init__(self, num_steps, alpha=3.5, beta=1.25, gamma=1.1, dt=0.1, N=100, S_0=90, I_0=10, R_0=0):
        """Initialize model parameters with defaults as reported in Figure 1 of the Lonnberg paper."""
        # Parameters
        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma
        self.dt = dt
        self.N = N

        # Initial values
        self.N = N  # Total population
        self.S = np.zeros(num_steps + 1)
        self.I = np.zeros(num_steps + 1)
        self.R = np.zeros(num_steps + 1)

        self.S[0] = S_0  # Initial susceptible individuals
        self.I[0] = I_0  # Initial infected individuals
        self.R[0] = R_0  # Initial recovered individuals

        # Generate Wiener processes
        np.random.seed(42)
        self.dW1 = np.random.normal(0, np.sqrt(self.dt), num_steps)
        self.W2 = np.random.normal(0, np.sqrt(self.dt), num_steps)
        self.W3 = np.random.normal(0, np.sqrt(self.dt), num_steps)

    def dS(self, t):
        # Compute change in susceptible agents
        return (-((self.alpha * self.S[t] * self.I[t]) / self.N) * self.dt
                - np.sqrt((self.alpha * self.S[t] * self.I[t]) / self.N) * self.dW1[t])

    def dI(self, t):
        # Compute change in infected agents
        return ((((self.alpha * self.S[t] * self.I[t]) / self.N)
                + ((self.beta * self.I[t] * self.R[t]) / self.N) - self.gamma * self.I[t]) * self.dt
                + np.sqrt((self.alpha * self.S[t] * self.I[t]) / self.N)
                * self.dW1[t] + np.sqrt((self.beta * self.I[t] * self.R[t]) / self.N) * self.W2[t]
                - np.sqrt(self.gamma * self.I[t]) * self.W3[t])

    def dR(self, t):
        # Compute change in recovered agents
        return ((-1 * ((self.beta * self.I[t] * self.R[t]) / self.N) + self.gamma * self.I[t]) * self.dt
                - np.sqrt((self.beta * self.I[t] * self.R[t]) / self.N) * self.W2[t]
                + np.sqrt(self.gamma * self.I[t]) * self.W3[t])

    def step(self, t):
        # Compute the SDEs for the current time step,
        # and return the current engagement level rounded to the nearest integer.
        dS = self.dS(t)
        dI = self.dI(t)
        dR = self.dR(t)
        self.S[t + 1] = max(0, self.S[t] + dS)
        self.I[t + 1] = max(0, self.I[t] + dI)
        self.R[t + 1] = max(0, self.R[t] + dR)
        return (round(self.S[t + 1]), round(self.I[t + 1]), round(self.I[t + 1]))

    def draw(self):
        # Plot the results
        plt.figure(figsize=(10, 6))
        # plt.plot(t, I, label='Infected')
        plt.plot(self.I, label='Interest')
        plt.plot(self.R, label='Recovered')
        plt.plot(self.S, label='Susceptible')
        plt.title('Lonnberg Model')
        plt.xlabel('Time (days/3)')
        plt.ylabel('Population')
        plt.legend()
        plt.grid(True)
        plt.show()
