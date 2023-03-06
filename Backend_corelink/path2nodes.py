import json
from get_core_path import path2node

from py2neo import Graph


'''
该文件用于运行cypher语句找到目标团伙的节点,并自动检测是否与之前的团伙重复。
'''

def run_comm(comm):
    graph = Graph('http://localhost:7474/', auth=("reader", "huyiyao"))
    output = graph.run(comm)
    print("output got!")
    output = output.data()
    #print(type(output))
    print("output to sth !")
    
    str = path2node(output)
    print("output str got!")

    
    print(str)

    return str

def check_chongfulv(mylist):

    for i in range(1,10):
        filename = "node"+str(i)+".json"
        print("checking", filename)
        with open("./json/%s"%filename, 'r', encoding='utf-8') as f:
            json_data = json.load(f)
            chongfu = list(set(mylist).intersection(set(json_data)))
            chongfulv = len(chongfu)/len(mylist)
            if(chongfulv > 0.01):
                print(filename, "重复率: %s"%str(chongfulv))





if(__name__=='__main__'):
    comm = '''MATCH p=(d_start:Domain)-[:r_request_jump|r_subdomain *0..1]-(d1:Domain)-[:r_request_jump|r_subdomain *0..1]-(d2:Domain)-[:r_request_jump|r_subdomain *0..1]-(d_end:Domain)-[:r_dns_a]->(ip:IP) 
    OPTIONAL MATCH p1=(cert_start:Cert)-[:r_cert_chain*0..1]-(cert_end:Cert)<-[c2d:r_cert]-(d_start:Domain)
    where (cert_end.name<>'321294f7c6') and (d1.industry<>'[]' or d2.industry<>'[]' or d_start.industry<>'[]' or d_end.industry<>'[]')  
    return p,p1 limit 3000'''

    # 团伙6 ceab
    comm1 = '''MATCH p=(cert_start:Cert)-[:r_cert_chain*0..1]-(cert_end:Cert)<-[c2d:r_cert]-(d_start:Domain)-[:r_request_jump|r_subdomain *0..1]-(d1:Domain)-[:r_request_jump|r_subdomain *0..1]-(d2:Domain)-[:r_request_jump|r_subdomain *0..1]-(d_end:Domain)-[:r_dns_a]->(ip:IP) where (cert_end.name<>'321294f7c6') and (d1.industry<>'[]' or d2.industry<>'[]' or d_start.industry<>'[]' or d_end.industry<>'[]')  return p limit 3000'''
