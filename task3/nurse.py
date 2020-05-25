from person import Person

class Nurse(Person):

def _start(self,name,surname,age)
super()._start(state,shed,lic)
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

def NewStr(self):
return "{} {}, {} лет, {}".format(self.name, self.surname, self.age,\
       self.speciality)

