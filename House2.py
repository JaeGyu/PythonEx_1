class House2(object):
    company = "Python Factory"

    def __init__(self, year, acreages, address, price):
        self.year = year
        self.acreages = acreages
        self.address = address
        self.price = price
    
    def show_company(self):
        print(House2.company)
    
    def change_price(self, rate):
        self.price = self.price * rate

    def show_info(self):
        print("""This house is built by {} in {},
        acreages : {},
        address  : {},
        price    : {}""".format(House2.company, self.year, self.acreages, self.address, self.price))


if __name__ == "__main__":
    house_A = House2(1999, 100, "seoul", 7777777)
    house_A.show_info()
    house_A.__class__.show_info(house_A)
    house_A.__init__(10,10,10,10)
    house_A.show_info()