import numpy as np
import random
from typing import List

from attributes import Anonymity, Ideology, Racism, States, Susceptability
from config import Config
from meme import Meme


class SimAgent:

    pass


class Agent(SimAgent):

    def __init__(self, id: int, state: States, meme: Meme, config: Config):
        # Agent properties
        self.id = id
        self.state = state
        self.config = config

        # The agent who last sent this Agent the meme, if applicable
        self.sent_by = None

        # Agent characteristics from 0-1 scales
        #
        # Political Ideology
        self.ideology = round(np.random.random(), 2)
        # Level of racism
        self.racism = round(np.random.random(), 2)
        # Susceptability to conspiracy theories & disinformation
        self.susceptability = round(np.random.random(), 2)
        # Level of anonymity this Agent has in the social network
        self.anonymity = round(np.random.uniform(self.config.anon_min, self.config.anon_max), 2)

        # Agent's message queue
        self.mq = []

        # Compute this agent's engagement probability and reaction score
        self.e, self.r = self.react(meme)

        self.aprint(f'{self.describe_anonymity()} anonymous ({self.anonymity})')
        self.aprint(f'{self.describe_ideology()} ideology ({self.ideology})')
        self.aprint(f'{self.describe_susceptability()} susceptible to disinformation ({self.susceptability})')
        self.aprint(f'{self.describe_racism_level()} racist ({self.racism})')

    def _map_to_attribute(self, cls, val):
        return min(cls, key=lambda x: abs(val - x.value)).name

    def describe_ideology(self):
        return self._map_to_attribute(Ideology, self.ideology)

    def describe_anonymity(self):
        return self._map_to_attribute(Anonymity, self.anonymity)

    def describe_racism_level(self):
        return self._map_to_attribute(Racism, self.racism)

    def describe_susceptability(self):
        return self._map_to_attribute(Susceptability, self.susceptability)

    def react(self, meme):
        """
        Computes this agent's sentiment towards a given Meme.

        Parameters
        ----------
        meme: Meme
            The meme this agent is reacting to.

        Returns
        -------
        tuple (float, float)
            The engagement level and reaction score, respectively, of this Agent to the meme.

            An engagement level of 0 indicates the Agent will not engage, where
            a level of 1 would mean the Agent is guaranteed to engage.

            A reaction score of 0 indicates strong agreement, and a reaction score indicates
            strong disagreement.
        """
        ideology_diff = abs(self.ideology - meme.ideology.value)
        racism_diff = abs(self.racism - meme.racism.value)

        # A very low score (0-0.25) indicates strong engagement due to agreement
        # A very high score (0.75-1) indicates strong engagement due to disagreement
        # A middling score indicates low engagement
        reaction_score = (ideology_diff + racism_diff) / 2  # Calculating engagement level

        # Calculate engagement as the distance to either 0 or 1, depending on which is closer
        engagement_score = abs(1 - reaction_score)

        # If a user is anonymous, they are more likely to engage
        anonymity_modifier = self.config.anon_modifier * 2.0 * abs(self.anonymity - 0.5)

        if self.anonymity >= 0.5:
            # Engagement bonus
            engagement_score += (engagement_score * anonymity_modifier)
        else:
            # Engagement penalty
            engagement_score -= (engagement_score * anonymity_modifier)

        # If the agent highly agrees/disagrees but is susceptible to disinformation,
        # they are more likely to engage
        if meme.truthfulness < 0.5:
            susceptability_modifier = self.config.susc_modifier * self.susceptability
            engagement_score += (engagement_score * susceptability_modifier)

        # Ensure the engagement score has not exceeded the bounds of 0, 1
        if engagement_score > 1:
            engagement_score = 1
        elif engagement_score < 0:
            engagement_score = 0

        return (round(engagement_score, 2), round(reaction_score, 2))

    def get_sort_available_neighbors(self, neighbors: List[SimAgent]) -> List[SimAgent]:
        most_similar = sorted(neighbors, key=lambda x: abs(self.r - x.r))
        return [agent for agent in most_similar if agent.state == States.SUSCEPTIBLE
                or agent.state == States.RECOVERED]

    def aprint(self, msg, *args):
        if self.config.verbose:
            print(f'[Agent {self.id}|{self.state.name}|e={self.e}|r={self.r}]', msg, *args)

    def decide_action(self, neighbors: List[SimAgent]):
        if self.state == States.INFECTED:
            if np.random.uniform(0, 1) >= self.e:
                self.aprint('Decided to do nothing.')
                self.state = States.RECOVERED
                return

            actions = [
                (0.3, self.reply),
                (0.3, self.consume),
                (0.4, self.send)
            ]

            action_prob = np.random.uniform(0, 1)
            cumulative_prob = 0

            for prob, action in actions:
                cumulative_prob += prob
                if action_prob <= cumulative_prob:
                    action(neighbors)
                    self.state = States.RECOVERED
        else:
            # SUSCEPTIBLE or RECOVERED: Do nothing until re-engaged
            self.aprint('Doing nothing.')

    def update_scores(self, e, r):
        self.e = e
        self.r = r
        # Normalize values
        if self.r < 0:
            self.r = 0
        if self.r > 0.9:
            self.r = 0.9
        if self.e < 0:
            self.e = 0
        if self.e > 0.9:
            self.e = 0.9

    # Actions as functions
    def send(self, neighbors: List[SimAgent]):
        self.aprint('Decided to send the meme')
        neighbors = self.get_sort_available_neighbors(neighbors)
        if len(neighbors) <= 1:
            return
        num_to_send = np.random.randint(1, len(neighbors))
        for i in range(num_to_send):
            self.aprint(f'Sending to Agent {neighbors[i].id}')
            neighbors[i].state = States.INFECTED
            neighbors[i].sent_by = self

    def consume(self, *args):
        self.aprint('Consuming the meme')
        # Reduce engagement level, adjust r score
        new_e = self.e - random.uniform(0, 0.5)
        new_r = self.r + random.uniform(-0.1, 0.1)
        self.update_scores(new_e, new_r)
        self.aprint('Adjusted e/r values')

    def reply(self, *args):
        # Emotional response?
        if not self.sent_by:
            # Initial infection, do nothing
            return
        self.aprint(f'Replying to Agent {self.sent_by.id}...')
        # If r scores are dissimilar (different views) and emotional responses are enabled,
        # sent_by's engagement probability should be reduced, and r score drifted towards the median.
        # If r scores are similar, reduce engagement but bolster r scores (confirmation of beliefs).
        new_e = self.sent_by.e - np.random.uniform(-0.1, 0.1)
        if self.config.emotional_responses and abs(self.sent_by.r - self.r) > 0.3:
            new_e -= (new_e * self.config.emotional_reply_modifier)
            if self.sent_by.r > 0.5:
                new_r = self.sent_by.r - (self.sent_by.r * self.config.emotional_reply_modifier)
            else:
                new_r = self.sent_by.r + (self.sent_by.r * self.config.emotional_reply_modifier)
            self.sent_by.update_scores(new_e, new_r)
        self.sent_by = None
