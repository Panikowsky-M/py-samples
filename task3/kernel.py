import traceback
from hospital import Hospital
from nurse import Nurse 
from doctor import Doctor 

d = Doctor("Александр", "Петров", 32)
print(str(d))
#try:
#d = Doctor("Иван", "Иванов", 20)
#assert str(d) == "Иван Иванов, 20 лет"
#
#d.addPatient(12, 12000.50)
#d.addPatient(4, 4747.00)
#assert d.Dprint() == "стол 12: 12000.50 руб\nстол 4: 4747.00 руб\n"
#
#w.removeCheck(4)
#assert w.printChecks() == "стол 12: 12000.50 руб\n"
#
#c = Cook("Кито","Иташима", 56)
#c.setspeciality("японская кухня")
#assert str(c) == "Кито Иташима, 56 лет, японская кухня"
#
#c.addDish("роллы Филадельфия", 20)
#c.addDish("сет Саяке", 60)
#assert c.printDishs() == "блюдо роллы Филадельфия: 20 мин\nблюдо сет Саяке: 60 мин\n"
#
#c.removeDish("роллы Филадельфия")
#assert c.printDishs() == "блюдо сет Саяке: 60 мин\n"
#
#f = Cafe("Якитория", "ул. Ленина, 5/1")
#f += c
#f += w
#assert str(f) == "Якитория, адрес: ул. Ленина, 5/1\nофицианты:\nИван Иванов, 20 лет\nповара:\nКито Иташима, 56 лет, японская кухня\n"
#assert len(f) == 2
#f -= w
#assert len(f) == 1
#
#f += w
#assert f.get(0) == w
#w2 = Waiter("Петр", "Петров", 30)
#f.replace(w2, 0)
#assert f.get(0) == w2
#f.delete(0)
#assert f.get(0) == c
#
#f += w
#f += w2
#f.toFile("якитория")
#
#
#
#
#
#except AssertionError:
#print("TEST ERROR")
#traceback.print_exc()
#else:
#print("TEST PASSED")
