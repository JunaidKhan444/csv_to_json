import os
import json
import csv
path_csv_files = '/home/junaid/Desktop/task/csvs'
path_json = '/home/junaid/Desktop/task/result'
fileList = os.listdir(path_csv_files)

for filename in fileList:
    with open(os.path.join(path_csv_files, filename), 'r') as f1:
       l1 ={}
       l2 = {}

       data = {}
       first_key = ''
       r1 = csv.DictReader(f1)
       count = 0
       for r2 in r1:
           data[r2['condition']] = {"cui":r2['condition_cui'],
                                    "have_had":{},
                                    "looking_for":{}
                                    }
           first_key = str(r2['condition'])
           count += 1
           if (count == 2):
               break
       with open(os.path.join(path_csv_files, filename), 'r') as f2:
           reader = csv.DictReader(f2)
           for row in reader:
               if(row['label_bucket'] == 'have_had'):
                   l1[str(row['label'])]={
                        "cui":str(row['label_cui']),
                        "score":str(row['label_score']) ,
                        "label_semantic_types":str(row['label_semantic_types']) ,
                        "label_ncts_counts": str(row['label_ncts_count']),
                        "ncts": str(row['label_ncts'])
                }
               else:
                    l2[str(row['label'])]={
                        "cui":str(row['label_cui']),
                        "score":str(row['label_score']) ,
                        "label_semantic_types":str(row['label_semantic_types']) ,
                        "label_ncts_counts": str(row['label_ncts_count']),
                        "ncts": str(row['label_ncts'])
                                           }
       data[first_key]['have_had'] = l1
       data[first_key]['looking_for'] = l2
                
        #print(data)
       new_filename = filename.rstrip('.csv')
       with open(os.path.join(path_json,new_filename+'.json'),'w') as f2:
           f2.write(json.dumps(data,indent=4))