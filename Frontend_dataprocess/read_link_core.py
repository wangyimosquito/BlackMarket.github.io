
import json
from tokenize import String
import numpy as np

# node_data_path = 'Node.csv'
# link_data_path = 'Link.csv'

# node_json_path = 'new_node.json'
# link_json_path = 'link.json'

# IP_industry_json_path = 'IP_Industry.json'
# Cert_industry_json_path = 'Cert_Industry.json'

# Link_type_json_path = 'link_type.json'
# Connect_json_path = 'connect.json'

# 单引号改双引号
def one2two(line:String):
    l = list(line)
    for i in range(len(l)):
        if(l[i] == "'"):
            l[i] = '"'
    ans = ''.join(l)
    return ans

paths = []

write_path = "../data/core_link10.json"

with open("./core_paths/path_of_node10.json","r") as f:
    lines = f.readlines()
    for line in lines:
        line = one2two(line)
        #print(line)
        j = json.loads(line)
        paths.append(j)

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

init_nodes = []
nodes = []
for i in range(np.array(paths).shape[0]):
    for j in range(np.array(paths[i]).shape[0]):
        for k in range(np.array(paths[i][j]).shape[0]):
            node = paths[i][j][k]
            if node in init_nodes:
                continue
            else:
                init_nodes.append(node)
            temp_dict = {}
            temp_dict["value"] = node
            if node in load_dict_core:
                temp_dict["name"] = "Core Property"
                temp_dict["category"] = 0
                temp_dict["symbolSize"] = 10
            else:
                temp_dict["name"] = "Other Property"
                temp_dict["category"] = 1
                # temp_dict["symbolSize"] = 10
            print(temp_dict)
            nodes.append(temp_dict)
try_dict["nodes"] = nodes

print(len(nodes))

links = []
for i in range(np.array(paths).shape[0]):
    for j in range(np.array(paths[i]).shape[0]):
        temp_dict = {}
        for n in range(len(init_nodes)):
            if init_nodes[n] == paths[i][j][0]:
                temp_dict["source"] = n
                break
        for n in range(len(init_nodes)):
            if init_nodes[n] == paths[i][j][1]:
                temp_dict["target"] = n
                break
        print(temp_dict)
        if temp_dict in links:
            continue
        else:
            links.append(temp_dict)

try_dict["links"] = links

print(len(links))

with open(write_path,"w") as f:
    json.dump(try_dict, f)