import numpy as np
import matplotlib.pyplot as plt

# Parameters
alpha, beta, gamma, dt = 3.5, 1.25, 1.1, 0.1
total_days = 900
time_step = 3
num_steps = int(total_days / time_step)

# Initial values
N = 100  # Total population
S = np.zeros(num_steps + 1)
I = np.zeros(num_steps + 1)
R = np.zeros(num_steps + 1)

S[0] = 90  # Initial susceptible individuals
I[0] = 10    # Initial infected individuals
R[0] = 0    # Initial recovered individuals

# Generate Wiener processes
np.random.seed(42)
dW1 = np.random.normal(0, np.sqrt(dt), num_steps)
W2 = np.random.normal(0, np.sqrt(dt), num_steps)
W3 = np.random.normal(0, np.sqrt(dt), num_steps)

# Euler-Maruyama method to solve SDEs

for i in range(num_steps):
    dS = -((alpha * S[i] * I[i]) / N) * dt - np.sqrt((alpha * S[i] * I[i]) / N) * dW1[i]
    dI = (((alpha * S[i] * I[i]) / N) + ((beta * I[i] * R[i]) / N) - gamma * I[i]) * dt \
        + np.sqrt((alpha * S[i] * I[i]) / N) * dW1[i] + np.sqrt((beta * I[i] * R[i]) / N) * W2[i] \
        - np.sqrt(gamma * I[i]) * W3[i]
    dR = (-1 * ((beta * I[i] * R[i]) / N) + gamma * I[i]) * dt - np.sqrt((beta * I[i] * R[i]) / N) * W2[i] \
        + np.sqrt(gamma * I[i]) * W3[i]

    S[i + 1] = max(0, S[i] + dS)
    I[i + 1] = max(0, I[i] + dI)
    print(f't={i}, I={I[i+1]}, dI={dI}, S={S[i+1]}, dS={dS}')
    R[i + 1] = max(0, R[i] + dR)

# Time vector
t = np.linspace(0, total_days, num_steps + 1)

print('Len: ', len(I))

# Plotting the results
plt.figure(figsize=(10, 6))
# plt.plot(t, I, label='Infected')
plt.plot(I, label='Infected')
# plt.plot(R, label='Recovered')
plt.plot(S, label='Susceptible')
plt.title('SIR Model Simulation')
plt.xlabel('Time (days)')
plt.ylabel('Population')
plt.legend()
plt.grid(True)
plt.show()
