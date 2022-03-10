import gym
import numpy as np
import matplotlib.pyplot as plt


NUMBER_GAMES = 1000
scores = []
round_scores = []

# Not-slippery (Deterministic):
# 0 - left
# 1 - down
# 2 - right
# 3 - up

# Map:
# 0 1 2 3
# 4 H 6 H
# 8 9 10 H
# H 13 14 T

env = gym.make('FrozenLake-v1')
policy = {0:1,4:1,8:2,9:1,13:2,14:2,1:2,2:1,6:1,10:1,3:0}

for i in range(NUMBER_GAMES):
    obs = env.reset()
    score = 0
    done = False
    while (not done):
        action = policy[obs]
        obs, reward, done, info = env.step(action)
        score += reward
    round_scores.append(score)
    if(i%10==0): scores.append(100*np.mean(round_scores[-10:]))

plt.title('Reasonable Policy')
plt.xlabel('nth 10 games')
plt.ylabel('win rate over the 10 games')
plt.plot(scores)

plt.show()
