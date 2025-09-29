import unittest
from strings import to_uppercase, to_lowercase, invert_string, count_vowels, count_consonants, remove_spaces

class TestStringFunctions(unittest.TestCase):
    def test_to_uppercase(self):
        self.assertEqual(to_uppercase('hello'), 'HELLO')
        self.assertEqual(to_uppercase('Hello'), 'HELLO')
        self.assertEqual(to_uppercase('HELLO'), 'HELLO')
        self.assertEqual(to_uppercase('123abc'), '123ABC')
        self.assertEqual(to_uppercase(''), '')

    def test_to_lowercase(self):
        self.assertEqual(to_lowercase('HELLO'), 'hello')
        self.assertEqual(to_lowercase('Hello'), 'hello')
        self.assertEqual(to_lowercase('hello'), 'hello')
        self.assertEqual(to_lowercase('123ABC'), '123abc')
        self.assertEqual(to_lowercase(''), '')

    def test_invert_string(self):
        self.assertEqual(invert_string('hello'), 'olleh')
        self.assertEqual(invert_string('Hello'), 'olleH')
        self.assertEqual(invert_string(''), '')
        self.assertEqual(invert_string('A'), 'A')

    def test_count_vowels(self):
        self.assertEqual(count_vowels('hello'), 2)
        self.assertEqual(count_vowels('HELLO'), 2)
        self.assertEqual(count_vowels('bcdfg'), 0)
        self.assertEqual(count_vowels('aeiou'), 5)
        self.assertEqual(count_vowels(''), 0)

    def test_count_consonants(self):
        self.assertEqual(count_consonants('hello'), 3)
        self.assertEqual(count_consonants('HELLO'), 3)
        self.assertEqual(count_consonants('aeiou'), 0)
        self.assertEqual(count_consonants('bcdfg'), 5)
        self.assertEqual(count_consonants(''), 0)

    def test_remove_spaces(self):
        self.assertEqual(remove_spaces('hello world'), 'helloworld')
        self.assertEqual(remove_spaces(' hello '), 'hello')
        self.assertEqual(remove_spaces(''), '')
        self.assertEqual(remove_spaces('no_spaces_here'), 'no_spaces_here')

if __name__ == '__main__':
    unittest.main()