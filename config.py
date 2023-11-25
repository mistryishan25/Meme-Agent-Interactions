# Anonymity and susceptability modifiers.
# These are percentages which increase or decrease
# the baseline likelihood of engagement by that amount.
ANON_MODIFIER = 0.15
SUSC_MODIFIER = 0.05

# Range of anonymity level for all agents.
# For example, a mostly anonymous social network (e.g., Reddit)
# might have a MIN/MAX of 0.5-1.0.
ANON_MIN = 0.0
ANON_MAX = 1.0

# Modifier for emotional replies
ER_MODIFIER = 0.15

VERBOSE = False
EMOTIONAL_RESPONSES = True


class Config:

    def __init__(
            self,
            anon_modifier=ANON_MODIFIER,
            susc_modifier=SUSC_MODIFIER,
            anon_min=ANON_MIN,
            anon_max=ANON_MAX,
            emotional_reply_modifier=ER_MODIFIER,
            verbose=VERBOSE,
            emotional_responses=EMOTIONAL_RESPONSES,
    ):
        self.anon_modifier = anon_modifier
        self.susc_modifier = susc_modifier
        self.anon_min = anon_min
        self.anon_max = anon_max
        self.emotional_reply_modifier = emotional_reply_modifier
        self.verbose = verbose
        self.emotional_responses = emotional_responses
