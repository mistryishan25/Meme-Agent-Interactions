import numpy as np
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



    def emotional_response(self, meme):
        # Implement emotional response to memes
        pass

