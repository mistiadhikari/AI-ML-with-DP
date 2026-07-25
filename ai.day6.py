function in python
def greet(name):
    print(name)
    print("hello"+ name)

greet("misti")
greet("shreeya")

def add(a,b):#return keywordai
   return a+b
sum = add(1,8)
print(sum)

def student():
   return "misti",21, "bhairawaha"
name,age,location= student()#unpacking tuple
print (name, age, location)

def say_hello(name):
   print("hello"+ name)

say_hello("misti")

def multiple(x,y):
   print(x,y)
   print(x*y)
multiple(3,4)

def square(num):
   return num*num
result= square(2)
result(2)
result2= lambda num:num*num #lambda function
result2(2)

