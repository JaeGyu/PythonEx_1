import json

class Person():
    def __init__(self, name:str, age:int):
        self.name = name
        self.age = age

    def getName(self) -> str:
        return self.name

    def getAge(self) -> int:
        return self.age
    
    def __str__(self) -> str:
        return self.getName() + ":" + str(self.getAge())

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, ensure_ascii=False, sort_keys=True, indent=4)


if __name__ == "__main__":
    p = Person("앨리스", 24)
    print(p)

    print(p.toJSON())