import unittest as ut

def add(a,b):
    print("a+b")
    return a+b 

def print_star():
    star = "*\n**\n***"
    print(star)
    return star

class FuncTest(ut.TestCase):
    def setUp(self):
        print("set_up")

    def tearDown(self):
        print("end")

    def test_add(self):
        self.assertEqual(3,add(1,2))
    
    def test_print_star(self):
        star = "*\n**\n***"
        self.assertEqual(star,print_star())

if __name__ == "__main__":
    ut.main()