class Value:
    def __init__(self):
        self.acc_kind_of = ['LEN', 'LETTERS', 'NUMBERS', 'SPECIALS']
        self.acc_cmp_char = ['<', '>', '=']
        self.sp_char = ['@', '#', '$', '%']

    def special_char_count(self, password):
        return sum(password.__contains__(s) for s in self.sp_char)

    def letters_char_count(self, password):
        return sum(p.isalpha() for p in password)

    def num_char_count(self, password):
        return sum(p.isdigit() for p in password)

    def acc_type(self, val):
        if val in self.acc_kind_of:
            return val
        return None

    def acc_cmp(self, val):
        if val in self.acc_cmp_char:
            return val
        return None

