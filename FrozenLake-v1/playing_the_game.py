import gym
import time

env = gym.make("FrozenLake-v1", is_slippery=True)
obs = env.reset()
env.render()

# The ice is slippery. So the controls change depending
# on probability. We can turn this off when making
# the environment. By default, it is stochastic (random).

# Not-slippery (Deterministic):

# 0 - left
# 1 - down
# 2 - right
# 3 - up

action_dict = {0: "left", 1: "down", 2:"right", 3:"up"}
# actions = [1,1,2,2,1,2]

policy = {0:1,4:1,8:2,9:1,13:2,14:2,1:2,2:1,6:1,10:1,3:0}

done = False
while(not done):
    time.sleep(1)
    # action = actions[i]
    action = policy[obs]
    print(action_dict[action])
    obs, reward, done, info = env.step(action)
    env.render()

print("Reward: ", reward)
    


