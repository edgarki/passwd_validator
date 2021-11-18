from value import Value


class Validate:

    def __init__(self, t):
        self.t = t
        self.v = Value()

    def cmp_chk(self, val, t):
        if self.v.acc_cmp(t[1]) == '<':
            return val < t[2]
        if self.v.acc_cmp(t[1]) == '>':
            return val > t[2]
        if self.v.acc_cmp(t[1]) == '=':
            return t[2] == val

    def t_chk(self, val, t, size):
        if self.v.acc_type(t[0]) == val:
            return self.cmp_chk(size, t)
        return False

    def rule(self, tup, password):
        if self.v.acc_type(tup[0]) == 'LEN':
            return self.t_chk('LEN', tup, len(password))
        if self.v.acc_type(tup[0]) == 'LETTERS':
            return self.t_chk('LETTERS', tup, self.v.letters_char_count(password))
        if self.v.acc_type(tup[0]) == 'NUMBERS':
            return self.t_chk('NUMBERS', tup, self.v.num_char_count(password))
        if self.v.acc_type(tup[0]) == 'SPECIALS':
            return self.t_chk('SPECIALS', tup, self.v.special_char_count(password))

    def check(self, password):
        count = sum(not self.rule(restrain, password) for restrain in self.t)
        return count == 0

