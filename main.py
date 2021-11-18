from validate import Validate


def print_password_checking(rules, passwd):
    print(f'Password checked: {passwd}')
    print(f'Valid? {Validate(rules).check(passwd)}')


if __name__ == '__main__':
    print_password_checking([('LEN', '=', 8), ('SPECIALS', '>', 1)], 'string@#')


