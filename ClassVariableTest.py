class A:
    store = [] #[]<- 이 리스트 객체의 주소를 모든 인스턴스가 공유한다.

    def __init__(self):
        pass
    
if __name__ == "__main__":
    a = A() 
    b = A() 
    a.store.append("a")

    #만약 여기서 a의 store를 재정의 해준다면 그건 당연히 b에 영향을 안미친다. 그냥 a안에있는 store의 참조주소가 재정의 하는 객체의 주소로 
    #변경되는 것 뿐이다.

    print(b.store)