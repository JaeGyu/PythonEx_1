class Mody:
    def __init__(self, name = "test"):
        self.__name = name
        self.age = 23
        self._addr = "suwon"
        self.__phone = "010"
    
    def get_name(self):
        return self.__name

    def get_phone(self):
        return self.__phone
    
    def mody_main(self):
        mo = Mody("alice")
        print(mo.get_name())


if __name__ == "__main__":
    mm = Mody()
    mm.mody_main()