# 从cert开始找 comm1
    comm2 = '''
    MATCH p=(ip:IP{id:'IP_6acab66245718783adbe872ed865728ac828f4666834336e41ac3878e8cf1836'})<-[:r_dns_a]-(d_start:Domain)-[:r_request_jump|r_subdomain *0..3]-(d_end:Domain)-[d2c:r_cert]->(cert_start:Cert)-[:r_cert_chain*0..1]-(cert_end:Cert)--(d_others:Domain)-[:r_request_jump|r_subdomain *0..3]-(d_others_end:Domain)   
    where (cert_end.name<>'fe794a69ea') and (d_end.industry<>'[]')
    return p limit 3000 '''

    comm3 = '''MATCH p=(d_start:Domain)-[:r_request_jump|r_subdomain *0..1]-(d1:Domain)-[:r_request_jump|r_subdomain *0..1]-(d2:Domain)-[:r_request_jump|r_subdomain *0..1]-(d_end:Domain)-[:r_dns_a]->(ip:IP) where d_start.id='Domain_7a4f65efe0cd15aad555d4ceb3de510f9a96817b416ae89e20dbe82ea3fc4bb6'
    OPTIONAL MATCH p1=(cert_start:Cert)-[:r_cert_chain*0..1]-(cert_end:Cert)<-[c2d:r_cert]-(d_start:Domain)
    where (cert_end.name<>'321294f7c6') and (d1.industry<>'[]' or d2.industry<>'[]' or d_start.industry<>'[]' or d_end.industry<>'[]')  
    return p,p1 limit 3000'''

    comm4 = '''MATCH p=(ip:IP{id:'IP_6acab66245718783adbe872ed865728ac828f4666834336e41ac3878e8cf1836'})<-[:r_dns_a]-(d_start:Domain)-[:r_request_jump|r_subdomain *0..4]-(d_end:Domain)-[d2c:r_cert]->(cert_start:Cert)-[:r_cert_chain*0..2]-(cert_end:Cert)--(d_others:Domain)-[:r_request_jump|r_subdomain *0..4]-(d_others_end:Domain)   
   where (cert_end.name<>'fe794a69ea') and (d_end.industry<>'[]')
   return p limit 3000 '''
   # comm4可以得到一个团伙 暂定为团伙7 问题在于没有info

    comm5 = '''
    MATCH p=(ip:IP{id:'IP_4857596c90a5057f7c9ebe1fc710d59ce71e10b227e566d51fefa96e343d4ad6'})<-[:r_dns_a]-(d_start:Domain)-[:r_request_jump|r_subdomain *0..3]-(d_end:Domain)-[d2c:r_cert|r_whois_name|r_whois_phone|r_whois_email]->(cert_start)-[:r_cert_chain*0..1]-(cert_end)--(d_others:Domain)-[:r_request_jump|r_subdomain *0..3]-(d_others_end:Domain),p1=(d_others_end)--(iporcert:Cert),p2=(d_others_end)--(orcert:IP)

where  (d_end.industry<>'[]' or d_start.industry<>'[]') and (d_others.industry<>'[]' or d_others_end.industry<>'[]')

return p,p1,p2 limit 10000'''

    comm6 = '''
    MATCH p=(cert_start:Cert)-[:r_cert_chain*0..1]-(cert_end:Cert)<-[c2d:r_cert]-(d_start:Domain)-[:r_request_jump|r_subdomain *0..1]-(d1:Domain)-[:r_request_jump|r_subdomain *0..1]-(d2:Domain)-[:r_request_jump|r_subdomain *0..1]-(d_end:Domain)-[:r_dns_a]->(ip:IP),p2=(ip)<-[:r_dns_a*0..1]-(d_end_right)-[:r_request_jump|r_subdomain *0..1]-(d2_right:Domain)-[:r_request_jump|r_subdomain *0..1]-(d1_right:Domain)-[:r_request_jump|r_subdomain *0..1]-(d_start_right:Domain)-->(cert_start_right:Cert)-[:r_cert_chain*0..1]-(cert_end_right:Cert)
    
    where (cert_start.id='Cert_fe794a69eacd63b21245bf4eda826222fc6c5862bebf77aa05459cb308cfd063') and (cert_end.name<>'321294f7c6') and (d1.industry<>'[]' or d2.industry<>'[]' or d_start.industry<>'[]' or d_end.industry<>'[]')  and (d1_right.industry<>'[]' or d2_right.industry<>'[]' or d_start_right.industry<>'[]' or d_end_right.industry<>'[]') and d_start.industry contains 'G'
    
    return p,p2 limit 5000'''

    comm8 = '''
    MATCH p=(ip:IP{id:'IP_3d2d6d57e02d1af283c148f588dc1ceeffc1d7798160ded07e1943477d6028b4'})<-[:r_dns_a]-(d_start:Domain)-[:r_request_jump|r_subdomain *0..4]-(d_end:Domain)-[d2c:r_cert]->(cert_start:Cert)-[:r_cert_chain*0..2]-(cert_end:Cert)--(d_others:Domain)-[:r_request_jump|r_subdomain *0..4]-(d_others_end:Domain)
where (cert_end.name<>'fe794a69ea') and (d_end.industry<>'[]')
with p, d_others_end 
match p2=(d_others_end)-->(someip:IP)--(somed:Domain)-[:r_request_jump|r_subdomain*0..2]-(dsome:Domain) 
where somed.industry<>'[]'

        return p,p2 limit 3000'''

    comm99 = '''
    MATCH p=(ip:IP{id:'IP_44e642e648fa555970bfd01596dc1b67e65b357e469479b4105fed2758339462'})<-[:r_dns_a]-(d_start:Domain)-[:r_request_jump|r_subdomain *0..4]-(d_end:Domain)-[d2c:r_cert|r_whois_name]->(cert_start)-[*0..1]-(cert_end)--(d_others:Domain)-[:r_request_jump|r_subdomain *0..4]-(d_others_end:Domain)
where (cert_end.name<>'fe794a69ea') and (d_end.industry<>'[]')
with p, d_others_end 
match p2=(d_others_end)-->(someip:IP)--(somed:Domain)-[:r_request_jump|r_subdomain*0..2]-(dsome:Domain) 
where somed.industry<>'[]'

        return p,p2 limit 3000'''

    comm9 = '''
    match p=(name:Whois_Name{id:'Whois_Name_fda9375865e67510b7a99ec277f14ff7bbedd070574a7ab7c2afe76782f9eb4d'})--(d_start:Domain)-[:r_request_jump|r_subdomain*0..3]-(d_end:Domain)--(ip:IP)where (d_start.industry<>'[]' or d_end.industry<>'[]') with ip, p optional match p2=(ip)--(d1:Domain)-[:r_request_jump|r_subdomain*0..1]-(d2:Domain)  where d1.industry<>'[]' or d2.industry<>'[]' with p,p2,d2 optional match p3=(d2)-[:r_request_jump|r_subdomain*0..1]-(d3:Domain)--(c:Cert) where (d2.industry<>'[]' or d3.industry<>'[]')  return p,p2,p3 limit 3000'''

    comm10 = '''MATCH p=(ip:IP{id:'IP_91e73ed138ba96ccf7120c2bb384bf8f12a1e37da9f1ab819b96e3ececeae7f1'})<-[:r_dns_a]-(d_start:Domain)-[:r_request_jump|r_subdomain *0..4]-(d_end:Domain)-[d2c:r_cert|r_whois_name|r_whois_phone|r_whois_email]->(cert_start)-[*0..1]-(cert_end)--(d_others:Domain)-[:r_request_jump|r_subdomain *0..4]-(d_others_end:Domain)
where (cert_end.name<>'fe794a69ea') and (d_end.industry<>'[]')
with p, d_others_end 
match p2=(d_others_end)-->(someip:IP)--(somed:Domain)-[:r_request_jump|r_subdomain*0..3]-(dsome:Domain) 
where somed.industry<>'[]'

        
        return p,p2 limit 3000'''

    ans = run_comm(comm9)

    ans_with_list_set = list(set(ans))

    print(len(ans))

    print(len(ans_with_list_set))

    check_chongfulv(ans_with_list_set)

    filename = 'node_temp.json'
    with open('json_hu/%s'%filename, 'w') as f:
        json.dump(ans_with_list_set, f)

