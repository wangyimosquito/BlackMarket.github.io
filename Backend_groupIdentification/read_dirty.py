import json
import numpy as np

write_path = "../data/dirty_node10.json"

with open("./group10/node10.json",'r') as load_f:
    load_dict = json.load(load_f)
    # print(load_dict)

with open("./group10/link10.json",'r') as load_f:
    load_dict_link = json.load(load_f)

with open("./new_node/new_node5.json",'r') as load_f:
    node_json = json.load(load_f)
with open("./new_node/node5.json",'r') as load_f:
    new_node_json = json.load(load_f)

print(np.array(load_dict).shape)

try_dict = {}
try_dict["type"] = "force"

categories = [
        # 0
        {
            "name": "Erotic",
            "keyword": {}
        },
        #1
        {
            "name": "Gambling",
            "keyword": {}
        },
        #2
        {
            "name": "Gun",
            "keyword": {}
        },
        #3
        {
            "name": "Scam",
            "keyword": {}
        },
        #4
        {
            "name": "Illegal Trade",
            "keyword": {}
        },
        #5
        {
            "name": "Drug",
            "keyword": {}
        },
        #6
        {
            "name": "Hacker",
            "keyword": {}
        },
        #7
        {
            "name": "Illegal Payment",
            "keyword": {}
        },
        #8
        {
            "name": "Other indstry",
            "keyword": {}
        },
        #9
        {
            "name": "Mixed Industry",
            "keyword": {}
        },
        #10
        {
            "name": "Clean"
        }
    ]

try_dict["categories"] = categories

nodes = []
for i in range(np.array(load_dict).shape[0]):
    temp_dict = {}
    if node_json[load_dict[i]]['type'] != 'Domain':
        temp_dict["name"] = "Clean"
        temp_dict["category"] = 10
        # temp_dict["value"] = load_dict[i].split('_')[-1]
        temp_dict["value"] = node_json[load_dict[i]]['type']
    elif(len(node_json[load_dict[i]]['industry']) == 0):
        temp_dict["name"] = "Clean"
        temp_dict["category"] = 10
        #temp_dict["value"] = load_dict[i].split('_')[-1]
        temp_dict["value"] = node_json[load_dict[i]]['type']
    else:
        temp_dict["name"] = "Dirty"
        temp_dict["value"] = new_node_json[load_dict[i]]['industry']
        if(len(node_json[load_dict[i]]['industry']) > 1):
            temp_dict["category"] = 9
        elif(node_json[load_dict[i]]['industry'][0] == 'A'):
            temp_dict["category"] = 0
        elif(node_json[load_dict[i]]['industry'][0] == 'B'):
            temp_dict["category"] = 1
        elif(node_json[load_dict[i]]['industry'][0] == 'C'):
            temp_dict["category"] = 3
        elif(node_json[load_dict[i]]['industry'][0] == 'D'):
            temp_dict["category"] = 5
        elif(node_json[load_dict[i]]['industry'][0] == 'E'):
            temp_dict["category"] = 2
        elif(node_json[load_dict[i]]['industry'][0] == 'F'):
            temp_dict["category"] = 6
        elif(node_json[load_dict[i]]['industry'][0] == 'G'):
            temp_dict["category"] = 4
        elif(node_json[load_dict[i]]['industry'][0] == 'H'):
            temp_dict["category"] = 7
        else:
            temp_dict["category"] = 8
    nodes.append(temp_dict)

try_dict["nodes"] = nodes

links = []
for i in range(np.array(load_dict_link).shape[0]):
    temp_dict = {}
    for j in range(np.array(load_dict).shape[0]):
        if load_dict_link[i][0] == load_dict[j]:
            temp_dict["source"] = j
            break
    for j in range(np.array(load_dict).shape[0]):
        if load_dict_link[i][1] == load_dict[j]:
            temp_dict["target"] = j
            break
    #print(temp_dict)
    links.append(temp_dict)

try_dict["links"] = links

with open(write_path,"w") as f:
    json.dump(try_dict, f)
