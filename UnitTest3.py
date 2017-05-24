import unittest as ut 


def add(x,y):
    return x+y

if __name__ == "__main__":
    ut.TestCase.assertEqual(3, add(1,2))