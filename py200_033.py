str1 = "나는 파이썬 프로그래머다"
str2 = 'I am python programmer'
str3 = '''I love
    Python.{} You love
Python too!
'''
str4 = """나는 파이썬을
    좋아합니다
"""

# " 와 ' 가 섞여 있을 경우 '''을 사용한다
str5 = '''
"나는" i am '입니다'
'''

print(str1)
print(str2)
print(str3.format("이부분은?"))
print(str4)
print(str5)

