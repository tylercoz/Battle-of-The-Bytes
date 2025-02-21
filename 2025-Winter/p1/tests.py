import unittest
from p1 import add #type: ignore

class TestAdd(unittest.TestCase):
  def test_zero(self):
    self.assertEquals(add(0,0), 0)

  def test_positives(self):
    self.assertEquals(add(5,3), 8)

  def test_negatives(self):
    self.assertEquals(add(-5,-2), -7)
    self.assertEquals(add(-5,10), 5)
    self.assertEquals(add(-5,5), 0)

if __name__ == '__main__':
  unittest.main()
