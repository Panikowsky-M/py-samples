# Даны результаты забегов в формате "h|m|s, h|m|s, h|m|s" (h – часы, m – \
# минуты, s – секунды).
# Написать функцию stat, которая возвращает строку в формате "Range: hh|mm|ss 
# Average: hh|mm|ss"
# (range – разница между максимальным и минимальным значением, 
# average – среднее значение)
#
# Пример:
# stat("01|15|59, 1|47|6, 01|17|20, 1|32|34, 2|3|17") ==> "Range: 00|47|18 
# Average: 01|35|15"


import traceback

from datetime import timedelta
from time import gmtime,strftime,strptime

def stat(x):
    def fmt_tDelta(tDelta):
        return strftime("%H|%M|%S", gmtime(tDelta.seconds) )

    tList = []
    for t in x.split(', '):
        h,m,s = map(int, t.split('|'))
        tList.append(timedelta(hours = h,minutes = m,seconds = s))

    rng = fmt_tDelta(max(tList) - min(tList))
    avg = fmt_tDelta(sum(tList,timedelta()) / len(tList))
    return f"Range: {rng} Average: {avg}"
#print(stat("01|15|59, 1|47|16, 01|17|20, 1|32|34, 2|17|17"))
# Тесты
try:
    assert stat("01|15|59, 1|47|16, 01|17|20, 1|32|34, 2|17|17") ==\
    "Range: 01|01|18 Average: 01|38|05"
    assert stat("02|15|59, 2|47|16, 02|17|20, 2|32|34, 2|17|17, 2|22|00,\
           2|31|41") == "Range: 00|31|17 Average: 02|26|18"
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
