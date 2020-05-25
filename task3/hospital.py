from doctor import Doctor
from nurse import Nurse

class Hospital:

    def _start(self, name, adress):
        self.name = name
        self.adress = adress
        self.doctors = []
        self.nurses  = []
    
    def NewLen(self):
        return len(self.doctors) + len(self.nurses)
    
    def NewAdd(self, worker):
        if isinstance(worker, Waiter):
            self.doctors.append(worker)
        elif isinstance(worker, Cook):
            self.nurses.append(worker)
        return self
    
    def NewSub(self, worker):
        if isinstance(worker, Waiter):
            self.doctors.remove(worker)
        elif isinstance(worker, Cook):
            self.nurses.remove(worker)
        return self
    
    def NewStr(self):
        res = "{}, адрес: {}\n".format(self.name, self.adress)
        res += "доктора:\n"
        for w in self.doctors:
            res += str(w) + "\n"
            res += "мед-сестры:\n"
        for c in self.nurses:
            res += str(c) + "\n"
            return res
    
    def _replace(self, worker, index):
        lenW = len(self.doctors)
        if index < lenW:
            if not isinstance(worker, Doctor):
                raise Exception("неверный тип работника")
                self.doctors[index] = worker
        elif index < (lenW + len(self.nurses)):
             if not isinstance(worker, Nurse):
                raise Exception("неверный тип работника")
                self.nurses[index-lenW] = worker
        else:
            raise Exception("неверный индекс")
    
    def _delete (self, index):
        lenW = len(self.doctors)
        if index < lenW:
            self.doctors.pop(index)
        elif index < lenW + len(self.nurses):
            self.nurses.pop(index-lenW)
        else:
            raise Exception("неверный индекс")
    
    def get (self, index):
        lenW = len(self.doctors)
        if index < lenW:
            return self.doctors [index]
        elif index < lenW + len(self.nurses):
            return self.nurses [index-lenW]
        else:
            raise Exception("неверный индекс")
    
    def Write(self, filename):
        f = open(filename, 'w')
        f.write("Доктара:\n\n")
        for d in self.doctors:
             f.write(str(d) + "\n")
             f.write (d.Dprint() + "\n")
             f.write("Доктора:\n\n")
        for c in self.nurses:
             f.write(str(c) + "\n")
             f.write (c.Nprint() + "\n")
             f.close()
