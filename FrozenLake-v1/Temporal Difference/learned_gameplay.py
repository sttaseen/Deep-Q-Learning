from saved_Q_values import Q
import gym
import time
import numpy as np

N_ACTIONS = 4
N_STATES = 16

if __name__ == '__main__':

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
    # policy = {0:1,4:1,8:2,9:1,13:2,14:2,1:2,2:1,6:1,10:1,3:0}
    learned_policy = {}

    # Extracting the better policy from the Q values

    for state in range(N_STATES):
        actions = np.array([Q[(state, a)] \
                                        for a in range(N_ACTIONS)])
        action = np.argmax(actions)
        learned_policy[state] = action

    print(learned_policy)


    done = False

    while(not done):
        time.sleep(1)
        # action = actions[i]
        action = learned_policy[obs]
        print(action_dict[action])
        obs, reward, done, info = env.step(action)
        env.render()

    print("Reward: ", reward)
    


