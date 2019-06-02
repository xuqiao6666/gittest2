import  requests

r=requests.get("https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&page_limit=50&page_start=0")

result = r.json()

list = result["subjects"]
list1 =[]

#for i in (0,len(list)-1) :
#    list1[i] =list[i]["id"]
    #print(list1)

for l in list:
    list1.append(l["id"])
    print(list1)

for m in list1:
    r1 = requests.get("https://movie.douban.com/subject/"+str(m)+"/?tag=%E7%83%AD%E9%97%A8&from=gaia_video")
print(r1.status_code)