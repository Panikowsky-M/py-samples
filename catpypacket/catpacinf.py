import requests, tarfile

FILENAME = 'testfile.tar.gz'
PATH = 'packet_extract'
META = 'generate_wiki-1.2.0/generate_wiki.egg-info/PKG-INFO'

#print('Загрузка сценария женкинса ... ')
print('Загрузка пакета ... ')

#fileToLoad = 'https://raw.githubusercontent.com/Panikowsky-M/docker/master/pipes/build_docker_pipe.jenkins'
fileToLoad  = 'https://files.pythonhosted.org/packages/57/54/5bff2bd5df319dd172610d9bf196040e28d7dcb1b6f074a7d9b908a37f9c/generate_wiki-1.2.0.tar.gz'

rq = requests.get(fileToLoad)

print('Статус запроса - %s'%(rq.status_code))
print('MIME загруженного файла - %s'%(rq.headers['content-type']))
print('Кодировка - %s'%(rq.encoding))


print('Пакет загружен')
with open(FILENAME,'wb') as _file:
    _file.write(rq.content)

print("Содержимое:\n")
with tarfile.open(FILENAME,"r") as arc:
    for lst in arc:
        print(lst.name)
        if lst.isreg():
            print("файл\n---")
        elif lst.isdir():
            print("папка\n---")
        else:
            print("сущ.\n---")
    meta = arc.extractfile(META)
    print("\nМетаданные пакета:\n====\n" +\
          meta.read().decode('utf-8') )

    """
    for inf in arc.getmembers():
        if fnmatch.fnmatch(inf.name,META):
            print(inf.name)
            arc.extract(inf.name,PATH)

    """
