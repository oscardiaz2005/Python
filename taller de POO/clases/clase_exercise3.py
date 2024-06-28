class Student :
    def __init__(self,name,age,qualifications) :
        self.name=name
        self.age=age
        self.qualifications=qualifications
    
    def average(self):
       return sum(self.qualifications) / len(self.qualifications) 

        
        