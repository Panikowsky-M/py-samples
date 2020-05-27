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

    n = Nurse("Ада","Лоулейс", 56)
    n.setspecialty("Нейрохирург")
    assert str(n) == "Ада Лоулейс, 56 лет, Нейрохирург"

    n.addWorkDay("Вт","7:00-19:00")
    n.addWorkDay("Ср","16:30-16:30 след.")
    assert n.Nprint() == "Вт - Часы работы: 7:00-19:00\nСр\
 - Часы работы: 16:30-16:30 след.\n"

    n.removeWorkDay("Ср")
    assert n.Nprint() == "Вт - Часы работы: 7:00-19:00\n"

    test = Hospital("Первая городская больница","ул.Фридриха-Энгельса, 6")
    test += d
    test += n
    assert str(test) == "Первая городская больница, адрес: ул.Фридриха-Энгельса, 6\nВрачи:\nПетров Александр, 32 лет\nМед-сестры:\nАда Лоулейс, 56 лет, Нейрохирург\n"
    assert len(test) == 2

    test-= n
    assert len(test) == 1
    
    test+= n 

    assert test.get(0) == d

    d1 = Doctor("Александра","Бортич",28)
    test.replace(d1,0)
    print(test.get(0))
    #assert test.get(0) == d2

    test._delete(0)

    assert test.get(0) == n

except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
