import random

class Agent:
    def __init__(self, agent_id):
        self.agent_id = agent_id
        self.age = random.randint(18, 65)  # Random age between 18 and 65
        self.political_affiliation = random.choice(['liberal', 'conservative', 'moderate'])
        self.social_network_size = random.randint(50, 300)  # Random social network size
        # try various informed tactics - link age and the susceptibility
        self.susceptibility_to_memes = random.uniform(0.0, 1.0)  # Random susceptibility value between 0 and 1
        self.beliefs = {'climate_change': random.choice(['strongly_agree', 'neutral', 'strongly_disagree']),
                        'healthcare': random.choice(['support', 'oppose']),
                        'economy': random.choice(['positive', 'negative'])}

    def share_meme(self, meme):
        # Implement meme sharing behavior
        pass

    def make_decision(self, meme):
        # Implement decision-making process
        pass

    def emotional_response(self, meme):
        # Implement emotional response to memes
        pass

# Create a list of agents
num_agents = 100  # Adjust the number of agents as needed
agents = [Agent(agent_id) for agent_id in range(num_agents)]

# Access agent attributes
for agent in agents:
    print(f"Agent {agent.agent_id}: Age {agent.age}, Political Affiliation {agent.political_affiliation}, " +
          f"Social Network Size {agent.social_network_size}, Susceptibility to Memes {agent.susceptibility_to_memes}, " +
          f"Beliefs {agent.beliefs}")
    break