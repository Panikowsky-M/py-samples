# Принимаем пакет и список зависимостей
# и выводим их

packages = dict(
        a = dict(depends = [["b"],["c"],["z"]], conflicts= []),
        b = dict(depends = [["d"]],conflicts=[]),
        c = dict(depends = [["d","e"],["f","g"]],conflicts = []),
        d = dict(depends = [],conflicts=["e"]),
        e = dict(depends = [],conflicts=[]),
        f = dict(depends = [],conflicts=[]),
        g = dict(depends = [],conflicts=[]),
        y = dict(depends = [["z"]],conflicts=[]),
        z = dict(depends = [],conflicts=[])
        )

def dep(p,deps):
    deps = " ".join(["%d" % d for d in deps])
    return "-%d %s" % (p,deps)


def confl(p, confls):
    confls = " ".join(["-%d" % c for c in confls])
    return "-%d %s" % (p,confls)

def buldFormula(packs, inst): # Получаем формулу для SAT-решателя
    idx = dict((i,k + 1) for k,i in enumerate(packs))
    suggs = []
    for p in packs:
        i = idx[p]
        pack = packs[p]
        if pack["depends"]:
            for d in pack["depends"]:
                # Предложение - строка ее надо завершить нулем
                suggs.append(dep(i, [ idx[x] for x in d]) + " 0")
            if pack["conflicts"]:
                suggs.append(confl(i, [ idx[x] for x in pack["conflicts"]]) + " 0")
    for i in inst:
        suggs.append("%d 0" % idx[i])
    return "\n".join(["p cnf %d %d" % (len(packs),len(suggs))] + suggs)

Formula = buldFormula(packages,["b","c"])
with open("packages-list.cnf","w") as wrotesolve:
    wrotesolve.write(Formula)
