import json
import math
import random
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

def path2node(path):
    str = my_to_string(path)

    str1 = re.findall(r"id='(.+?)'",str)
    
    return str1

# class json2csv:
#     def __init__(self, link_str, node_str):
#         self.nodes_file = open('./reduced_subGraph2/%s'%node_str,'r',encoding='utf8')
#         self.link_file = open('./reduced_subGraph2/%s'%link_str,'r',encoding='utf8')

#     def getCSV():
#         pass


def full_connected_path(data_len:int):
    run_indexs = []
    for i in range(data_len):
        for j in range(i+1, data_len):
            run_indexs.append((i, j))

    return run_indexs


def random_connected_path(data_len:int):
    run_indexs = []
    for i in range(data_len):
        for j in range(i+1, data_len):
            run_indexs.append((i, j))

    p = math.log(data_len)/data_len
    ans = random.sample(run_indexs, 5*int(p * len(run_indexs)))

    ans.sort()
    return ans


def get_comms(filename):
    '''
    using each pair of node in filename , get the path command of these pairs.
    '''
    comms=[]
    
    with open('./task2/core_asset/%s'%filename,'r',encoding='utf8')as fp:
        json_data = json.load(fp)
        data_len = len(json_data)
        print (data_len)
        print (json_data)
        #run_indexs = full_connected_path(data_len)
        run_indexs = full_connected_path(data_len)
        for run_index in run_indexs:
            i, j = run_index
            print(i, j)
            start_id = json_data[i]
            end_id = json_data[j]

            comm = "MATCH (x), (y), p=shortestPath((x)-[*0..4]-(y)) where x.id='%s' and y.id='%s' RETURN p"%(start_id, end_id)
            #print(comm)
            comms.append(comm)

    return comms

def run_comms(comms):
    graph = Graph('http://localhost:7474/', auth=("reader", "huyiyao"))
    strs = []
    count=0
    for temp_comm in comms:
        print(count)
        output = graph.run(temp_comm).to_ndarray()
        print(output.shape)
        if(output.shape != (0,)):
            str = path2link(output)
        
            strs.append(str)
        else:
            str = 0

        
        print(str)
        count+=1

    return strs

if(__name__ == '__main__'):

    '''
    Get critical links
    '''
    filename = "node10.json"
    comms = get_comms(filename)
    print(len(comms))
    strs = run_comms(comms)


    with open("./core_paths/path_of_%s"%filename, "w", encoding='utf-8') as f:
        for temp_str in strs:
            f.write(temp_str)
        f.close()