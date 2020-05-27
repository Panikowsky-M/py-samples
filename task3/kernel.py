import traceback
from hospital import Hospital
from nurse import Nurse 
from doctor import Doctor 

try:
    d = Doctor("Александр", "Петров", 32)
    assert str(d) == "Петров Александр, 32 лет"

    d.addPatient(777,"Сергей","Бурунов")
    d.addPatient(778,"Александра","Бортич")
    assert d.Dprint()  == "Мед.книжка 777: Бурунов Сергей\nМед.книжка 778:\
 Бортич Александра\n"

    d.removePatient(778)
    assert d.Dprint() == "Мед.книжка 777: Бурунов Сергей\n"

    n = Nurse("Юрий","Никулин", 56)
    n.setspecialty("Нейрохирург")
    assert str(n) == "Юрий Никулин, 56 лет, Нейрохирург"

    n.addWorkDay("Вт","7:00-19:00")
    n.addWorkDay("Ср","16:30-16:30 след.")
    assert n.Nprint() == "Вт - Часы работы: 7:00-19:00\nСр\
 - Часы работы: 16:30-16:30 след.\n"

    n.removeWorkDay("Ср")
    assert n.Nprint() == "Вт - Часы работы: 7:00-19:00\n"

    #test = Hospital("Якитория", "ул. Ленина, 5/1")
    #tesr += c
    #tesr += w
    #assert str(f) == "Якитория, адрес: ул. Ленина, 5/1\nофицианты:\nИван Иванов, 20 лет\nповара:\nКито Иташима, 56 лет, японская кухня\n"
#assert len(f) == 2
#f -= w
#assert len(f) == 1
#
#f += w
#assert f.get(0) == w
#w2 = Waiter("Петр", "Петров", 30)
#f.replace(w2, 0) #assert f.get(0) == w2 #f.delete(0) #assert f.get(0) == c
#
#f += w
#f += w2
#f.toFile("якитория")

except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
