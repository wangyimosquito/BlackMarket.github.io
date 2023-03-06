import json

def checkAinB(filea):
    fa = open(filea,'r')
    
    lista = json.load(fa)
    
    for i in range(1,11):
        filename = 'json/node'+str(i)+'.json'
        listb = json.load(open(filename,'r'))
        chongfu = list(set(lista).intersection(set(listb)))
        chongfulv = len(chongfu)/len(lista)

        print("checking %s"%filea, "chongfu %.4f in %s"%(chongfulv, filename))

    



checkAinB('json/node9.json')