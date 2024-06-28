import json

data={ "name":"oscar",
      "age":"18",
      "last name":"diaz"
}

datajson="data.json"

with open(datajson ,"w") as file:
    json.dump(data,file)
    