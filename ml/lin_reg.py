from sklearn import linear_model
reg = linear_model.LinearRegression()

# read csv

data = [
        [0, 0, 0], 
        [1, 1, 1], 
        [2, 2, 2],
        [3, 3, 3]
        ]

label = [0, 1, 0, 2]

reg.fit(data, label)
print(reg.coef_)
print(reg.predict([[0, 1, 2]]))
print(reg.predict([[3, 3, 3]]))
