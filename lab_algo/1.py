
# mean
def mean(x):
    return sum(x)/len(x)

#variance
def variance(x,x_mean):
    return sum([(i - x_mean)**2 for i in x])

#covariance
def covar(x,x_mean,y,y_mean):
    covar = 0
    for i,j in zip(x,y):
        covar += (i-x_mean)*(j-y_mean)
    return covar

# coefficients
def coeff(covar,x_var,y_mean,x_mean):
    b1 = covar/x_var
    b0 = y_mean - b1*x_mean
    return b0,b1

# linear regression
def linr(x,b0,b1):
    predicted = []
    for i in x:
        y = b0 + b1*i
        predicted.append(y)
    return predicted

# rmse
import math
def rmse(lr,y):
    er = 0
    for i,j in zip(lr,y):
        er += (i-j)**2 
    er_mean = er / len(y)
    return math.sqrt(er_mean)

# Test simple linear regression 
dataset = [[1, 1], [2, 3], [4, 3], [3, 2], [5, 5]]
x = [i[0] for i in dataset]
y = [i[1] for i in dataset]
print(x,y)

x_mean = mean(x)
y_mean = mean(y)
print(f"mean: {x_mean}")
print(f"mean: {y_mean}")

x_var = variance(x,x_mean)
y_var = variance(y,y_mean)
print(f"X_Variance: {x_var}")
print(f"Y_Variance: {y_var}")

covar = covar(x,x_mean,y,y_mean)
print(f"Covariance: {covar}")

# y = b0 + b1*x
b0,b1 = coeff(covar,x_var,y_mean,x_mean)
print(f"b0:{b0},b1:{b1}")

# linear regression
lr = linr(x,b0,b1)
print(f"Predicted Values: {lr}")

#rmse
r = rmse(lr,y)
print(f"RMSE:{r}")

