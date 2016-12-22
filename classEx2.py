class Human:
    name = "alice"
    def intro(self):
        print("제 이름은 %s 입니다." % self.name)

class Child(Human):
    def hello(self):
        print("저는 %s 2세 입니다." % self.name)


def main():
    h = Child()
    h.hello()

if __name__ == "__main__":
    main()
