import os

path_dir = 'toProcess/'

file_list = os.listdir(path_dir)
print(file_list)

f = open("tpslist.txt",'w')
for name in file_list:
	newname = name[:-5] + '1' + name[-4:]
	print(newname)
	f.write(name+'\n')
f.close()