import gym
import time

env = gym.make("FrozenLake-v1", is_slippery=False)
env.reset()
env.render()

# The ice is slippery. So the controls change
# on probability. We can turn this off when making
# the environment

#Not-slipper:
# 3 - up
# 1 - down
# 0 - left
# 2 - right

actions = [1,1,2,2,1,2]

for i in range(len(actions)):
    time.sleep(1)
    action = actions[i]
    print(action)
    new_state, reward, done, info = env.step(action)
    env.render()

print(reward)
    


