import requests

print('Загрузка сценария женкинса ... ')

fileToLoad = 'https://raw.githubusercontent.com/Panikowsky-M/docker/master/pipes/build_docker_pipe.jenkins'

rq = requests.get(fileToLoad)

print('Статус запроса - %s'%(rq.status_code))
print('Тип загруженного файла - %s'%(rq.headers['content-type']))
print('Кодировка - %s'%(rq.encoding))

print('Сценарий записан в файл')
with open('testfile','wb') as _Text:
     _Text.write(rq.content)
with open('testfile','r') as _Text2:
    for line in _Text2:
        print(line)
