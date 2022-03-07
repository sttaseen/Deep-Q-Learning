# frozen-lake-ex2.py
import gym
import time

n_games = 10

env = gym.make("FrozenLake-v1")


for i in range(n_games):
    obs = env.reset()
    done = False
    while(not done):    
        time.sleep(0.5)    
        random_action = env.action_space.sample()
        new_state, reward, done, info = env.step(random_action)
        env.render()
        print("Reward: ", reward)
        print(format(info))
        
