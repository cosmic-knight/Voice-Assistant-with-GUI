import json

def dbPasser(names,reset=0):

    data=[]
    old_data=[]
    counter=""

    with open('pro_data.json','r') as f:
        json_object=json.loads(f.read())
        
    counter+=str(json_object)
    counter=counter.count("command")

    for i in range(counter):
        old_data.append(json_object[i]['command'])

    if reset==0:
        for i in old_data:
            a={"command":i}
            data.append(a)

    a={"command":names}
    data.append(a)
    data.reverse()
    json_string=json.dumps(data,indent=2)   #converts it into javascript compatible
    with open('pro_data.json','w') as f:
        f.write(json_string)

def clearer():
    with open('pro_data.json','w') as f:
        f.write("[]")