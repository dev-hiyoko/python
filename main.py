# １行で複数処理をかける
hInt = 123; hStr = 'abc';
# 浮動小数方は紙数表記が可能
hFloat = 1.23e-5 # 1.23 * 10 ^ -5
# 演算子の一部
hBool = 100 < hInt and hInt < 200
hBool2 = 100 < hInt < 200

# リスト
hList = [1, 2, 3, 4, 5, 6]
hVal = hList[2]
hList.append(7)
hList[3]=8

# タプル （値が変更できないリスト）
hTuple = (1, 2)
hSimpleTuple = (1,) # シンプルなものは.（カンマ）が必要

# リストやタプルでは下記の様にそれぞれ入れることが可能
hTupleVal1, hTupleVal2 = hTuple

# if
if hBool:
    print('hBool is True')
elif hBool2:
    print('hBool2 is True')
else:
    print('hBool is False')

# for(in)
for i in hList:
    print(i)
# for(range)
# for i in range(10): 開始が０からの場合は省略可能
for i in range(1, 10):
    print(i)

# 関数
def add(a, b):
    return a + b
# アスタリスクを利用することで複数渡すことが可能
print(add(*hTuple))
def add2(a, b=1, c=2):
    return a + b + c

# スコープ
gInt = 100
def func():
    # グローバル変数を変更したい場合
    global gInt
    gInt = 200
print(gInt)

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
