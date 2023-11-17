import unittest
import tempature


class Testing(unittest.TestCase):
    def test_above_freezing(self):
        self.assertEqual(tempature.above_freezing(-1),False)

    def test_FtoC(self):
        self.assertEqual(tempature.FtoC(32),0)
        
    def test_CtoF(self):
        self.assertEqual(tempature.CtoF(0),32)

if __name__ == '__main__':
    unittest.main()