import json
import csv
import re
from pprint import pprint
import fasttext
import timeit

start = timeit.default_timer()
data=[]

# with open(file_name, "r") as data_file:
#     print(type(data_file))
    # for i in data_file:
    #     for j in i:
    #         for k in j:
    #             data.append(json.loads(data_file))
jprofiles=[]
data = open('./0006.jl', 'r').read()
jprofiles= data.split("\n")

# print(len(jprofiles))

profiles=[]
for i in jprofiles:
    profiles.append(json.loads(i))
# print(len(profiles))

p = []
#h = {}
for i in profiles:
    #p.append(i.get('experience', 'Missing: key_name'))
    if 'experience' in i:
        #print(i['experience'])
        for t in i['experience']:
            h= {}
            if 'title' in t:
                #h[1]= t['title']
               # h.keys('title')
                #print(t['title'])
                if 'description' in t:
                    h[t['title']]=t['description']
                #print(t['description'])
                    h[t['title']] = re.sub('[^a-zA-Z_ ]', "", h[t['title']])
                p.append(h)
# for i in p:
#     print(i)

#print(p)


with open('mycsvfile.csv', 'w') as f:  # Just use 'w' mode in 3.x

    w = csv.writer(f)
    for i in p:
        w.writerows(i.items())



model = fasttext.cbow('mycsvfile.csv', 'model')
print(model.words)
print(model['king'])
stop = timeit.default_timer()

print(stop-start)
