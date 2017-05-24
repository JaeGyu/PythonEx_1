import unittest as ut

class Portfolio(object):
    def __init__(self):
        self.stocks = []

    def buy(self, name, shares, price):
        self.stocks.append([name,shares,price])
    
    def cost(self):
        amt = 0.0

        for name, shares, price in self.stocks:
            amt += shares * price
        return amt

class PortfolioTest(ut.TestCase):
    def test_google(self):
        p = Portfolio()
        p.buy("google", 100, 176.48)
        self.assertEqual(17648.0, p.cost())

    def test_google_yahoo(self):
        p = Portfolio()
        p.buy("google", 100, 176.48)
        p.buy("yahoo", 100, 36.15)
        self.assertEqual(21263.0, p.cost())

class NumberTest(ut.TestCase):

    # def test_even(self):
    #     for i in range(0,6):
    #         self.assertEqual(i % 2 , 0)

    def test_even_with_subtest(self):
        for i in range(0,6):
            with self.subTest(i=i):
                self.assertEqual(i % 2, 0)



if __name__ == "__main__":
    # p = Portfolio()
    # print(p.cost())
    
    # assert p.cost() == 0.0
    # p.buy('Google', 100, 176.48)
    # print(p.cost())
    # p.buy('Yahoo', 100, 36.15)
    # print(p.cost())
    ut.main()