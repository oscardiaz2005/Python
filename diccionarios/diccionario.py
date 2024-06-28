data={"document" : 123435,
      "name" : "oscar",
      "last name" : "diaz",
      "emails" :["pepe@gmail","oscar@gmail"]
      }

print(data)
print(data["document"])
print(data["emails"])
print(data["emails"][1])
print(data.values()) #all values
print(data.keys()) #all keys
data["phone"]=312812312 #add
data["document"]=222222 #modify
del data ["phone"] #delete
print(data)

datatwo={
    "1":{"document" : 123435,
      "name" : "oscar",
      "last name" : "diaz",
      "emails" :["pepe@gmail","oscar@gmail"]
      },
    "2":{"document" : 6546456,
      "name" : "juli",
      "last name" : "hernandez",
      "emails" :["peperepe@gmail","oscarin@gmail"]
      },  
    "3":{
        "document" : 43534,
      "name" : "juan",
      "last name" : "cruz",
      "emails" :["pepereperin@gmail","oscarinpepe@gmail"]
      ,

    }  
}

for k ,v in datatwo.items(): #run all diccionary
    for a, b in v.items(): #run each diccionary
        print(a," ",b)


