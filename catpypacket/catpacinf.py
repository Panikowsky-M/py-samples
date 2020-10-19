import io,zipfile
import requests,urllib
import xml.etree.ElementTree as xmlElement


print("Вводите название пакета:\n")
SEARCH = input()
LINK  = str('https://pypi.org/simple/%s' % SEARCH)


# Загрузим пакет с репозитория

def pullPacket(url):
    with urllib.request.urlopen(url) as _content:
        packContent = _content.read()
        print('Пакет загружен')
    return packContent


# Разбором html найдем пакет в формате whl

def getRepo(name):
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

pack = pullPacket(getRepo(SEARCH))

# Представление архива
arc = io.BytesIO(pack)
_zip = zipfile.ZipFile(arc)

metapath = [s for s in _zip.namelist() if "METADATA" in s][0]
print(metapath)

with _zip.open(metapath) as f:
    meta = f.read().decode("utf-8")

print("Метаданные:\n")
for line in meta.split("\n"):
    print(line)
