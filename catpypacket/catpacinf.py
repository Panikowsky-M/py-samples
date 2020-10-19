import io,zipfile
import requests,urllib
import xml.etree.ElementTree as xmlElement


print("Вводите название пакета:\n")
SEARCH = input()

# Загрузим пакет с репозитория

def pullPacket(url):
    with urllib.request.urlopen(url) as _content:
        packContent = _content.read()
        #print('Пакет загружен')
    return packContent


# Разбором html найдем пакет в формате whl

def getLink(name):
    LINK  = str('https://pypi.org/simple/%s' % name)
    rq = requests.get(LINK)
    #print('Статус запроса - %s'%(rq.status_code))
    #print('MIME загружаемого файла - %s'%(rq.headers['content-type']))
    #print('Кодировка - %s'%(rq.encoding))
    docRoot = xmlElement.fromstring(rq.content)
    pack_link = None
    for el in docRoot[1]:
        if el.tag == "a":
            url = el.attrib["href"]
            if ".whl#" in url:
                pack_link = url
    if pack_link == None:
        print("whl-архив не найден")
        return 0
    return pack_link

def getPacketMeta(packet):
    # Представление архива
    arc = io.BytesIO(packet)
    _zip = zipfile.ZipFile(arc)
    
    # Просмотр содержимого на предмет файла METADATA
    metapath = [s for s in _zip.namelist() if "METADATA" in s][0]
    #print(metapath)
    
    with _zip.open(metapath) as f:
        meta = f.read().decode("utf-8")
    
    return meta


def getPacketDeps(metainfo):
    deps = []
    for line in metainfo.split("\n"):
        line = line.split()
        if not line:
            break
        if line[0] == "Requires-Dist:" and "extra" not in line:
            deps.append(line[1])
    return deps

def getDepsGraph(name):
    graph = {}
    def rec(name):
        print(name)
        graph[name] = set()
        deps = getPacketDeps(\
                getPacketMeta(pullPacket(getLink(name))) )
        for d in deps:
            graph[name].add(d)
            rec(d)
    rec(name)
    return graph

print( getDepsGraph(SEARCH) )
