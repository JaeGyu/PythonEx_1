#_*_ coding: UTF-8 _*_

a =1

def func():
    print("h")

print(locals())
global_namespace = locals()
try:
    print("-" * 100)
    print(global_namespace["a"])
    print(global_namespace["func"])
    print(global_namespace["b"])
except KeyError:
    print("없습니다.")
