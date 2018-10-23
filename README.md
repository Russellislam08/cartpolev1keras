OpenAI Gym CartPole-v1 Neural Network using Keras

CartPole-v1 can be found here: https://gym.openai.com/envs/CartPole-v1/
Inspired by Sentdex's reinforcement learning video series which can be found here: https://www.youtube.com/watch?v=3zeg7H6cAJw&ab_channel=sentdex

Changes that I made:
  1) Implemented the neural network using Keras, instead of TFLearn which Sentdex uses in his series. A few changes this leads to is the reshaping of the Numpy arrays and adding in a validation split when calling model.fit()
  2) Added a secondary training step. This step consists of a fraction of the trials played by the trained neural network and the rest is played using random values, similar to the first training step. In general, if using a bot to record game data, you should add randomness to the games. If not, then the bot will not try to find different ways to win. The whole point is to have it explore its capabilities
