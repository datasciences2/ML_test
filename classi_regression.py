# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 20:09:20 2021

@author: NEM'S
"""
#%matplotlib inline
from sklearn import linear_model
from sklearn.linear_model import LinearRegression
import  numpy  as  np 
import  matplotlib.pyplot  as  plt 
#import  seaborn  as  sns ;  sns . ensemble ()
from sklearn.datasets import make_blobs
X, y = make_blobs(100, 4, centers=1, random_state=3, cluster_std=1.5)

# model = linear_model.LinearRegression()
# model.fit(X, y)

# print(model.coef_, model.intercept_)
# a = model.coef_
# b = model.intercept_

plt.scatter(X[:, 0],X[:, 2],  c=y, s=60, cmap='coolwarm_r');#X[:, 1],
# ordonne = np.linspace(0,15,1000)
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree=2)
X_poly = poly_reg.fit_transform(X)

X_poly     # prints X_poly
 
lin_reg2 = LinearRegression()
lin_reg2.fit(X_poly,y)
X_grid = np.arange(min(X),max(X),0.1)
X_grid = X_grid.reshape(len(X_grid),1)
plt.scatter(X[:, 0],X[:, 2],y)
plt.plot(X_grid, lin_reg2.predict(poly_reg.fit_transform(X_grid)),color='blue')
plt.show()
# plt.plot(ordonne,a*ordonne+b,color='r')
# plt.show()