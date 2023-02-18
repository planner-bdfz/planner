# -*- coding: utf-8 -*-
# -=- planner_strategy -=-

import csv
import os

p = os.path.dirname(__file__)

with open(p+'/../../temp/test1.csv','r') as csvfile:
    reader = csv.reader(csvfile)
    rows = [row for row in reader]
    for i in range (1,len(rows)):
         t = rows[i]
         for j in range(i+1,len(rows)):
              if rows[i][1]>rows[j][1]:
                 rows[i]=rows[j]
                 rows[j]=t
                 t=rows[i]
csvfile.close()

f = open('test1.csv', 'w', newline='')
writer = csv.writer(f)
for n in rows:
    print(n)
    writer.writerow(n)
f.close()