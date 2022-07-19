# Deep-Q-Learning

This is an implementation of a [Stanford research paper](https://web.stanford.edu/class/psych209/Readings/MnihEtAlHassibis15NatureControlDeepRL.pdf) on reinforcement learning by combining deep learning and q-learning. 

Code for Move-37 is from a course on [udemy](https://www.udemy.com/course/deep-q-learning-from-paper-to-code/).

![image](https://user-images.githubusercontent.com/67076071/179663034-6dd84f8d-b61f-4b89-82e6-b17a76bd5d4c.png)

FrozenLakev1 uses q-learning for our agent to move from the starting position to the treasure/flag.

![image](https://user-images.githubusercontent.com/67076071/179661820-87eb1bed-bbb2-4b7f-ac3c-0e3a53680c93.png)

There are also some holes along the way which result in terminal states if the agent lands on them. Q-learning assigns a value to each square on the space based on the score gained if it chooses the best option available to it. For example, if the agent is left to the flag, the score would be 1 on the square to the left of the flag if the score gained from landing on the flag is 1.

These values are gained by randomly playing the game, choosing more random moves at first and then slowly reducing the number of random moves as the number of wins increases.

[Wikipedia](https://en.wikipedia.org/wiki/Q-learning) talks more in depth about the concepts used to gain the final q-values such as discount factor, learning rate and epsilon.
