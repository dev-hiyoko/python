# １行で複数処理をかける
h_int = 123
h_str = 'abc'
# 浮動小数方は紙数表記が可能
h_float = 1.23e-5 # 1.23 * 10 ^ -5
# 演算子の一部
h_bool = 100 < h_int and h_int < 200
h_bool2 = 100 < h_int < 200

# リスト
h_list = [1, 2, 3, 4, 5, 6]
h_val = h_list[2]
h_list.append(7)
h_list[3] = 8

# タプル （値が変更できないリスト）
h_tuple = (1, 2)
h_simple_tuple = (1,) # シンプルなものは.（カンマ）が必要

# リストやタプルでは下記の様にそれぞれ入れることが可能
h_tuple_val1, h_tuple_val2 = h_tuple

# if
if h_bool:
    print('h_bool is True')
elif h_bool2:
    print('h_bool2 is True')
else:
    print('h_bool is False')

# for(in)
for i in h_list:
    print(i)
# for(range)
# for i in range(10): 開始が０からの場合は省略可能
for i in range(1, 10):
    print(i)

# 関数
def add(a, b):
    return a + b
# アスタリスクを利用することで複数渡すことが可能
print(add(*h_tuple))
def add2(a, b=1, c=2):
    return a + b + c

# スコープ
g_int = 100
def func():
    # グローバル変数を変更したい場合
    global g_int
    g_int = 200
print(g_int)

print('hello world')


# クラス
class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add(self, value):
        return self.a + self.b + value
c = Calculator(1, 2)
print(c.add(3))

# 継承
class ExtendedCalculator(Calculator):
    def mul(self, value):
        return self.a * self.b * value
ec = ExtendedCalculator(1, 2)
print(ec.add(3))
print(ec.mul(3))