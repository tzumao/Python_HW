class People:
    def __init__(self, name, id, height, weight):
        self.name = name
        self.id = id
        self.height = height
        self.weight = weight
    def BMI(self):        
        return self.weight/(self.height/100)/(self.height/100)
    def print(self):
        print('姓名：',self.name)
        print('號碼：',self.id)
        print('身高：',self.height)
        print('體重：',self.weight)
class Man(People):
    def __init__(self, name, id, height, weight, company, job):
        super().__init__(name,id,height,weight)
        self.company=company
        self.job=job
    def BMI(self):
        return super().BMI()*1.1
    def print(self):
        super().print()
        print('公司：',self.company)
        print('職務：',self.job)
class Woman(People):
    def __init__(self, name, id, height, weight, city, child):
        super().__init__(name,id,height,weight)
        self.city=city
        self.child=child
    def BMI(self):
        return super().BMI()*0.8
    def print(self):
        super().print()
        print('城市：',self.city)
        print('小孩：',self.child)
def Find_Max_BMI(*S):
    indexM=-1
    MaxM=0
    indexW=-1
    MaxW=0   
    for i in range(len(S)):
        if S[i].id[1]=='1':
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
M1=Man('Justin','L112654981',180,70,'FCU','Prof1')
M2=Man('Mark','L123456789',180,100,'NCU','Prof2')
M3=Man('Bob','L198715144',100,90,'NCHU','Prof3')
W1=Woman('Jennifer','L223456789',180,100,'Taichung',3)
W2=Woman('Tiffany','L295646521',100,90,'Taipei',5)
W3=Woman('Aaliyah','L233215458',180,70,'Tainan',4)
Find_Max_BMI(M2,M3,W1,W3,M1,W2)