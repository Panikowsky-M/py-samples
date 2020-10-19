import requests
import xml.etree.ElementTree as xmlElement
import tarfile


print("Вводите название пакета:\n")
SEARCH = input()
FILENAME = 'testfile.tar.gz'
LINK  = str('https://pypi.org/simple/%s' % SEARCH)

def printRepo(name):
    rq = requests.get(LINK)
    print('Статус запроса - %s'%(rq.status_code))
    print('MIME загружаемого файла - %s'%(rq.headers['content-type']))
    print('Кодировка - %s'%(rq.encoding))
    docRoot = xmlElement.fromstring(rq.content)
    pack_link = None
    for el in docRoot[1]:
        if el.tag == "a":
            url = el.attrib["href"]
            if ".whl#" in url:
                pack_link = url
    return pack_link

print(printRepo(SEARCH))

"""
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

    for inf in arc.getmembers():
        if fnmatch.fnmatch(inf.name,META):
            print(inf.name)
            arc.extract(inf.name,PATH)

    """
