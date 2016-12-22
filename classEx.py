class Bread:
    #meterial = "팥"
    def __init__(self,meterial):
        self.meterial = meterial

    def set_meterial(self,value):
        self.meterial = value
    
    def get_meterial(self):
        return self.meterial

def main():
    b = Bread("설탕")
    print(b.get_meterial())

    b.set_meterial("슈크림")
    print(b.get_meterial())

if __name__ == "__main__":
    main()