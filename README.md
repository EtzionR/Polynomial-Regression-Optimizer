# Polynomial-Regression-Optimizer
A regression model that find the optimal polynomial-degree for the input data

## Overview
Polynomial regression is a statistical **machine learning** tool tool that allows us to find a simple model that fits between our features and the data we want to predict. In contrast to the simple linear model, polynomial regression can predict complex and diverse functions. This feature makes polynomial regression a useful tool in the field of Machine Learning. We can be seen example of fitting curve using Polynomial Regression:

![fit](https://github.com/EtzionR/Polynomial-Regression-Optimizer/blob/main/pictures/fitting.png)

Polynomial regression is a simple **extension of the familiar linear model**. As we know, the simple linear model fit a **beta** vector to the matrix of X values, so that they give a prediction to the Y values. The matrix shape can be in a high dimension or also in dimension 1 (vector). In the case of polynomial regression, the model receives vector X and vector Y. Then, the model converts vector x to a matrix, so that each column represents a different rank of the polynomial degree. This means that each column in the matrix is a version of the vector x values under a different power (0,1,... until the polynom degree). Now, we can just use the matrix in the familiar **multi-dimensional** linear model. The model allows us to find a beta vector in dimension P (the polynomial degree) that matches the data to the corresponding Y values.
We can display the Linear-Polynomial Model as follow:

<img src="https://latex.codecogs.com/svg.image?Y&space;=&space;\beta&space;\cdot&space;X^{P}&space;&plus;&space;\varepsilon" title="Y =   X^{P} \cdot \beta + \varepsilon" />

When:

<img src="https://latex.codecogs.com/svg.image?p^{1\times&space;P},&space;\beta^{P\times&space;1},&space;x^{n\times&space;1},&space;(X^{P})^{n\times&space;P},&space;\varepsilon^{1\times&space;n},&space;Y^{n\times&space;1}&space;&space;" title="p^{1\times P}, \beta^{P\times 1}, X^{n\times P}, \varepsilon^{1\times n}, Y^{n\times 1} " />

<img src="https://latex.codecogs.com/svg.image?\varepsilon&space;=&space;N(0,\sigma)" title="\varepsilon = N(0,\sigma)" />,

<img src="https://latex.codecogs.com/svg.image?p&space;=&space;\begin{Bmatrix}0&space;&&space;1&space;&&space;2&space;&&space;\cdots&space;&space;&&space;P&space;\\\end{Bmatrix}" title="p = \begin{Bmatrix}0 & 1 & 2 & \cdots & P \\\end{Bmatrix}" />, 

<img src="https://latex.codecogs.com/svg.image?X^{P}&space;=&space;\begin{bmatrix}&space;1&space;&&space;&space;x_{1}&space;&&space;&space;x_{1}^{2}&space;&&space;\cdot&space;\cdot&space;\cdot&space;&space;&space;&&space;x_{1}^{p}&space;\\&space;1&space;&&space;&space;x_{2}&space;&&space;&space;x_{2}^{2}&space;&&space;\cdot&space;\cdot&space;\cdot&space;&space;&space;&&space;x_{2}^{p}&space;\\\cdot&space;\cdot&space;\cdot&space;&&space;\cdot&space;\cdot&space;\cdot&space;&&space;\cdot&space;\cdot&space;\cdot&space;&&space;\cdot&space;\cdot&space;\cdot&space;&&space;\cdot&space;\cdot&space;\cdot&space;\\&space;1&space;&&space;&space;x_{n}&space;&&space;&space;x_{n}^{2}&space;&&space;\cdot&space;\cdot&space;\cdot&space;&space;&space;&&space;x_{n}^{p}&space;\\\end{bmatrix}" title="X^{P} = \begin{bmatrix} 1 & x_{1} & x_{1}^{2} & \cdot \cdot \cdot & x_{1}^{p} \\ 1 & x_{2} & x_{2}^{2} & \cdot \cdot \cdot & x_{2}^{p} \\\cdot \cdot \cdot & \cdot \cdot \cdot & \cdot \cdot \cdot & \cdot \cdot \cdot & \cdot \cdot \cdot \\ 1 & x_{n} & x_{n}^{2} & \cdot \cdot \cdot & x_{n}^{p} \\\end{bmatrix}" />,

Using this method, we can adjust regression models to our data by defining different degrees of polynomials:

![degrees](https://github.com/EtzionR/Polynomial-Regression-Optimizer/blob/main/pictures/various.png)

As you can see, some curves are more suitable for the original function, while others do not really seem to fit. Unfortunately, it is **not possible** to know what the proper polynomial degree to our data. Manual selection of a polynomial degree that is too low will result in an **underfitting** result and selection of a degree that is too high will result in an **overfitting** condition as well. Therefore, to find the degree that will lead to the optimal model, the [**polyr**](https://github.com/EtzionR/Polynomial-Regression-Optimizer/blob/main/polyr.py) code examines the polynomial model for a wide range of polynomial degrees, to find the one that leads to the best result. As can be seen in the following example:

![opt](https://github.com/EtzionR/Polynomial-Regression-Optimizer/blob/main/pictures/curve.gif)

As can be seen, each degree of polynomial leads to other errors value (in our case RMSE). In our case, the values that lead to the best results seem to be between 15 and 20. This means that the [**polyr**](https://github.com/EtzionR/Polynomial-Regression-Optimizer/blob/main/polyr.py) code will choose the betas vector that are based on the optimal polynomial degree. All that remains for the user is to define the range of values for which the various models will be tested. The range can be set using the **max_p** parameter. To prevent overfitting, the code uses the **k-folds cross validation** method, where its value can be adjusted via the **cv** parameter (default = 5)

In addition, the [**polyr**](https://github.com/EtzionR/Polynomial-Regression-Optimizer/blob/main/polyr.py) code has inside plot function to display the error results of each tested model. To use this function all you have to do is follow the following example code:

``` sh
# import code
from polyr import PolyR
import numpy as np

# load data
matrix = np.load('matrix.npy')
x, y   = matrix[:,0], matrix[:,1]

# using the code
PolyR(max_p=29).fit(x,y).plot_rmse()
```
![plot](https://github.com/EtzionR/Polynomial-Regression-Optimizer/blob/main/pictures/rmse.png)

All mathematical calculations performed in the code are implemented using the **numpy** library. With the use of this library it is possible to ensure efficient realization of the various regressive models and quickly find the appropriate polynomial degree.

## Libraries
The code uses the following library in Python:

**matplotlib**

**numpy**

## Application
An application of the code is attached to this page under the name: 

[**implementation.py**](https://github.com/EtzionR/Polynomial-Regression-Optimizer/blob/main/implementation.py)

The examples and the outputs are also attached here: [examples](https://github.com/EtzionR/Polynomial-Regression-Optimizer/tree/main/examples) & [outputs](https://github.com/EtzionR/Polynomial-Regression-Optimizer/tree/main/pictures).


## Example for using the code
To use this code, you just need to import it as follows:
``` sh
# import code
from polyr import PolyR
import numpy as np

# load data
train = np.load('train.npy')
test  = np.load('test.npy')

# define variables
max_p   = 30
cv      = 7
x_test  = test[:,0]
x_train = train[:,0]
y_train = train[:,1]

# using the code
y_prediction = PolyR(max_p = max_p,cv = cv).fit(x_train,y_train).predict(x_test)
```

When the variables displayed are:

**max_p:** maximum polynomial degree to check

**cv:** k value for k-folds cross validation (defualt = 5)

## License
MIT ?? [Etzion Harari](https://github.com/EtzionR)
