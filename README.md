# gym-algorithmic
This repository contains the algorithmic environments previously present in [OpenAI Gym](https://github.com/openai/gym) prior to Gym version 0.20.0.  
These environments were introduced in the paper [Learning Simple Algorithms from Examples](https://arxiv.org/abs/1511.07275)

## Documentation

[Algorithmic Environments](https://github.com/Rohan138/gym-algorithmic/blob/main/docs/algorithmic.md)  

[Copy-v0](https://github.com/Rohan138/gym-algorithmic/blob/main/docs/copy.md)  
[DuplicatedInput-v0](https://github.com/Rohan138/gym-algorithmic/blob/main/docs/duplicated_input.md)  
[RepeatCopy-v0](https://github.com/Rohan138/gym-algorithmic/blob/main/docs/repeat_copy.md)  
[Reverse-v0](https://github.com/Rohan138/gym-algorithmic/blob/main/docs/reverse.md)  
[ReversedAddition-v0](https://github.com/Rohan138/gym-algorithmic/blob/main/docs/reversed_addition.md)  
[ReversedAddition3-v0](https://github.com/Rohan138/gym-algorithmic/blob/main/docs/reversed_addition.md)  

Documentation credit: https://github.com/openai/gym/pull/2334

## Usage
```
$ pip install gym-algorithmic

import gym
import gym_algorithmic

gym.make("Copy-v0")
```

## Citation

```
@inproceedings{Zaremba2016LearningSA,
  title={Learning Simple Algorithms from Examples},
  author={Wojciech Zaremba and Tomas Mikolov and Armand Joulin and R. Fergus},
  booktitle={ICML},
  year={2016}
}
```
