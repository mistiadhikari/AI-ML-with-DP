
#1 Answer:
print("Welcome to DPLMS Student Registration System")

#2 Answer:
courses= [" Python with AI/ML", "JavaScript", "Flutter","MERN Stack"]

#3 Answer: 
for course in courses:
    print(course)

#4 Answer:
name= input("Enter your name:")
email= input("Enter your email:")
age= int(input("Enter your age:"))
selected_course= (input("Enter Selected Courses:"))

#5 Answer:
Student = {
    "Name": name,
    "Email": email,
    "Age": age,
    "Selected_Course": selected_course
}
#6&7 Answer:
if selected_course in courses:
    print("registration successful!")
else:
    print("course not available")

#8 Answer:
print("\n Student Registration Details")
print("Name:",Student["Name"])
print("Email:",Student["Email"])
print("Age:",Student["Age"])
print("Selected Course:",Student["Selected_Course"])
