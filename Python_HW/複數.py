class Complex:
    def __init__(self,r,i):
        self.r=r
        self.i=i
    def add(self,a):
        return Complex(self.r+a.r,self.i+a.i)
    def minus(self,a):
        return Complex(self.r-a.r,self.i-a.i)
    def multi(self,a):
        r= self.r * a.r - self.i * a.i
        i= self.r * a.i + self.i * a.r
        return Complex(r,i)
    def div(self,a):
        mom = a.r **2 + a.i **2
        r= self.r * a.r + self.i * a.i
        i= self.r * a.i - self.i * a.r
        return Complex(r/mom,i/mom)
    def print(self):
        print("%.2f+%.2fi"%(self.r,self.i))
c1=Complex(4,5)
c2=Complex(2,-3)
c1.print()
c2.print()
c3=c1.add(c2)
c4=c1.minus(c2)
c6=c1.multi(c2)
c5=c1.div(c2)
c3.print()
c4.print()
c5.print()
c6.print()