import unittest
from countwords import count_words
class TestCountLetters(unittest.TestCase):

    def test_simple(self):
        result = count_words('hola')
        self.assertEqual(result, {'hola': 1})

    def test_complejo(self):
        result = count_words('Hola como estas hola')
        self.assertEqual(
            result,
            {
                'hola': 2,

                'como': 1,

                'estas': 1,
            },
        )

    def test_mascomplejo(self):
        result = count_words('Hola profesor hola profesor')
        self.assertEqual(
            result,
            {
                'hola': 2,

                'profesor': 2,
            },
        )

    def test_muchomascomplejo(self):
        result = count_words('Pablito clavo un clavito que clavito clavo pablito')
        self.assertEqual(
            result,
            {
                'pablito': 2,

                'clavo': 2,

                'un': 1,

                'que' : 1,

                'clavito' : 2,
            },
        )
if __name__ == '__main__':
    unittest.main()