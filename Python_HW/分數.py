from math import gcd

class Fraction:
    def __init__(self, n, d):
        if d == 0:
            raise ValueError("Denominator cannot be zero.")
        self.n = n  # 分子
        self.d = d  # 分母
        self.simplify()

    def simplify(self):
        """將分數化為最簡形式"""
        g = gcd(self.n, self.d)
        self.n //= g
        self.d //= g
        if self.d < 0:
            self.n *= -1
            self.d *= -1

    def add(self, other):
        """加法"""
        n = self.n * other.d + other.n * self.d
        d = self.d * other.d
        return Fraction(n, d)

    def sub(self, other):
        """減法"""
        n = self.n * other.d - other.n * self.d
        d = self.d * other.d
        return Fraction(n, d)

    def mul(self, other):
        """乘法"""
        n = self.n * other.n
        d = self.d * other.d
        return Fraction(n, d)

    def div(self, other):
        """除法"""
        if other.n == 0:
            raise ValueError("Cannot divide by zero.")
        n = self.n * other.d
        d = self.d * other.n
        return Fraction(n, d)

    def __str__(self):
        """返回分數字串表示"""
        if self.d == 1:
            return str(self.n)
        return f"{self.n}/{self.d}"


# 測試程式
if __name__ == "__main__":
    f1 = Fraction(3, 4)  # 3/4
    f2 = Fraction(5, 6)  # 5/6

    print("分數1:", f1)
    print("分數2:", f2)

    # 加法
    res = f1.add(f2)
    print("\n加法結果:", res)

    # 減法
    res = f1.sub(f2)
    print("減法結果:", res)

    # 乘法
    res = f1.mul(f2)
    print("乘法結果:", res)

    # 除法
    res = f1.div(f2)
    print("除法結果:", res)
