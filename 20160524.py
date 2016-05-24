#_*_ coding: utf-8 _*_

def fun(*args):
	print(args);
	print(type(args))
	print(len(args))

fun('a','b')

#패킹된 열거형 자료를 언패킹 해서 사용한다.

print(list(range(3,6)))

args=[3,6]

#함수를 호출 할때 사용하는 *는 args를 언패킹 하라는 소리다.
print(list(range(*args)))


