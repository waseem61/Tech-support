import requests
import csv
import  json
import time
headers={'Content-type':'application/json', 'Accept':'application/json', 'x-csrftoken': 'UYKOQLgEJGgHq2XIhWbOeGMQ94PiMv37'}

cookies = {
        'session': '122890d62fbdd59b5e972485',
        'csrftoken': 'UYKOQLgEJGgHq2XIhWbOeGMQ94PiMv37'
    }

with open('waseem.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    next(reader)
    for row in reader:
        print(row)
        candidate_ids = row[0]
        application_id = row[1]
        brands_id = row[2]
        data = '{"tag_ids":[39683],"candidate_ids":['+str(candidate_ids)+'],"source":"APPLIED","application_id":'+str(application_id)+'}'
        response = requests.post('https://talent-pool-api.harri.com/api/v1/brands/'+str(brands_id)+'/candidates/tags/assign',headers=headers, cookies=cookies, data=data)
        print  response.status_code