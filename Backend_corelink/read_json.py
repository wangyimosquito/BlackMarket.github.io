
from itertools import count
import json
from py2neo import Graph, Node, Relationship
import re
import sys
import numpy as np

class redirect:
    content = ""

    def write(self,str):
        self.content += str
    def flush(self):
        self.content = ""

def my_to_string(obj):
    r = redirect()
    backup = sys.stdout
    sys.stdout = r
    print(obj)
    sys.stdout = backup
    return r.content

def path2link(path):
    str = path[0][0]
    str = my_to_string(str)

    str1 = re.findall(r"id='(.+?)'",str)
    str2 = np.array(str1).reshape(-1,2).tolist()
    str3 = my_to_string(str2)
    str3 = str3.replace("'", '"')
    
    return str3

comms = []
filename = "group5.json"
with open('./连通性+子图数据/max_degree_node/%s'%filename,'r',encoding='utf8')as fp:
    json_data = json.load(fp)
    data_len = len(json_data)
    #print(data_len)
    for i in range(data_len):
        for j in range(i+1, data_len):
            #print(i, j)
            start_id = json_data[i]
            end_id = json_data[j]
            comm = "MATCH (x), (y), p=shortestPath((x)-[*0..10]-(y)) where x.id='%s' and y.id='%s' RETURN p"%(start_id, end_id)
            #print(comm)
            comms.append(comm)

# print(comms)
graph = Graph('http://localhost:7474/', auth=("neo4j", "huyiyao"))
# cursor = graph.run(comms[0])
# for record in cursor:
#     print(type(record[""]))
strs = []

count=0
for temp_comm in comms:

    output = graph.run(temp_comm).to_ndarray()

    str = path2link(output)
    
    strs.append(str)
    print(str)
    print(count)
    count+=1

with open("./paths/%s"%filename, "w", encoding='utf-8') as f:
    for temp_str in strs:
        f.write(temp_str)
    f.close()





