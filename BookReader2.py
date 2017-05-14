class BookReader:
    __country = "south Korea" #앞에 __을 붙이면 파이썬이 _클래스명__변수명 으로 변수를 변경을 한다 그럼 외부에서 정의된 변수명으로는 접근이 안되는 효과를 볼 수 있다. 


if __name__ == "__main__":
    print(dir(BookReader))
    print("-"*80)
    BookReader._BookReader__country = "USA"
    print(BookReader._BookReader__country)