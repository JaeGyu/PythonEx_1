#_*_ coding: utf-8 _*_
#Python3 실습

print("hh")

def sum(a,b):
	return (a+b)

print(sum(4,5))
print(sum("han"," jaegyu"))


def no_return():
	print("안녕하세요")
	return

print(no_return())
print(type(None))

a=None
print(a)
print(range(10))
print(list(range(10)))

def daily_sleeping_hours(hours=None):
	if hours == None:
		print("인자 값 세팅을 잊으셨군요..")
	return hours


print(daily_sleeping_hours(6))
print(daily_sleeping_hours())


def introduce_my_car(manufacturer, seats=4, type='sedan'):
	print("내 차는", manufacturer, "의", seats, "인승", type,"이다.")

introduce_my_car("ㄹㄹ")

def fun(a='1',b='2',c='3'):
	print(a,b,c)

fun(1)
fun(1,1,1)
fun(10,20)
fun(10,c="30")
fun(a='10')

def introduce_your_family(name, *family_names, **family_info):
	print("제 이름은", name," 입니다.")
	print("제 가족들의 이름은 아래와 같아요. ")
	print("-"*40)	
	for name in family_names:
		print(name)
	print("-"*40)	
	for key in family_info.keys():
		print(key, ":", family_info[key])

introduce_your_family("홍길동","홍길비","홍길수", 집="용인", 가훈="행복하게  살자!")

def ff(**n):
	print(n)

ff(a='aa',b='bb')

def concat(*args, sep='/'):
	return sep.join(args)

print(concat("a","b","c"))

print(concat("a","b","c",sep="."))






