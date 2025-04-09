items=["mango","mango","orange","orange","banana","apple"]
count={}
for item in items:
    count[item]=count.get(item,0)+1
print(count)    

    