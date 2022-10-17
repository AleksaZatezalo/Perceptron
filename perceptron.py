import numpy as np;
class Perceptron:
    """Perceptron classifier.

    Parameters:
    eta: float
        Learning Rate (between 0.0 and 1)
    n_iter: int
        Passes over the training set.
    random_state: int
        random number generator seed for the initial weights.
    
    Attributes:
        w_: 1d-array
        b_: Scalar
            Bias unit after fitting.
        
        errors_: list
            number of missclassifications (updates) in each epoch.
    """

    def __init__(self, eta=0.01, n_iter=50, random_stare=1):
        pass
    
    def fit(self, X, y):
        """Fit training data
        
        Parameters:
        X: {array-like}, shape={n_examples, n_features}, Training vectors, where n_examples is
        the number of examples and n_features is the number of features.

        y: array-like, shape=[n-examples]
        Target values.

        Returns self : object
        """