"""Module to test"""
import unittest 
from translator import english_to_french, french_to_english

class TestTranslation(unittest.TestCase): 

    def test_english_to_french(self):
        self.assertEqual(english_to_french("Car"), "Voiture")
        self.assertNotEqual(english_to_french("Car"), "Car")
    
    def test_french_to_english(self):
        self.assertEqual(french_to_english("Voiture"), "Car")
        self.assertNotEqual(french_to_english("Voiture"), "Voiture")

if __name__ =='__main__':
    unittest.main()


