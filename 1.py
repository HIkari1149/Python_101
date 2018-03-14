import requests
import time
import pickle
import random
import os
token = "EAACEdEose0cBAH99r4kQoZCl27tww08L3dVujMrwKHK7HeWQQ0b6PEL4ZBiKhXYZCNcQGstvDI7gJtNyR5vQVWYLvhyZBBaEmwi1j09ckxnOpQ87aeVL4utthZAZCKqs98OKuWlQF58d4DvwL4A0u7VMndvOHikRfgFL6nm1ZCnYzg1GVB4zmvZByz6GNYXQ1CLi5V4ypyy6fQZDZD"
page_id="1220332944702810"
def req_facebook(req):
    r=requests.get("https://graph.facebook.com/v2.12/"+req,{'access_token':token})
    return r
r = req_facebook(page_id+"?fields=posts.limit(5)")
print(r.status_code)
res=r.json()["posts"]
data=[]
cnt=0
while(cnt<5):
    try:
       # time.sleep(random.randint(2,5))
       # print(res['data'])
        data.extend(res['data'])
        r=requests.get(res['paging']['next'])
        res=r.json()
        cnt+=1
    except:
        print("Done")
        break



file = open("data_1.txt","w+")
for t in data:
    file.write(str(t)+"\n")
file.close()








    
