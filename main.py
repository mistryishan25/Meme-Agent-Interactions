from attributes import Ideology, Racism
from config import Config
from lonnberg import Lonnberg
from meme import Meme
from networks import CommunityClusters, PolarizedCrowd, RandomNetwork
from simulation import simulate


def main():
    """Run several simulation scenarios."""
    # Reusable simulation parameters
    default_config = Config()
    verbose_config = Config(verbose=True)
    high_anon_config = Config(anon_min=0.8, anon_max=1.0)
    low_anon_config = Config(anon_min=0.0, anon_max=0.2)
    echo_chamber_config = Config(
        anon_min=0.8,
        anon_max=1.0,
        susc_modifier=0.10,
        susceptibility_min=0.75,
        susceptibility_max=1.0,
        racial_bias_min=0.0,
        racial_bias_max=0.25,
        ideology_min=0.75,
        ideology_max=1.0,
    )
    echo_chamber_config_2 = Config(
        anon_min=0.8,
        anon_max=1.0,
        susc_modifier=0.10,
        susceptibility_min=0.75,
        susceptibility_max=1.0,
        racial_bias_min=0.75,
        racial_bias_max=1.0,
        ideology_min=0.0,
        ideology_max=0.25,
    )
    rand_net = RandomNetwork()
    cc_net = CommunityClusters()
    polarized_net = PolarizedCrowd()
    controversial_meme = Meme('A racist meme', Ideology.ALT_RIGHT, 0.2, Racism.HARD)
    controversial_meme_2 = Meme('A highly political meme', Ideology.LEFTIST, 0.4, Racism.ANTI)
    uncontroversial_meme = Meme('A funny meme', Ideology.MODERATE, 1.0, Racism.NEUTRAL)

    # RandomNetwork | Controversial Meme
    desc = 'RandomNetwork | Controversial Meme'
    i_0 = 10
    s_0 = 80
    simulate(desc, i_0, s_0, controversial_meme, rand_net, verbose_config)

    # RandomNetwork | Uncontroversial Meme
    desc = 'RandomNetwork | Uncontroversial Meme'
    simulate(desc, i_0, s_0, uncontroversial_meme, rand_net, default_config)

    # RandomNetwork | Controversial Meme | High Anonymity
    desc = 'RandomNetwork | Controversial Meme | High Anonymity'
    simulate(desc, i_0, s_0, controversial_meme, rand_net, high_anon_config)

    # RandomNetwork | Controversial Meme | Low Anonymity
    desc = 'RandomNetwork | Controversial Meme | Low Anonymity'
    simulate(desc, i_0, s_0, controversial_meme, rand_net, low_anon_config)

    # CommunityClusters | Controversial Meme
    desc = 'CommunityClusters | Controversial Meme'
    i_0 = 20
    s_0 = 80
    simulate(desc, i_0, s_0, controversial_meme, cc_net, default_config)

    # PolarizedCrowd | Controversial Meme | Low Anonymity
    desc = 'PolarizedCrowd | Controversial Meme'
    i_0 = 30
    s_0 = 70
    simulate(desc, i_0, s_0, controversial_meme, polarized_net, default_config)

    # RandomNetwork | Echo Chamber
    desc = 'RandomNetwork | Echo Chamber'
    i_0 = 10
    s_0 = 80
    simulate(desc, i_0, s_0, controversial_meme_2, rand_net, echo_chamber_config)

    # RandomNetwork | Hornet's Nest
    desc = "RandomNetwork | Hornet's Nest"
    i_0 = 30
    s_0 = 70
    simulate(desc, i_0, s_0, controversial_meme_2, rand_net, echo_chamber_config_2)

    # PolarizedCrowd | Opposing Factions
    desc = 'PolarizedCrowd | Opposing Factions'
    i_0 = 30
    s_0 = 70
    simulate(desc, i_0, s_0, controversial_meme, polarized_net, echo_chamber_config, secondary=echo_chamber_config_2)

    # Lonnberg SIR model (baseline)
    num_days = 900
    time_step = 3
    num_steps = int(num_days / time_step)
    sim = Lonnberg(num_steps)
    for t in range(num_steps):
        sim.step(t)
    sim.draw()


if __name__ == '__main__':
    main()
