class BookReader:
    country = "South Korea"  #클래스 변수라 한다. 이는 클래스에 의해 생성된 모든 객체에서 같은 값을 조회할때 사용한다.
                             #클래스.클래스변수 = ~~~ <- 이렇게 하면 자바의 static 처럼 된다.
                             #다른 인스턴스에도 영향을 미친다.
                             #각 각의 인스턴스가 클래스 변수가 가지고 있는 객체참조 주소를 공유 한다. 

    def __init__(self, name):
        self.name = name
    
    def read_book(self):
        print(self.name + ' is reading Book!!')
    
class NameSpacePrint:
    def __init__(self, name):
        self.name = name
    
    def print_name(self):
        print(self.name)

if __name__ == "__main__":
    b = BookReader("alice")
    e = BookReader("peter")
    # b.read_book()
    # print(b.country)
    b.country = "hhhhhhh"
    # BookReader.country = "abc"
    print("b : ",b.country)
    print("e : ",e.country)

    d = BookReader("Bob")
    print(d.country)

    c = NameSpacePrint(__name__)
    c.print_name()