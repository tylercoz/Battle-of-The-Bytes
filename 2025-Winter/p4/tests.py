import unittest
from p4 import palindrome #type: ignore

class TestAdd(unittest.TestCase):
  def test_zero(self):
    self.assertEqual(palindrome(0), 0)

  def test_111(self):
    self.assertEqual(palindrome(111), True)

  def test_121(self):
    self.assertEqual(palindrome(121), True)

  def test_12221(self):
    self.assertEqual(palindrome(12221), True)

  def test_12521(self):
    self.assertEqual(palindrome(12521), True)

  def test_3765673(self):
    self.assertEqual(palindrome(3765673), True)

  def test_112(self):
    self.assertEqual(palindrome(112), False)

  def test_3565673(self):
    self.assertEqual(palindrome(3565673), False)

  def test_neg_121(self):
    self.assertEqual(palindrome(-121), False)

  def test_neg_122(self):
    self.assertEqual(palindrome(-122), False)
if __name__ == '__main__':
  unittest.main()
