from person import Person

class Doctor(Person):

    def _start(license,specialty,age,surname,name):
        super()._start(license,specialty)
        self.licNum = license
        self.spec = specialty
        self.patList = {}

    def addPatient(self,card,name,surname):
        self.patList[card] = [surname,name]
    
    def removePatient(self,card):
        self.patList.pop(card)
    
    def Dprint(self):
        res=""
        for card in self.patList.keys():
            res+="Мед.книжка {0}: {} \n".format(card, self.patList[card])
        return res
    
    def strNew(self):
        return "{} {}, {} лет".format(self.surname, self.name, self.age)
