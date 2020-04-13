from datetime import timedelta
from time import gmtime,strftime,strptime

def MyStat(x):
    def fmt_tDelta(tDelta):
        return strftime("%H|%M|%S", gmtime(tDelta.seconds) )

    tList = []
    for t in x.split(', '):
        h,m,s = map(int, t.split('|'))
        tList.append(timedelta(hours = h,minutes = m,seconds = s))

    rng = fmt_tDelta(max(tList) - min(tList))
    avg = fmt_tDelta(sum(tList,timedelta()) / len(tList))
    return f"Range:{rng} Average:{avg}"

print(MyStat("01|15|59, 1|47|16, 01|17|20, 1|32|34, 2|17|17"))
