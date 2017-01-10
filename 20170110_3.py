a = [1,2,3,4,5]

it = iter(a)
try:
    print(it.__next__())
    print(it.__next__())
    print(it.__next__())
except StopIteration as e:
    print("더 이상 값이 없습니다.", e)