import re
import json

FILENAME = 'testfile'

class Config(object):

    rex_start = re.compile(r"""^<(?P<name>[^/\s>]+)\s*(?P<value>[^>]+)?>$""")
    rex_end = re.compile(r"""^</(?P<name>[^\s>]+)\s*>$""")
    rex_comment = re.compile(r"""^#.*$""")

    def __init__(self, name, vals=[]):
        self.name = name
        self.vals = vals
        self.attribs = []
        self.children = []
        
    def find(self, path):
        pathPoint = path.strip("/").split("/")
        if pathPoints[0] == '':
            return self
        return self._find(pathPoints)


    def search(self, pathPoints):
        if pathPoints: 
            next = pathPoints.pop(0)
            for child in self.children:
                if child.name == next:
                    result = child._find(pathPoints)
                    if result:
                        return result
            return None
        else: 
            return self


    def findall(self, path):
        pathPoints = path.strip("/").split("/")
        if pathPoints[0] == '':
            return [self]
        return self._findall(pathPoints)


    def searchall(self, pathPoints):
        if pathPoints: 
            result = []
            next = pathPoints.pop(0)
            for child in self.children:
                if child.name == next:
                    result.extend(child._findall(pathelements))
            return result
        else:
            return [self]

    def _attrib(self, name, vals ):
        setattr( self, name, vals )
        self.attribs.append( name )
        
    def childAppend(self, name, vals):
        child = Config(name, vals)
        self.children.append(child)
        child.parent = self
        self.attribs.append( child )

        attr = getattr( self, name, None )
        if attr != None:
            if type(attr) == list:
                attr.append( child )
            else:
                attr = [attr,child,]
            setattr( self, name, attr )
        else:
            setattr( self, name, child )

        return child

    def print_json(self, indt = 0):
        if indt == 0:
            print("{")
            indt += 1

        if self.vals != []:
            print ("    " * indt + '"атрибут": %s,'%json.dumps(self.vals))
        for attribute in self.attribs[:-1]:
            if type(attribute) != Config:
                print( "    " * indt + '"' + attribute + '":' + json.dumps(getattr(self, attribute, None)) + ",")
            else:
                print ("    " * indt + '"' + attribute.name + '":{')
                attribute.print_json(indt+1)
                print ("    " * indt + "},")
        else:
            if type(self.attribs[-1]) != Config:
                print( "    " * indt + '"' + self.attribs[-1] + '":' + json.dumps(getattr(self, self.attribs[-1], None)) )
            else:
                print ("    " * indt + '"' + self.attribs[-1].name + '":{')
                self.attribs[-1].print_json(indt+1)
                print ("    " * indt + "}")
        
        if indt == 1:
            print("}")


    @classmethod
    def pars_file(cls, file):
        f = open(file)
        root = cls._pars(f)
        f.close()
        return root

    @classmethod
    def _pars(cls, itobj):
        root = node = Config('root')
        for line in itobj:
            line = line.strip()
            

            # Если строка пустая или это комментарий, то пропускаем 
            if (len(line) == 0) or cls.rex_comment.match(line):
                continue

            # Если найдено начало блока, добавляем его как дочерний элемент
            match = cls.rex_start.match(line)
            if match:
                vals = match.group("value").split()
                node = node.add_child(match.group("name"), vals)
                continue

            # Возвращаемся на родителя если найден конец блока
            match = cls.rex_end.match(line)
            if match:
                if node.name != match.group("name"):
                    raise Exception("Ошибка: '"+match.group("name")+"' должен быть '"+node.name+"'")
                node = node.parent
                continue
            
            """
             Если строка - не начало или конец,
             то это параметр, добавляем его в свойства узла
             и делаем его свойством класса
            """

            vals = line.split()
            name = vals.pop(0)
            if len(vals) == 1:
                vals = vals[0].strip('"')
            node._attrib(name, vals)
        return root
    
conf=Config.pars_file(FILENAME)

conf.print_json()
