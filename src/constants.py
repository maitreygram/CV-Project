import numpy as np
F= 135
W = 500
H = 500

I44 = np.eye(4)
K = np.array([[F, 0, W//2], [0, F, H//2], [0, 0, 1]], dtype=float)
Kinv = np.linalg.inv(K)