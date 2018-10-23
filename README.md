# OpenAI Gym CartPole-v1 Neural Network using Keras

### CartPole-v1 can be found here: https://gym.openai.com/envs/CartPole-v1/

### Inspired by Sentdex's reinforcement learning video series which can be found here: https://www.youtube.com/watch?v=3zeg7H6cAJw&ab_channel=sentdex

#### What is OpenAI Gym?
  OpenAI Gym is a toolkit with various environments which can be used as a playground to develop neural networks.
  
  One of the environments is a game in which you have a pole on a cart and you must make it balance. If it tilts too far from the veritcal axis or the cart moves too far to the left/right, you lose. The whole point is to train a neural network to be able to play the game.
  
  The game CartPole-v1 is considered solve when the average score attained by the bot is >= 195.0 over 100 consecutive trials, which this model does.
 
#### What did I make?
  I followed a tutorial on YouTube created by Sentdex to develop a neural network using Python to learn how to play the game. There are certain differences between what he did and what I did, which I explain further below. 
  
  The model is implemented using Tensorflow along with Keras and has 11 layers in total. Training data is obtained initially by running numerous trials of the game with random values as the input. The model uses reinforcement learning on the data to teach itself how to play the game to achieve a score which is acceptable.
  
  The model is not computationally expensive. I run this using Tensorflow-GPU on a nVidia Geforce 940MX 2GB RAM on Ubuntu 18.04 and the whole process takes about 5 minutes to complete.

#### Differences in the version I created:

- Implemented the neural network using Keras, instead of TFLearn which Sentdex uses in his series. A few changes this leads to is the reshaping of the Numpy arrays and adding in a validation split when training the model

- Added a secondary training step. This step consists of a fraction of the trials played by the trained neural network and the rest is played using random values, similar to the first training step.
  - The idea of this is that since the initial games played are completely random, the outcome of the model will be random as well. I decided to make the model play again and then learn from itself in order to improve its score. I've run the model numerous times and the general trend is that it scores better once trained again. 
  - Theoretically, this step can be done x number of times. I did it once just to show the idea of it.
  - Also, in general, if using a bot to record game data, you should add randomness to the games. If not, then the bot will not try to find different ways to win. The whole point is to have it explore its capabilities
