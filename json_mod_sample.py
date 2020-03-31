import json

hum = [
    {'name':'Leo','age':23,'phones':[123,234]},
    {'name':'Shura','age':33,'phones':[101,102]},
]

print(type(hum))

json_hum = json.dumps(hum)

print(hum)
print(type(json_hum))

hum = json.loads(json_hum)

print(hum)
print(type(hum))
