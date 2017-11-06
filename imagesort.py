import argparse, os

def readCommand( argv ):
    USAGE_STRING = """
  USAGE:      python3 imagesort.py <options>
  EXAMPLES:   (1) python imagesort.py
                  - trains the default mostFrequent classifier on the digit dataset
                  using the default 100 training examples and
                  then test the classifier on test data
              (2) python dataClassifier.py -c perceptron -t 1000 -s 500
                  - would run the perceptron classifier on 1000 training examples, would
                  test the classifier on 500 test data points
                 """
    parser = argparse.ArgumentParser()