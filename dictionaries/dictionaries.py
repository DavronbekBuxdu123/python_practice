capitals={
    "USA":"Washington",
    "Russia":"Moscow",
    "Germany":"Berlin",
    "Uzbekistan":"Tashkent"
}

print(capitals.get("USA"))

if capitals.get("Russia"):
    print("Found")
else:
    print("Not found")    

capitals.update({"Germany":"Tokio"})
capitals.pop("Germany")
capitals.popitem()
capitals.clear()
keys=capitals.keys()
print(keys)
for key in capitals.keys():
    print(key)
for value in capitals.values():
    print(value)    
print(capitals)

for item in capitals.items():
    print(item)

for key,value in capitals.items():
    print(f"{key} : {value}")    