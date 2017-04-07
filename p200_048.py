'''


mode        |  desc

r 또는 rt    | 텍스트 모드로 읽기
w 또는 wt    | 텍스트 모드로 쓰기
a 또는 at    | 텍스트 모드로 파일 마지막에 추가하기
rb          | 바이너리 모드로 읽기
wb          | 바이너리 모드로 쓰기
ab          | 바이너리 모드로 파일 마지막에 추가하기

'''

f = open("./py200_sample.txt", "w")

f.write("abcd")
f.close()

r = open("./py200_sample.txt", "r")

print("-" * 60)
print(r.readline())

r.close()
