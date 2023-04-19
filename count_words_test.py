import unittest
from countwords import count_words
class TestCountLetters(unittest.TestCase):
    def test_simple(self):
        result = count_words('hola')
        self.assertEqual(result, {'hola': 1})

        def test_simple(self):
            result = count_words('hola')
            self.assertEqual(result, {'hola': 1})

    def test_complex(self):
        result = count_words('Hola como estas hola')
        self.assertEqual(
            result,
            {
                'hola': 2,

                'como': 1,

                'estas': 1,
            },
        )

if __name__ == '__main__':
    unittest.main()