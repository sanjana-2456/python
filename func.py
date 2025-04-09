# def printMyName(name):
#     print(name)
# printMyName("new name")
# printMyName("sanjana")

# def sum(a,b=12):
#     return a+b
# res=sum(10)
# print(res)
# sum(10,20)
# sum(10)
# def greet(name,message="hi"):
#     print(message +","+ name)
# greet("sanjana")   
# greet("sanjana","good morning")


# def sum_numbers(*parms):
#     print(sum(parms))
# sum_numbers(1,2,3,4)

# x=20
# def local_scope():
#    print(x)
count=0
def increment():
   global count
   count+= 1
increment() 
print(count)   
