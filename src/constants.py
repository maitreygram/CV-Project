import numpy as np
F= 1
W = 500
H = 500

K = np.array([[F, 0, W//2], [0, F, H//2], [0, 0, 1]], dtype=float)
Kinv = np.linalg.inv(K)
