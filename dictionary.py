students = [
    {"name": "Gift", "phone": "0712345678", "age": 20, "location": "Nairobi", "DOB": "2006-03-15"},
    {"name": "Amina", "phone": "0723456789", "age": 22, "location": "Mombasa", "DOB": "2004-07-02"},
    {"name": "Daniel", "phone": "0734567890", "age": 19, "location": "Kisumu", "DOB": "2007-01-20"},
    {"name": "Rophus", "phone": "0745678901", "age": 25, "location": "Nakuru", "DOB": "2001-11-05"},
    {"name": "Grace", "phone": "0756789012", "age": 21, "location": "Eldoret", "DOB": "2005-09-30"},
]

print(students)

students.append({"name": "Peter", "phone": "0767890123", "age": 23, "location": "Thika", "DOB": "2003-05-12"})
students[0]["age"] = 21
students.pop(2)

print(students)