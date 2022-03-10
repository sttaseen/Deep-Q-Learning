# Author: Sadat Taseen, 2022

import gym
import numpy as np
import matplotlib.pyplot as plt
# import time

env = gym.make("FrozenLake-v1")

NUMBER_GAMES = 1000
scores = []

# obs - current state (int)
# reward - +1 if treasure reached (float)
# done - episode ended (boolean)
# info - probability of the move happening (dict)

round_scores = []

for i in range(NUMBER_GAMES):    
    done = False
    obs = env.reset()
    score = 0
    while(not done):
        # env.render()
        random_action = env.action_space.sample()
        obs, reward, done, info = env.step(random_action)
        # time.sleep(0.5)
        score += reward
    round_scores.append(score)
    if (i%10==0): scores.append(100*np.mean(round_scores[-10:]))

plt.xlabel("nth 10 games")
plt.ylabel("win rate over the 10 games")
plt.title("Random Policy")
plt.plot(scores)
plt.show()
