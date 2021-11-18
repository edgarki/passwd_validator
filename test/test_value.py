import unittest
from value import Value


class TestValue(unittest.TestCase):
    password = '123qwe5r'
    password_two = 'st#ing@1'
    
    value = Value()

    def test_special_char_count(self):
        self.assertEqual(self.value.special_char_count(self.password), 0)
        self.assertEqual(self.value.special_char_count(self.password_two), 2)

    def test_letters_char_count(self):
        self.assertEqual(self.value.letters_char_count('31235436'), 0)
        self.assertEqual(self.value.letters_char_count(self.password), 4)
        self.assertEqual(self.value.letters_char_count(self.password_two), 5)

    def test_num_char_count(self):
        self.assertEqual(self.value.num_char_count(self.password), 4)
        self.assertEqual(self.value.num_char_count(self.password_two), 1)

    def test_acc_type(self):
        self.assertIsNone(self.value.acc_type('BLA'))
        self.assertIsNone(self.value.acc_type('123123'))
        self.assertIsNone(self.value.acc_type('azsdfsx124a'))
        self.assertEqual(self.value.acc_type('LEN'), 'LEN', msg='It must use reserved rule')
        self.assertEqual(self.value.acc_type('LETTERS'), 'LETTERS', msg='It must use reserved rule')
        self.assertEqual(self.value.acc_type('NUMBERS'), 'NUMBERS', msg='It must use reserved rule')
        self.assertEqual(self.value.acc_type('SPECIALS'), 'SPECIALS', msg='It must use reserved rule')
        self.assertIsNone(self.value.acc_type('SPECIALS2'))

    def test_acc_cmp(self):
        self.assertEqual(self.value.acc_cmp('<'), '<', msg='It must use reserved comparison command')
        self.assertEqual(self.value.acc_cmp('>'), '>', msg='It must use reserved comparison command')
        self.assertEqual(self.value.acc_cmp('='), '=', msg='It must use reserved comparison command')
        self.assertIsNone(self.value.acc_cmp('<<'))
        self.assertIsNone(self.value.acc_cmp('<>'))
        self.assertIsNone(self.value.acc_cmp('>>>'))