import json
import numpy as np

write_path = "../data/core10.json"

with open("./group10/node10.json",'r') as load_f:
    load_dict = json.load(load_f)
    # print(load_dict)

with open("./group10/link10.json",'r') as load_f:
    load_dict_link = json.load(load_f)

with open("./group10/core_node10.json",'r') as load_f:
    load_dict_core = json.load(load_f)

try_dict = {}

try_dict["type"] = "force"

categories = [
        {
            "name": "Core Property",
            "keyword": {}
        },
        {
            "name": "Other Property",
            "keyword": {}
        }
    ]

try_dict["categories"] = categories

nodes = []
for i in range(np.array(load_dict).shape[0]):
    temp_dict = {}
    temp_dict["value"] = load_dict[i]
    if load_dict[i] in load_dict_core:
        temp_dict["name"] = "Core Property"
        temp_dict["category"] = 0
        temp_dict["symbolSize"] = 15
        # temp_dict["itemStyle.borderWidth"] = 2
        # temp_dict["itemStyle.borderType"] = "Solid"
        # temp_dict["itemStyle.borderColor"] = "black"
    else:
        temp_dict["name"] = "Other Property"
        temp_dict["category"] = 1
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
    print(temp_dict)
    links.append(temp_dict)

try_dict["links"] = links

with open(write_path,"w") as f:
    json.dump(try_dict, f)