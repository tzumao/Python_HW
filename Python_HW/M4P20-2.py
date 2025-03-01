import random
import math

class Vertex:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, A, B):
        self.A = A
        self.B = B

    def Sampling(self):
        r = random.uniform(0, 1)
        return Vertex(self.A.x + (self.B.x - self.A.x) * r, self.A.y + (self.B.y - self.A.y) * r)

class Square(Line):
    def __init__(self, A, B, C, D):
        self.A = A  
        self.B = B 
        self.C = C 
        self.D = D 

    def Sampling(self):
        r_x = random.uniform(0, 1)
        r_y = random.uniform(0, 1)
        x = self.A.x + r_x * (self.B.x - self.A.x)
        y = self.A.y + r_y * (self.D.y - self.A.y)
        return Vertex(x, y)

def Sampling(S):
    return S.Sampling()

A = Vertex(0, 0)
B = Vertex(3, 0) 
C = Vertex(3, 3)
D = Vertex(0, 3) 

Sq = Square(A, B, C, D)

for i in range(1000):
    S = Sampling(Sq)
    print(S.x, S.y)
