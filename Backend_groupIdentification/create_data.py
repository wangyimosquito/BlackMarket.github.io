import pandas as pd
import numpy as np
import json

#把node.csv和link.csv和这个文件放在同一个文件夹下

node_data_path = 'Node.csv'
link_data_path = 'Link.csv'

node_json_path = './new_node/node1.json'
# link_json_path = './group5/link5.json'

new_node_json_path = './new_node/new_node1.json'

class readData:
	def __init__(self):
		self.node_data = pd.read_csv(node_data_path)
		self.link_data = pd.read_csv(link_data_path)
		self.node_data = np.array(self.node_data)
		self.link_data = np.array(self.link_data)
	
	def node_to_dic(self):
		node_json = {}
		new_node_json = {}
		for i in self.node_data:
			#需要将字符串识别为数组
			industry = self.parse_industry(i[3])
			node_json[i[0]] = {'name': i[1], 'type': i[2], 'industry': i[3]}
			new_node_json[i[0]] = {'name': i[1], 'type': i[2], 'industry': industry}
		dict_json = json.dumps(node_json)
		with open(node_json_path,'w+') as file:
			file.write(dict_json)
		dict_json = json.dumps(new_node_json)
		with open(new_node_json_path,'w+') as file:
			file.write(dict_json)
	
	def parse_industry(self, str):
		industry = []
		for c in str:
			if c == 'A':
				industry.append('A')
			if c == 'B':
				industry.append('B')
			if c == 'C':
				industry.append('C')
			if c == 'D':
				industry.append('D')
			if c == 'E':
				industry.append('E')
			if c == 'F':
				industry.append('F')
			if c == 'G':
				industry.append('G')
			if c == 'H':
				industry.append('H')
			if c == 'I':
				industry.append('I')
		return industry


if(__name__ == '__main__'):
	test = readData()
	test.node_to_dic()