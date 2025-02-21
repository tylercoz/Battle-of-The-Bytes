import unittest
from p6 import letter_combinations #type: ignore

class TestLetterCombinations(unittest.TestCase):
  def test_one(self):
    digits = "23"
    self.assertEqual(
      letter_combinations(digits),
      ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    )

  def test_two(self):
    digits = ""
    self.assertEqual(
      letter_combinations(digits),
      []
    )

  def test_three(self):
    digits = "2"
    self.assertEqual(
      letter_combinations(digits),
      ["a","b","c"]
    )

  def test_four(self):
    digits = "4523"
    self.assertEqual(
      sorted(letter_combinations(digits)),
      ['gjad', 'gjae', 'gjaf', 'gjbd', 'gjbe', 'gjbf', 'gjcd', 'gjce', 'gjcf', 'gkad', 'gkae', 'gkaf', 'gkbd', 'gkbe', 'gkbf', 'gkcd', 'gkce', 'gkcf', 'glad', 'glae', 'glaf', 'glbd', 'glbe', 'glbf', 'glcd', 'glce', 'glcf', 'hjad', 'hjae', 'hjaf', 'hjbd', 'hjbe', 'hjbf', 'hjcd', 'hjce', 'hjcf', 'hkad', 'hkae', 'hkaf', 'hkbd', 'hkbe', 'hkbf', 'hkcd', 'hkce', 'hkcf', 'hlad', 'hlae', 'hlaf', 'hlbd', 'hlbe', 'hlbf', 'hlcd', 'hlce', 'hlcf', 'ijad', 'ijae', 'ijaf', 'ijbd', 'ijbe', 'ijbf', 'ijcd', 'ijce', 'ijcf', 'ikad', 'ikae', 'ikaf', 'ikbd', 'ikbe', 'ikbf', 'ikcd', 'ikce', 'ikcf', 'ilad', 'ilae', 'ilaf', 'ilbd', 'ilbe', 'ilbf', 'ilcd', 'ilce', 'ilcf']
    )

  def test_five(self):
    digits = "8765"
    self.assertEqual(
      sorted(letter_combinations(digits)),
      ['tpmj', 'tpmk', 'tpml', 'tpnj', 'tpnk', 'tpnl', 'tpoj', 'tpok', 'tpol', 'tqmj', 'tqmk', 'tqml', 'tqnj', 'tqnk', 'tqnl', 'tqoj', 'tqok', 'tqol', 'trmj', 'trmk', 'trml', 'trnj', 'trnk', 'trnl', 'troj', 'trok', 'trol', 'tsmj', 'tsmk', 'tsml', 'tsnj', 'tsnk', 'tsnl', 'tsoj', 'tsok', 'tsol', 'upmj', 'upmk', 'upml', 'upnj', 'upnk', 'upnl', 'upoj', 'upok', 'upol', 'uqmj', 'uqmk', 'uqml', 'uqnj', 'uqnk', 'uqnl', 'uqoj', 'uqok', 'uqol', 'urmj', 'urmk', 'urml', 'urnj', 'urnk', 'urnl', 'uroj', 'urok', 'urol', 'usmj', 'usmk', 'usml', 'usnj', 'usnk', 'usnl', 'usoj', 'usok', 'usol', 'vpmj', 'vpmk', 'vpml', 'vpnj', 'vpnk', 'vpnl', 'vpoj', 'vpok', 'vpol', 'vqmj', 'vqmk', 'vqml', 'vqnj', 'vqnk', 'vqnl', 'vqoj', 'vqok', 'vqol', 'vrmj', 'vrmk', 'vrml', 'vrnj', 'vrnk', 'vrnl', 'vroj', 'vrok', 'vrol', 'vsmj', 'vsmk', 'vsml', 'vsnj', 'vsnk', 'vsnl', 'vsoj', 'vsok', 'vsol']
    )


if __name__ == '__main__':
  unittest.main()
