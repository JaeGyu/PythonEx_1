
a = "python"

print(a*2)

try:
    print(a[-10])
except IndexError as e:
    print("인덱스 범위를 초과 했습니다.")
    print(e)

