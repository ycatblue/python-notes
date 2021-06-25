d = {"aod": 89, "andy": 100, "candy": 76}
x = d["aod"]
y = d.keys()
print(x)
print(y)

d["aod"] = 22
d["anna"] = 100
print(y)
print(d)

if "aod" in d:
    print("yes,is in d")
else:
    print("no")