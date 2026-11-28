# import time

# def ggg():
#     pprev = 1
#     prev = 1
#     while True:
#         cur = pprev + prev
#         pprev = prev
#         prev = cur
#         yield cur

# g = ggg()
# while True:
#     time.sleep(0.1)
#     print(next(g))

# import numpy as np

# a = np.array([1, 2, 3])
# b = np.array(x for x in range(3))
# print(b)

# """28 ноября"""
# from sklearn import datasets, linear_model, model_selection, svm

# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.markers import MarkerStyle

# n_samples = 2000
# random_state = 123
# train_size = 700

# A, y = datasets.make_blobs(n_samples=n_samples, centers = 1, random_state=random_state)
# colors = np.array(['xkcd:bright blue', 'gold'])
# # plt.scatter(X[:, 0], X[:,1], s=7, color=colors[y-1])

# transformation = [[0.6, 0.6], [0.4, 0.8]]
# A_aniso = np.dot(A, transformation)
# # plt.scatter(A_aniso[:, 0], A_aniso[:,1], s=7, color=colors[y-1])

# A_train = A_aniso[:train_size]
# A_test = A_aniso[train_size:]

# x_train = A_train[:,0]
# y_train = A_train[:,1]

# x_train = x_train.reshape((train_size, 1))
# y_train = y_train.reshape((train_size, 1))
# lreg = linear_model.LinearRegression().fit(x_train, y_train)
# print(lreg.coef_, lreg.intercept_)

# x_test = A_test[:,0]
# y_test = A_test[:,1]

# x_test = x_test.reshape((n_samples - train_size, 1))
# y_test = y_test.reshape((n_samples - train_size, 1))
# x_test.sort(axis=0)

# X_for_pred = x_test.copy()
# X_for_pred.sort(axis = 0)

# y_pred = lreg.predict(X_for_pred)

# y_cust = X_for_pred[:, 0]* lreg.coef_ + lreg.intercept_
# y_cust

# colors_pred = np.array(['xkcd:salmon', 'xkcd:bright purple'])
# plt.scatter(x_test[:, 0], color=colors[y_test-1], s=5)


# plt.plot(X_for_pred[:, 0], y_pred, color=colors_pred[0] )

# plt.show()
