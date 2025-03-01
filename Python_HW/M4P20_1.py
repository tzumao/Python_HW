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
        S = super().Sampling()
        r=random.uniform(0,1)
        return Vertex(S.x+(self.C.x-S.x)*r,S.y+(self.C.y-S.y)*r)
def Sampling(S):
    return S.Sampling()
A=Vertex(0,0)
B=Vertex(0,3)
C=Vertex(3,3)
T=Triangle(A,B,C)
for i in range(1000):
    S=Sampling(T)
    print(S.x,S.y)
