import unittest

class TestExample(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(1 + 1, 2)

    def test_dummy(self):
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()

