from person import Person

class Nurse(Person):

    def __init__(self,name,surname,age):
       Person._start(self,state,shed,lic)
       self.shedule = {}
    
    def addWorkDay(self,day,time):
        self.shedule[day] = time
    
    def removeDish(self, dish):
        self.shedule.pop(day)
    
    def Nprint(self):
        res=""
        for shed in self.shedule.keys():
            res+="{} - Часы работы: {}\n".format(shed, self.shedule[shed])
        return res
    
    def setspeciality(self, spec):
        self.spec = speciality
    
    def __str__(self):
        return "{} {}, {} лет, {}".format(self.name, self.surname, self.age,\
               self.speciality)

