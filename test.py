import numpy as np


def _discount_accum_reward(rewards, gamma=0.99, initial_running_add=0.0):
    """ discounted the reward using gamma
    Args:
        rewards: list of reward,
        gamma: discount factor
        initial_running_add: the initial value to add
    Returns:
        list of discounted return
    """
    discounted_r = np.zeros_like(rewards, dtype=np.float32)
    running_add = initial_running_add
    for t in reversed(range(len(rewards))):
        running_add = rewards[t] + running_add * gamma
        discounted_r[t] = running_add
    return list(discounted_r)


def main():
    rewards = np.array([0.1, 0.1, 0.1, 1])
    print _discount_accum_reward(rewards, 0.9)
    
    return

if __name__ == '__main__':
    main()