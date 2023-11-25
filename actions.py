import random

class Agent:
    def __init__(self, agent_id):
        self.agent_id = agent_id
        self.characteristics = {'influence': random.uniform(0, 1)}

    def decide_action(self, meme, neighbors):
        actions = [
            (0.3, self.send_meme),
            (0.4, self.consume_meme),
            (0.3, self.forward_meme)
        ]

        action_prob = random.uniform(0, 1)
        cumulative_prob = 0

        for prob, action in actions:
            cumulative_prob += prob
            if action_prob <= cumulative_prob:
                return action(meme, neighbors)

    def send_meme(self, meme, neighbors):
        receiver = random.choice(neighbors)
        send_meme(self, receiver, meme)

    def consume_meme(self, meme, neighbors):
        consume_meme(self, meme)

    def forward_meme(self, meme, neighbors):
        receiver = random.choice(neighbors)
        forward_meme(self, receiver, meme)

# Actions as functions
def send_meme(sender, receiver, meme):
    sender.consume_meme(meme)
    receiver.receive_meme(meme)

def consume_meme(agent, meme):
    agent.characteristics['influence'] += random.uniform(-0.1, 0.1)

def forward_meme(self, meme, neighbors):
    strategy = 'random'  # You can change this as needed
    if strategy == 'random':
        receivers = random.sample(neighbors, min(3, len(neighbors)))
    elif strategy == 'influence_based':
        # Implement an influence-based forwarding strategy
        pass
    elif strategy == 'degree_based':
        # Implement a degree-based forwarding strategy
        pass

    for receiver in receivers:
        forward_meme(self, receiver, meme)

