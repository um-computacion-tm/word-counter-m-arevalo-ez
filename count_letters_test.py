import unittest
from count_letters import count_letters
class TestCountLetters(unittest.TestCase):

    def test_simple(self):
        result = count_letters('a')
        self.assertEqual(result, {'a': 1})

    def test_complex(self):
        result = count_letters('hola')
        self.assertEqual(
            result,
            {
                'h': 1,
                'o': 1,
                'l': 1,
                'a': 1,
            }
        )

    def test_super_complex(self):
        result = count_letters('hola chau')
        self.assertEqual(
            result,
            {
                'h': 2,
                'o': 1,
                'l': 1,
                'a': 2,
                ' ': 1,
                'c': 1,
                'u': 1,
            }
        )

    def test_super_complex2(self):
        result = count_letters('buenas buenas')
        self.assertEqual(
            result,
            {
                'b': 2,
                'u': 2,
                'e': 2,
                'n': 2,
                'a': 2,
                's': 2,
                ' ': 1,
            }
        )
        
if __name__ == '__main__':
    unittest.main()
