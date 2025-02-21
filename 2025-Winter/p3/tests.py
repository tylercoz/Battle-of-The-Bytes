import unittest
from p3 import fact #type: ignore

class TestFactorial(unittest.TestCase):
  def test_zero(self):
    self.assertEqual(fact(0), 1)

  def test_one(self):
    self.assertEqual(fact(1), 1)

  def test_three(self):
    self.assertEqual(fact(3), 6)

  def test_seven(self):
      self.assertEqual(fact(7), 5040)

if __name__ == '__main__':
  unittest.main()
