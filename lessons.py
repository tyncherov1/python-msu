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

import numpy as np

a = np.array([1, 2, 3])
b = np.array(x for x in range(3))
print(b)
