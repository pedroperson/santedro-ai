from typing import List
import tensorflow as tf
import numpy as np
import gym

# TODO: match these types to whatever environemtns and tensorflow use
Observation = np.ndarray
Observations = List[Observation]
Action = tf.Tensor
Actions = tf.Tensor
Logits = tf.Tensor
Reward = float
Rewards = List[float]
LogPs = List[float]
Loss = List[float]
#  TODO: find a better name for critic_v and rename it everywhere
CriticV = float
Environment = gym.Env


def observation_to_observations(observation: Observation) -> Observations:
    return observation.reshape(1, -1).astype(np.float32)


def actions_as_action(actions: Actions) -> Action:
    return actions.numpy()[0]


print("HELLO")
