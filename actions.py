import random

receivers = []
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



