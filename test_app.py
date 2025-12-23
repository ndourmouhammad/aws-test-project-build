# test_app.py
import unittest
from app import say_hello

class TestApp(unittest.TestCase):
    def test_say_hello(self):
        # Enlevez la virgule pour correspondre à la fonction
        self.assertEqual(say_hello("AWS"), "Hello AWS")
        # Optionnel : testez avec d'autres noms
        self.assertEqual(say_hello("World"), "Hello World")
        self.assertEqual(say_hello(""), "Hello ")

if __name__ == "__main__":
    unittest.main()
