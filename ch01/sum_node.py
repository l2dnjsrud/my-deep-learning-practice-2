import numpy as np
D, N = 8, 7
x = np.random.randn(N, D)  #입력
y = np.sum(x, axix = 0, keepdims = True)  #순전파

dy = np.random.randn(1, D)  #무작위 기울기
dx = np.repeat(dy, N, axis = 0)  #역전파