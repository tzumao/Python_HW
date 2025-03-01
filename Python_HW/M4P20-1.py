import random
import math
class Vertex:
    def __init__(self,x,y):
        self.x=x
        self.y=y
class Line:
    def __init__(self, A, B):
        self.A = A
        self.B = B
    def Sampling(self):
        r=random.uniform(0,1)
        return Vertex(self.A.x+(self.B.x-self.A.x)*r,self.A.y+(self.B.y-self.A.y)*r)
class Triangle(Line):
    def __init__(self, A, B, C):
        super().__init__(A,B)
        self.C=C
    def Sampling(self):
        u = random.uniform(0, 1)
        v = random.uniform(0, 1)
        if u + v > 1:
            u = 1 - u
            v = 1 - v
        x = (1 - u - v) * self.A.x + u * self.B.x + v * self.C.x
        y = (1 - u - v) * self.A.y + u * self.B.y + v * self.C.y
        return Vertex(x, y)
def Sampling(S):
    return S.Sampling()
A=Vertex(0,0)
B=Vertex(0,3)
C=Vertex(3,3)
T=Triangle(A,B,C)
for i in range(1000):
    S=Sampling(T)
    print(S.x,S.y)
