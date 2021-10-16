# Polynomial-Regression-Optimizer
A regression model that find the optimal polynomial-degree for the input data

## Overview
Polynomial regression is a tool that allows us to find a simple model that fits between our features and the data we want to predict. In contrast to the simple linear model, polynomial regression can predict complex and diverse functions, as can be seen in the following example:

[fit](https://github.com/EtzionR/Polynomial-Regression-Optimizer/blob/main/pictures/fitting.png)

Polynomial regression is a simple **extension of the familiar linear model**. As we know, the simple linear model fit a **beta** vector to the matrix of X values, so that they give a prediction to the Y values. The matrix shape can be in a high dimension or also in dimension 1 (vector). In the case of polynomial regression, the model receives vector X and vector Y. Then, the model converts vector x to a matrix, so that each column represents a different rank of the polynomial degree. This means that each column in the matrix is a version of the vector x values under a different power (0,1,... until the polynom degree). Now, we can just use the matrix in the familiar **multi-dimensional** linear model. The model allows us to find a beta vector in dimension P (the polynomial degree) that matches the data to the corresponding Y values.
We can display the Linear-Polynomial Model as follow:

<img src="https://latex.codecogs.com/svg.image?Y&space;=&space;\beta&space;\cdot&space;X^{P}&space;&plus;&space;\varepsilon" title="Y =   X^{P} \cdot \beta + \varepsilon" />

When:

<img src="https://latex.codecogs.com/svg.image?p^{1\times&space;P},&space;\beta^{P\times&space;1},&space;x^{n\times&space;1},&space;(X^{P})^{n\times&space;P},&space;\varepsilon^{1\times&space;n},&space;Y^{n\times&space;1}&space;&space;" title="p^{1\times P}, \beta^{P\times 1}, X^{n\times P}, \varepsilon^{1\times n}, Y^{n\times 1} " />

<img src="https://latex.codecogs.com/svg.image?\varepsilon&space;=&space;N(0,\sigma)" title="\varepsilon = N(0,\sigma)" />,

<img src="https://latex.codecogs.com/svg.image?p&space;=&space;\begin{Bmatrix}0&space;&&space;1&space;&&space;2&space;&&space;\cdots&space;&space;&&space;P&space;\\\end{Bmatrix}" title="p = \begin{Bmatrix}0 & 1 & 2 & \cdots & P \\\end{Bmatrix}" />, 

<img src="https://latex.codecogs.com/svg.image?X^{P}&space;=&space;\begin{bmatrix}&space;1&space;&&space;&space;x_{1}&space;&&space;&space;x_{1}^{2}&space;&&space;\cdot&space;\cdot&space;\cdot&space;&space;&space;&&space;x_{1}^{p}&space;\\&space;1&space;&&space;&space;x_{2}&space;&&space;&space;x_{2}^{2}&space;&&space;\cdot&space;\cdot&space;\cdot&space;&space;&space;&&space;x_{2}^{p}&space;\\\cdot&space;\cdot&space;\cdot&space;&&space;\cdot&space;\cdot&space;\cdot&space;&&space;\cdot&space;\cdot&space;\cdot&space;&&space;\cdot&space;\cdot&space;\cdot&space;&&space;\cdot&space;\cdot&space;\cdot&space;\\&space;1&space;&&space;&space;x_{n}&space;&&space;&space;x_{n}^{2}&space;&&space;\cdot&space;\cdot&space;\cdot&space;&space;&space;&&space;x_{n}^{p}&space;\\\end{bmatrix}" title="X^{P} = \begin{bmatrix} 1 & x_{1} & x_{1}^{2} & \cdot \cdot \cdot & x_{1}^{p} \\ 1 & x_{2} & x_{2}^{2} & \cdot \cdot \cdot & x_{2}^{p} \\\cdot \cdot \cdot & \cdot \cdot \cdot & \cdot \cdot \cdot & \cdot \cdot \cdot & \cdot \cdot \cdot \\ 1 & x_{n} & x_{n}^{2} & \cdot \cdot \cdot & x_{n}^{p} \\\end{bmatrix}" />,

Unfortunately, it is **not possible** to know what is the rank of the polynomial from which the data before us were created. Manual selection of a polynomial degree that is too low will result in an **underfitting** result and selection of a degree that is too high will result in an **overfitting** condition as well. Therefore, to find the degree that will lead to the optimal model, the [**polyr**](https://github.com/EtzionR/Polynomial-Regression-Optimizer/blob/main/polyr.py) code examines the polynomial model for a wide range of polynomial degrees, to find the one that leads to the best result. As can be seen in the following example:

![opt](https://github.com/EtzionR/Polynomial-Regression-Optimizer/blob/main/pictures/curve.gif)



## Libraries
The code uses the following library in Python:

**matplotlib**

**numpy**

## Application
An application of the code is attached to this page under the name: 

[**implementation.py**]()

The examples and the outputs are also attached here: [examples]() & [outputs]().


## Example for using the code
To use this code, you just need to import it as follows:
``` sh

```

When the variables displayed are:

**aaa:** aaa

## License
MIT © [Etzion Harari](https://github.com/EtzionR)
