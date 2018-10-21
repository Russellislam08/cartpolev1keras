'''
  main.py
  Main file which will create the training data and train the model
'''
from training_data import initial_training_data
from training_data import further_training_data
from model import train_model
from model import test_model

def main():
  # Creates the initial training sample and trains the model
  # test_model will then make the model play games to determine how well it scores
  training_data = initial_training_data()
  model = train_model(training_data)
  test_model(model)
  
  # This can be put in a loop and run for x number of times
  # I only did it once just to show the general idea of it
  # Be careful that you don't overfit the model
  secondary_data = further_training_data(model)
  model = train_model(secondary_data)
  test_model(model)

if __name__ == '__main__':
  main()
