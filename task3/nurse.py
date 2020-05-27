from person import Person

class Nurse(Person):

    def __init__(self,name,surname,age):
       Person.__init__(self,name,surname,age)
       self.shedule = {}
    
    def addWorkDay(self,day,time):
        self.shedule[day] = time
    
    def removeWorkDay(self, day):
        self.shedule.pop(day)
    
    def Nprint(self):
        res=""
        for shed in self.shedule.keys():
            res+="{} - Часы работы: {}\n".format(shed, self.shedule[shed])
        return res
    
    def setspecialty(self, specialty):
        self.spec = specialty
    
    def __str__(self):
        return "{} {}, {} лет, {}".format(self.name, self.surname, self.age,\
               self.spec)

