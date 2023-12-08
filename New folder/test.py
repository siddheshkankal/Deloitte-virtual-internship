
import json

f = open('D:/deloitte/Newfolder/data1.json',encoding="utf8")
  
# returns JSON object as 
# a dictionary
data = json.load(f)

print(data)
# Iterating through the json
# list
# for i in data['emp_details']:
#     print(i)
  
# Closing file
# f.close()