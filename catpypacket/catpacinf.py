import io,zipfile
import requests,urllib
from bs4 import BeautifulSoup as bSoup
import re


print("Вводите название пакета:\n")
SEARCH = input()

# Родительский и дочерний узел p,q
def graphViz(g):
    gvStrings = ["digraph G {"]
    for p in g:
        for q in g[p]:
            gvStrings.append('"%s" -> "%s"' % (p,q) )
    gvStrings.append("}")
    print("\n=============\nПостроенный граф зависимостей\n")
    return "\n".join(gvStrings)

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
    document = bSoup(rq.content,'html5lib')
    pack_link = None
    for l in document.find_all('a'):
        if re.findall('.whl#',str(l)):
            pack_link = l.get('href')
    if pack_link == None:
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
        line = line.replace(";","").split()
        if not line:
            break
        if line[0] == "Requires-Dist:" and "extra" not in line:
            deps.append(line[1])
    return deps

"""
         Получим граф составленный из зависимостей пакета
Будем заполнять узлы графа из найденных зависимостей пакета.
Зависимости - список, проитерируем его и и по каждой 
итерации будем рекурсивно звать функцию итерации зависимости
"""
def getDepsGraph(name):
    graph = {}
    def _walk(name):
        print("\n----\nЗависимости пакета :\n%s" % name)
        graph[name] = set()
        url = getLink(name)
        if not url:
            return
        deps = getPacketDeps( getPacketMeta(pullPacket(url)) )
        for d in deps:
            graph[name].add(d)
            if d not in graph:
                _walk(d)
    _walk(name)
    return graph

print("\nЧто следует делать с пакетом?\n")
In = int(input("1 - Вывести метаданные\n2 - Вывести зависимости\n\
3 - Построить граф зависимостей\n"))
if In == 1:
    print( getPacketMeta(pullPacket(getLink(SEARCH))) )
if In == 2:
    print( getPacketDeps(getPacketMeta(pullPacket(getLink(SEARCH)))) )
if In == 3:
    gr1 = getDepsGraph(SEARCH)
    print(graphViz(gr1))
