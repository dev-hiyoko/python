import matplotlib.pyplot as plt
import numpy as np

# linspace
# 0から100までの範囲を等間隔で分割
# グラフのx軸の値を作成するときによく使う
# ls = np.linspace(0, 100)
# print(ls)
# print(len(ls))

x = np.linspace(-100, 100)
y_1 = 2 * x
y_2 = 3 * x
plt.plot(x, y_1, label="y1")
plt.plot(x, y_2, label="y2", linestyle="--")
plt.legend()
plt.show()

# 散布図
h_x = np.random.randn(1000)
h_y = np.random.randn(1000)
plt.scatter(h_x, h_y)
plt.show()

# ヒストグラム
i_x = np.random.randn(1000)
plt.hist(i_x, bins=50)
plt.show()

# 画像化
h_array= np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
plt.imshow(h_array, "gray")
plt.colorbar()
plt.show()
