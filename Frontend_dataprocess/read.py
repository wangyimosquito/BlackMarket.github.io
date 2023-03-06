from asyncore import write
import json
import numpy as np

write_path = "../data/subgraph10.json"

with open("./group10/node10.json",'r') as load_f:
    load_dict = json.load(load_f)
    # print(load_dict)

with open("./group10/link10.json",'r') as load_f:
    load_dict_link = json.load(load_f)

try_dict = {}

try_dict["type"] = "force"

categories = [
        {
            "name": "Domain",
            "keyword": {}
        },
        {
            "name": "IP",
            "keyword": {}
        },
        {
            "name": "Cert",
            "keyword": {}
        },
        {
            "name": "Whois_Info",
            "keyword": {}
        },
        # {
        #     "name": "Whois_Phone",
        #     "keyword": {}
        # },
        # {
        #     "name": "Whois_Email",
        #     "keyword": {}
        # },
        {
            "name": "IP_Info",
            "keyword": {}
        }
        # {
        #     "name": "ASN",
        #     "keyword": {}
        # }
    ]

try_dict["categories"] = categories

nodes = []
for i in range(np.array(load_dict).shape[0]):
    temp_dict = {}
    # temp_dict["name"] = load_dict[i]
    # temp_dict["value"] = 1
    temp_dict["value"] = load_dict[i].split('_')[-1]
    if load_dict[i].startswith("Domain"):
        temp_dict["name"] = "Domain"
        temp_dict["category"] = 0
    elif load_dict[i].startswith("IP_CIDR"):
        temp_dict["name"] = "IP_CIDR"
        temp_dict["category"] = 4
    elif load_dict[i].startswith("Cert"):
        temp_dict["name"] = "Cert"
        temp_dict["category"] = 2
        temp_dict["symbolSize"] = 15
    elif load_dict[i].startswith("Whois_Name"):
        temp_dict["name"] = "Whois_Name"
        temp_dict["category"] = 3
    elif load_dict[i].startswith("Whois_Phone"):
        temp_dict["name"] = "Whois_Phone"
        temp_dict["category"] = 3
    elif load_dict[i].startswith("Whois_Email"):
        temp_dict["name"] = "Whois_Email"
        temp_dict["category"] = 3
    elif load_dict[i].startswith("IP"):
        temp_dict["name"] = "IP"
        temp_dict["category"] = 1
        temp_dict["symbolSize"] = 15
    else:
        temp_dict["name"] = "ASN"
        temp_dict["category"] = 4
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
