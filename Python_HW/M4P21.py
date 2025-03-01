class People:
    def __init__(self,name,ID,height,weight):
        self.name=name
        self.ID=ID
        self.height=height
        self.weight=weight
    def BMI(self):
        return self.weight/(self.height/100)/(self.height/100)
    def print(self):
        print("姓名:",self.name)
        print("ID:",self.ID)
        print("身高:",self.height)
        print("體重:",self.weight)   
class Man(People):
    def __init__(self, name, ID, height, weight, company, job):
        super().__init__(name, ID, height, weight)
        self.company=company
        self.job=job
    def BMI(self):
        return super().BMI()*1.1
    def print(self):
        super().print()
        print("公司:",self.company)
        print("職務:",self.job)
class Woman(People):
    def __init__(self, name, ID, height, weight, city, child):
        super().__init__(name, ID, height, weight)
        self.city=city
        self.child=child
    def BMI(self):
        return super().BMI()*0.8
    def print(self):
        super().print()
        print("城市:",self.city)
        print("小孩:",self.child)
def Find_Max_BMI(*S):
    indexM=-1
    MaxM=0
    indexW=-1
    MaxW=0   
    for i in range(len(S)):
        if S[i].ID[1]=='1':
            if S[i].BMI()>MaxM:
                MaxM=S[i].BMI()
                indexM=i
        else:
            if S[i].BMI()>MaxW:
                MaxW=S[i].BMI()
                indexW=i
    if indexM != -1:
        S[indexM].print()
    if indexW != -1:
        S[indexW].print()
M1=Man('Sam','L124365738',190,75,'FCU','Prof1')
M2=Man('Tommy','L194756354',180,90,'NCU','Prof2')
M3=Man('Peter','L104836254',170,80,'NTU','Prof3')
W1=Woman('Cindy','L29374657',160,60,'Taichung',3)
W2=Woman('Ruby','L21038475',150,45,'Taipei',2)
W3=Woman('Aalisa','L20948563',170,50,'Tainan',1)
Find_Max_BMI(M1,M2,M3,W1,W2,W3)

