# import libraries
from polyr import PolyR
import numpy as np


# example 1 (simple using + ploting)
data = np.load(r'examples\example_1.npy')
p = 24

PolyR(max_p=p).fit(data[:,0],data[:,1]).plot_rmse()


# example 2 (define cv + prediction)
data = np.load(r'examples\example_2.npy')
samp = np.random.uniform(0,1,100)

y_prediction = PolyR(max_p=15,cv=4).fit(data[:,0],data[:,1]).predict(samp)


# example 3 (get betas vector)
data = np.load(r'examples\example_3.npy')

print(np.round(PolyR(max_p=70).fit(data[:,0],data[:,1]).betas,10))
