import unittest


def add(a,b):
    return a+b

def sub(a,b):
    return a-b


class unit_test(unittest.TestCase):

    def test_add(self):
        self.assertEqual(3, add(1,2))
    
    def test_sub(self):
        self.assertEqual(2,sub(4,2))


if __name__ == "__main__":
    unittest.main()
