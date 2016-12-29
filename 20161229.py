class Car:
    def set_name(self,name):
        self.name = name
    
    def get_name(self):
        return self.name
    
    def __set_year(self,year):
        self.year = year
    
    def __get_year(self):
        return self.year
    
    def _set_door_cnt(self,cnt):
        self.door_cnt = cnt
    
    def _get_door_cnt(self):
        return self.door_cnt


class HasPrivate:
    def __init__(self):
        self.public = "PUBLIC"
        self.__private = "PRIVATE"
        self._protected = "PROTECTED"

    def print_test(self):
        print(self.public)
        print(self.__private)
        print(self._protected)


def main():
    c = Car()
    c.set_name("아반테")

    print(c.get_name())

    obj = HasPrivate()
    obj.print_test()
    print(obj.public)
    print(obj._protected)
    print(obj.__private)


if __name__ == "__main__":
    main()




    