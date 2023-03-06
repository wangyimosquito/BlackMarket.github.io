import pandas as pd
import numpy as np
import json
import random

node_data_path = 'Node.csv'
link_data_path = 'Link.csv'

node_json_path = 'new_node.json'
link_json_path = 'link.json'

IP_industry_json_path = 'IP_Industry.json'
Cert_industry_json_path = 'Cert_Industry.json'

Link_type_json_path = 'link_type.json'
Connect_json_path = 'connect.json'

class task2:
	def __init__(self):
		self.node_data = pd.read_csv(node_data_path)
		self.link_data = pd.read_csv(link_data_path)
		self.node_data = np.array(self.node_data)
		self.link_data = np.array(self.link_data)

		with open(node_json_path, "r") as json_file:
			self.node_json = json.load(json_file)
		with open(link_json_path, "r") as json_file:
			self.link_json = json.load(json_file)
		with open(Link_type_json_path, "r") as json_file:
			self.link_type_json = json.load(json_file)
		with open(Connect_json_path, "r") as json_file:
			self.connect_json = json.load(json_file)
	
	def gen_link(self, group_name):
		node_path = './task2/subGraph/node'+str(group_name)+'.json'
		save_path = './task2/subGraph/link'+str(group_name)+'.json'
		with open(node_path, "r") as json_file:
			node = json.load(json_file)
		
		node_set = set(node)
		link = set()
		for each_node in node:
			for target_node in self.link_json[each_node]:
				if target_node in node_set and ((each_node, target_node) not in link):
					link.add((each_node, target_node))
		
		print("-----------------------------basic info-------------------------------------")
		print("group"+str(group_name)+' node: ', len(node))
		print("group"+str(group_name)+' link: ', len(link))
		dict_json = json.dumps(list(link))
		with open(save_path,'w+') as file:
			file.write(dict_json)

	def gen_core_asset(self, group_name):
		print("-----------------------------core asset-------------------------------------")
		with open("./task2/subGraph/node"+str(group_name)+".json", "r") as json_file:
			ori_node = json.load(json_file)
		#首先找到其核心资产
		core_node = []
		totol_candidate = []
		#如果一个节点的连边50%以上都是较弱连边，则其不是核心节点
		for each_node in ori_node:
			if self.node_json[each_node]['type'] == 'IP' or self.node_json[each_node]['type'] == 'Cert':
				totol_candidate.append(each_node)
				#对于IP节点统计其连边类型为弱的数量
				if self.node_json[each_node]['type'] == 'IP':
					count_weak = 0
					total_link = len(self.connect_json[each_node])
					#print("node[",each_node,"] total link num: ", total_link)
					for each_target in self.connect_json[each_node]:
						if each_node+each_target in self.link_type_json:
							if(self.link_type_json[each_node+each_target]) == 'r_asn' or (self.link_type_json[each_node+each_target]) == 'r_cidr':
								count_weak += 1
						else:
							if(self.link_type_json[each_target+ each_node]) == 'r_asn' or (self.link_type_json[each_target+each_node]) == 'r_cidr':
								count_weak += 1
					if count_weak/total_link < 0.5:
						core_node.append(each_node)
				#对于证书节点，肯定不存在弱边
				else:
					total_link = len(self.connect_json[each_node])
					#print("node[",each_node,"] total link num: ", total_link)
					core_node.append(each_node)

		print("delete weak most candidate: ", len(totol_candidate)," -> ",len(core_node))
		#如果一个域名连接了两个或者两个以上的IP，则这个IP不是核心节点
		delete_core = []
		for core1 in core_node:
			if self.node_json[core1]['type'] == 'IP':
				for core2 in core_node:
					if self.node_json[core2]['type'] == 'IP':
						if core1 == core2:
							pass
						else:
							#检查是否存在域名节点同时指向这两个节点
							for each_node in ori_node:
								if self.node_json[each_node]['type'] == 'Domain':
									if each_node+core1 in self.link_type_json and each_node+core2 in self.link_type_json:
										delete_core.append(core1)
										delete_core.append(core2)
										break
		tmp = core_node
		core_node = []
		for each_node in tmp:
			if not(each_node in set(delete_core)):
				core_node.append(each_node)
		print("delete distribute IP: ", len(tmp),"->", len(core_node))
		
		dict_json = json.dumps(core_node)
		with open("./task2/core_asset/node"+str(group_name)+".json",'w+') as file:
			file.write(dict_json)

	def gen_member_info(self, group_name):
		print("-----------------------------member info------------------------------------")
		node_path = "./task2/subGraph/node"+str(group_name)+".json"
		save_path = './task2/group_member_info/group_info'+str(group_name)+'.json'
		
		with open(node_path, "r") as json_file:
			node = json.load(json_file)
		
		member_info_list  = []
		for each_node in node:
			if(self.node_json[each_node]['type'] == 'Whois_Name' or self.node_json[each_node]['type'] == 'Whois_Phone' or self.node_json[each_node]['type'] == 'Whois_Email'):
				member_info_list.append([each_node,self.node_json[each_node]['name']])
		
		dict_json = json.dumps(member_info_list)
		print("group"+str(group_name)+"info num: ", len(member_info_list))
		with open(save_path,'w+') as file:
			file.write(dict_json)
	
	def gen_industry_statistic(self, group_name):
		print("-----------------------------industry info----------------------------------")
		node_path =  "./task2/subGraph/node"+str(group_name)+".json"
		
		with open(node_path, "r") as json_file:
			node = json.load(json_file)
		
		industry_count = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E':0, 'F':0, 'G':0, 'H': 0, 'I':0 }
		for each_node in node:
			if len(self.node_json[each_node]['industry'])!=0:
				for each_industry in self.node_json[each_node]['industry']:
					old = industry_count[each_industry]
					old += 1
					industry_count[each_industry] = old
		print(industry_count)

	def gen_type_statistic(self, group_name):
		print("-----------------------------type info--------------------------------------")
		node_path = "./task2/subGraph/node"+str(group_name)+".json"
		with open(node_path, "r") as json_file:
			node = json.load(json_file)
	
		domain_num = 0
		IP_num = 0
		Cert_num = 0
		Whois_Name_num = 0
		Whois_Phone_num = 0
		Whois_Email_num = 0
		IP_C_num= 0
		ASN_num = 0

		for each_node in node:
			if self.node_json[each_node]['type'] == "Domain":
				domain_num += 1
			elif self.node_json[each_node]['type'] == "IP":
				IP_num += 1
			elif self.node_json[each_node]['type'] == "Cert":
				Cert_num += 1
			elif self.node_json[each_node]['type'] == "Whois_Name":
				Whois_Name_num += 1
			elif self.node_json[each_node]['type'] == "Whois_Phone":
				Whois_Phone_num += 1
			elif self.node_json[each_node]['type'] == "Whois_Email":
				Whois_Email_num += 1
			elif self.node_json[each_node]['type'] == "IP_C":
				IP_C_num += 1
			elif self.node_json[each_node]['type'] == "ASN":
				ASN_num += 1

		print("d: ", domain_num)
		print("IP: ", IP_num)
		print("Cert: ", Cert_num)
		print("Whois Name: ", Whois_Name_num)
		print("Whois Phone: ", Whois_Phone_num)
		print("Whois Email: ", Whois_Email_num)
		print("IP_C: ", IP_C_num)
		print("ASN: ", ASN_num)

	def search_member(self, group_name):
		node_path = "./task2/subGraph/node"+str(group_name)+".json"
		with open(node_path, "r") as json_file:
			node = json.load(json_file)

		member_info_node = []
		for each_node in node:
			for each_connect_node in self.connect_json[each_node]:
				if self.node_json[each_connect_node]['type'] == 'Whois_Name' or self.node_json[each_connect_node]['type'] == 'Whois_Phone' or self.node_json[each_connect_node]['type'] == 'Whois_Email':
					member_info_node.append(each_connect_node)
		print("group"+str(group_name)+"info node num: ", len(member_info_node))
		new_node = node + member_info_node
		new_node = list(set(new_node))

		dict_json = json.dumps(new_node)
		with open(node_path,'w+') as file:
			file.write(dict_json)
	
	def wrap_func(self, group):
		self.search_member(group)
		self.gen_link(group)
		self.gen_core_asset(group)
		self.gen_member_info(group)
		self.gen_industry_statistic(group)
		self.gen_type_statistic(group)

t = task2()
t.wrap_func(7)


