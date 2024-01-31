a={"Name":"Akhila","Age":24,"Place":"Pta"}

print(a["Age"])
c=a.get("Name")
print(c)
d=a.keys()
print(d)
e=a.values()
print(e)
f=a.items()
print(f)

a.update({"Course":"ML"})
print(a)
a.pop("Age")
print(a)
a.popitem()
print(a)

dict1=a.copy()
print(dict1)

dict2={{"Fruit":"Apple"},
       {"Fruit":"banana"
    
}
       }
