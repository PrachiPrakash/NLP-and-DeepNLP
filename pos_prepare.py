import os

out_file = open(r'./output.txt','w+')

files = os.listdir(r"/Users/prakash/Thesis/datasets/brown_subset_news")
for file in files:
	out_file.write(open(r'../datasets/brown_subset_news/'+file,'r').read())

out_file.close()