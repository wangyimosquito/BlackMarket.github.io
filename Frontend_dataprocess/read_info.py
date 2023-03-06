import json
import numpy as np

write_path = "../data/dirty_node5.json"

with open("./group_member_list/group_info5.json",'r') as load_f:
    load_dict = json.load(load_f)
print(len(load_dict))