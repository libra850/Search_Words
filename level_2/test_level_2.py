import unittest
import search

class TestCheck_keyword(unittest.TestCase):

    def test_txt_load(self):
        expected = "test"
        actual = search.load(value)
        self.assertEqual(expected, actual)


    

if __name__ == '__main__':
    unittest.main()