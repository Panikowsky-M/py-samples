import pickle
person = {'name':'Max','phones':[456,4831]}

with open('person.dat','wb') as file:

    pickle.dump(person,file)

print('Структура была записана\
 в файл: person.dat\n')

print('Вот вывод записанной\
 структуры в формате pickle\n')

d = open('person.dat','rb')
cat = d.readlines()
print(cat,'\n')
