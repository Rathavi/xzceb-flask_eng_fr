import unittest
from translator import french_to_english, english_to_french

class TestTranslator(unittest.TestCase):
    def test_nullinputentofr(self):
        self.assertEqual(english_to_french(''), '')

    def test_nullinputfrtoen(self):
        self.assertEqual(french_to_english(''), '')
        
    def test_englishtofrench(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

    def test_frenchtoenglish(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

if __name__ == "__main__":
    unittest.main()