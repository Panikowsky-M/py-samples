from person import Person

class Doctor(Person):

    def __init__(self,surname,name,age):
        super(Person,self).__init__(surname,name,age)
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
