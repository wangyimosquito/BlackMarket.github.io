
from asyncore import write
from importlib.resources import path
import json
from os import link
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

write_path = "../data/link10.json"

with open("./core_paths/path_of_node10.json","r") as f:
	lines = f.readlines()
	for line in lines:
		line = one2two(line)
		#print(line)
		j = json.loads(line)
		paths.append(j)

# print(np.array(paths).shape)

# for i in range(np.array(paths).shape[0]):
# 	print(np.array(paths[i]).shape)

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
        {
            "name": "IP_Info",
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
			temp_dict["value"] = node.split('_')[-1]
			if node.startswith("Domain"):
				temp_dict["name"] = "Domain"
				temp_dict["category"] = 0
			elif node.startswith("IP_CIDR"):
				temp_dict["name"] = "IP_CIDR"
				temp_dict["category"] = 4
			elif node.startswith("Cert"):
				temp_dict["name"] = "Cert"
				temp_dict["category"] = 2
				temp_dict["symbolSize"] = 10
			elif node.startswith("Whois_Name"):
				temp_dict["name"] = "Whois_Name"
				temp_dict["category"] = 3
			elif node.startswith("Whois_Phone"):
				temp_dict["name"] = "Whois_Phone"
				temp_dict["category"] = 3
			elif node.startswith("Whois_Email"):
				temp_dict["name"] = "Whois_Email"
				temp_dict["category"] = 3
			elif node.startswith("IP"):
				temp_dict["name"] = "IP"
				temp_dict["category"] = 1
				temp_dict["symbolSize"] = 10
			else:
				temp_dict["name"] = "ASN"
				temp_dict["category"] = 4
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