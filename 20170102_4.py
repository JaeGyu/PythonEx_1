

a = 1

def func():
    b = 2
    print(locals())

func()

print("="*90)

for i in locals().keys():
    print(i)

def func2(c):
    print(locals())

print("="*90)
func2(2)