# Car Project
title_list=[]

def get_titles():
	with open ("autotitles.txt", "r") as f:
		titles =f.readlines()
	titles = [title.split() for title in titles]
	for row in titles:
		try:
			dummy = int(row[0][:-1])
			title_list.append(row[1][:-1])
		except:
			pass
	return title_list

def get_data():
	with open("autorawdata.txt", "r") as f:
		lines = f.readlines()
	#for index in lines
	return lines

title_list = get_titles()
lines = get_data()

for element in title_list:
	print(element)

#for element in lines[:10]:
#	print(element)