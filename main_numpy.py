import numpy as np

# 3次元配列
h_array = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]]])
print(h_array)
print(h_array * 2) # すべての要素に2を掛ける

# 要素の取得
m_array = np.array([[1, 2, 3], [4, 5, 6]])
print(m_array[1][2]) # 6

# 要素の変更
# m_array[1][2] = 10
m_array[1, 2] = 10
print(m_array)

# ブロードキャスト
i_array = np.array([1, 2, 3])
j_array = np.array([[4, 5, 6], [7, 8, 9]])
print(i_array + j_array) # i_arrayをj_arrayの行数に合わせて足し算

# shape 配列の形状を確認できる
k_array = np.array([[1, 2, 3], [4, 5, 6]])
print(k_array.shape)

# reshape 配列の形状を変更できる
l_array = np.array([1, 2, 3, 4, 5, 6])
print(l_array.reshape(2, 3))
print(h_array.reshape(-1)) # -1を指定すると、元の配列の要素数に合わせて形状を変更

# sum, max, min, mean
n_array = np.array([[1, 2, 3], [4, 5, 6]])
print("合計" ,n_array.sum())
print("合計(列)", n_array.sum(axis=0))
print("合計(行)", n_array.sum(axis=1))
print("最大値", n_array.max())
print("最小値", n_array.min())
print("平均値", n_array.mean())