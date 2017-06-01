

class Person:
    name = "hhh"


def main():
    p = Person() 
    print(p.name)
    p.name = "han"
    print(p.name)

    p2 = Person() 
    print(p2.name)

    print("*" * 60)

    Person.name = "ka"
    print(p.name)
    print(p2.name)

if __name__ == "__main__":
    main()