
a = "python"

print(a*2)

try:
    print(a[-10])
except IndexError as e:
    print("인덱스 범위를 초과 했습니다.")
    print(e)

print(a[0:4])
print(a[1:-2])

# -10은 hi뒤로 10칸
print("%-10sjane." % "hi")

b = "Python is best choice."
print(b.find("b"))
print(b.find("B"))
try:
    print(b.index("B"))
except ValueError as e:
    print(e)


c = "hi"
print(c.upper())

a = "   hi"
print("kk",a.lstrip())

a = "  hi  "
print(a.strip())



