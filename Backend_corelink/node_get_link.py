import json


if(__name__=='__main__'):
    with open('json_hu/node6.json','r') as f_node:
        nodes = json.load(f_node)
        num_of_node = len(nodes)
        print(num_of_node)
