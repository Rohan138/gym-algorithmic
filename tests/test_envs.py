import gym

import gym_algorithmic


def test_envs():
    gym.make("Copy-v0")
    gym.make("DuplicatedInput-v0")
    gym.make("RepeatCopy-v0")
    gym.make("Reverse-v0")
    gym.make("ReversedAddition-v0")
    gym.make("ReversedAddition3-v0")
