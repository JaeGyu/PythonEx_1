# students = []
# students.append({"std_id": 1, "name":"alice"})
# students.append({"std_id": 2, "name":"bob"})
# students.append({"std_id": 3, "name":"peter"})

# for i in students:
#     print(i)

# find_list = [i for i in students if i["std_id"] == 2]
# print(find_list)


students = []
students.append({"std_id" : 2017020001, "name" : "Alice"})
students.append({"std_id" : 2017020002, "name" : "Peter"})
# find_list = [i for i in students if i["std_id"] == 2017020002]
find_list = [student for student in students if student["std_id"] ==  2017020002]
print(find_list)