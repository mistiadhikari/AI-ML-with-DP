# email= "hello@gmail.com"
# password= "hello123"
# if email== "hello@gmail.com":
#     if password== "hello123":
#      print("login successful")
logged_in= False
if not logged_in:
    print("please login")

for i in range(0,5):
    print(i)
for j in range(10,0,-2):
    print (j)

countries= ["japan","usa","nepal"]
for country in countries:
    print(country)

prediction_score= [77,99,23,67]
for score in prediction_score:
    if score>80:
        print(score,"good ")
    else:
        print(score,"not good")

email_list=[
    "market has discount",
    "free ticket of plane",
    "congrats, you won free watch"
]
for email in email_list:
    if "congrats" in email or "free"