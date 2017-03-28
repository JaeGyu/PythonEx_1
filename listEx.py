

list = [1,2,3,4]

print(list[0])
print(list[-1])
print(list[:2])


i = 0

while i<10:
    print(i)
    i+=1
    
list = []

if not list:
    print("list is Empty")

list = [1]

if not list:
    print("list is Empty")
else:
    print("list is not Empty")

if list and True:
    print("list is not Empty")

list = [1,2,3]

print("Befor : ",list)
print("Pop : ",list.pop(0))
print("After : ",list)


list = [1,2,3,4]
print(list)
l1 = list[:int(len(list)/2)]
print(l1)

