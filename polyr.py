# Create by Etzion Harari
# https://github.com/EtzionR

# Load libraries:
import numpy as np
import matplotlib.pyplot as plt

# Define useful functions
create_matrix = lambda x, p: np.power(x, np.arange(p).reshape(p, 1)).T
create_polynm = lambda x, b: np.dot(create_matrix(x, len(b)), b)
b_coefficient = lambda x, y: np.dot(np.linalg.inv(np.dot(x.T, x)), np.dot(x.T, y))
rmse = lambda p, y: np.sqrt(np.mean(np.power(p - y, 2)))

# Define Polynom Object
class PolyR:
    """
    Polynomial Regression Object
    Optimize Model by fitting polynom degree
    """
    def __init__(self, max_p, cv=5):
        """
        initilize PolyR object
        :param max_p: max degree to check for fitting
        :param cv: number to K fold cross validation
        """
        self.p = None
        self.betas = None
        self.r_mse = None
        self.folds = None
        self.scores = {}
        self.max_p = max_p
        self.ary_p = np.arange(1, self.max_p + 1)
        self.cv = cv

    def fit(self, x, y):
        """
        fit betas vector for the input data
        :param x: x vector (independent variables)
        :param y: y vector (dependent variable)
        :return: The object
        """
        mat_x = create_matrix(x, self.max_p)
        self.folds = np.arange(mat_x.shape[0]) % self.cv

        for j in self.ary_p:
            self.scores[j] = self.cross_validation(mat_x[:, :j], y)

        self.p = min(self.scores, key=lambda k: self.scores[k])
        self.r_mse = self.scores[self.p]
        self.betas = b_coefficient(create_matrix(x, self.p), y)

        return self

    def predict(self, x):
        """
        predict y values using x values
        :param x: x vector (independent variables)
        :return:  y vector (dependent variable)
        """
        return create_polynm(x, self.betas)

    def cross_validation(self, x, y):
        """
        cross validation function
        using to prevent overfitting of the regression
        :param x: x matrix (independent variables)
        :param y: y vector (dependent variable)
        :return: RMSE for the model
        """
        cross_valid = []
        for k in np.arange(self.cv):
            trn = self.folds != k
            tst = self.folds == k

            x_trn = x[trn, :]
            y_trn = y[trn]
            x_tst = x[tst, :]
            y_tst = y[tst]

            betas = b_coefficient(x_trn, y_trn)
            y_prd = np.dot(x_tst, betas)

            cross_valid.append(rmse(y_prd, y_tst))
        return np.mean(cross_valid)

    def plot_rmse(self, size=10):
        """
        plot rmse result for each polynom degree
        :param size: plot size (default: 10)
        """
        vlu = self.scores.values()
        plt.figure(figsize=(size, size * .6))
        plt.title(f'RMSE for each Polynomial degree:\n[from 1 to {self.max_p}]', fontsize=14)
        plt.plot(self.scores.keys(), vlu, color='r', label='RMSE')
        plt.plot([self.p, self.p], [min(vlu), max(vlu)], color='k', linestyle='dotted', label='Minimum RMSE')
        plt.xlabel('Polynomial degree', fontsize=12)
        plt.ylabel('RMSE', fontsize=12)
        plt.legend(fontsize=12)
        plt.show()


# License
# MIT © Etzion Harari