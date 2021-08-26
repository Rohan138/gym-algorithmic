from gym.envs.registration import register

from gym_algorithmic.copy_ import CopyEnv
from gym_algorithmic.duplicated_input import DuplicatedInputEnv
from gym_algorithmic.repeat_copy import RepeatCopyEnv
from gym_algorithmic.reverse import ReverseEnv
from gym_algorithmic.reversed_addition import ReversedAdditionEnv

register(
    id="Copy-v0",
    entry_point="gym_algorithmic:CopyEnv",
    max_episode_steps=200,
    reward_threshold=25.0,
)

register(
    id="RepeatCopy-v0",
    entry_point="gym_algorithmic:RepeatCopyEnv",
    max_episode_steps=200,
    reward_threshold=75.0,
)

register(
    id="ReversedAddition-v0",
    entry_point="gym_algorithmic:ReversedAdditionEnv",
    kwargs={"rows": 2},
    max_episode_steps=200,
    reward_threshold=25.0,
)

register(
    id="ReversedAddition3-v0",
    entry_point="gym_algorithmic:ReversedAdditionEnv",
    kwargs={"rows": 3},
    max_episode_steps=200,
    reward_threshold=25.0,
)

register(
    id="DuplicatedInput-v0",
    entry_point="gym_algorithmic:DuplicatedInputEnv",
    max_episode_steps=200,
    reward_threshold=9.0,
)

register(
    id="Reverse-v0",
    entry_point="gym_algorithmic:ReverseEnv",
    max_episode_steps=200,
    reward_threshold=25.0,
)
