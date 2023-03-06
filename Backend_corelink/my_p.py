import json
from tokenize import String

# 单引号改双引号
def one2two(line:String):
    l = list(line)
    for i in range(len(l)):
        if(l[i] == "'"):
            l[i] = '"'
    ans = ''.join(l)
    return ans


filename = "group1.json"
with open("./paths/%s"%filename, "r", encoding='utf-8') as f:
    lines = f.readlines()
    #print(line)
    for line in lines:
        line = one2two(line)
        #print(line)
        j = json.loads(line)
        # blabla