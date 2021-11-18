import unittest
from validate import Validate
from value import Value


class TestValidate(unittest.TestCase):
    req = [('LEN', '=', 8), ('SPECIALS', '>', 1), ('NUMBERS', '<', 5)]
    password = '123qwe5r'
    password_two = 'st#ing@1'

    v = Validate(req)
    value = Value()

    def test_cmp_chk(self):
        self.assertTrue(self.v.cmp_chk(8, self.req[0]), msg='val must be the same of length tuple with its rule')
        self.assertFalse(self.v.cmp_chk(9, self.req[0]), msg='val must be the same of length tuple with its rule')
        self.assertTrue(self.v.cmp_chk(2, self.req[1]), msg='val must be the same of length tuple with its rule')
        self.assertFalse(self.v.cmp_chk(1, self.req[1]), msg='val must be the same of length tuple with its rule')

    def test_t_chk(self):
        self.assertTrue(self.v.t_chk('LEN', self.req[0], len(self.password)),
                        msg='Typecheck must match type of rule with its rule and size')
        self.assertTrue(self.v.t_chk('SPECIALS', self.req[1], self.value.special_char_count(self.password_two)),
                         msg='Typecheck must match type of rule with its rule and size')
        self.assertFalse(self.v.t_chk('SPECIALS', self.req[1], self.value.special_char_count(self.password)),
                         msg='Typecheck must match type of rule with its rule and size')

    def test_rule(self):
        self.assertTrue(self.v.rule(self.req[0], self.password), msg='Rule must match given password')
        self.assertTrue(self.v.rule(self.req[0], self.password_two), msg='Rule must match given password')
        self.assertFalse(self.v.rule(self.req[1], self.password), msg='Rule must match given password')
        self.assertTrue(self.v.rule(self.req[1], self.password_two), msg='Rule must match given password')
        self.assertFalse(self.v.rule(self.req[1], self.password), msg='Rule must match given password')

    def test_check(self):
        self.assertFalse(self.v.check(self.password), msg='check verify all req conditions are true')
        self.assertTrue(self.v.check(self.password_two), msg='check verify all req conditions are true')