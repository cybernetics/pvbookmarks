
from os import urandom

char_set = {'small': 'abcdefghijklmnopqrstuvwxyz',
             'nums': '0123456789',
             'big': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
             'special': '^!\$%&/()=?{[]}+~#-_.:,;<>|\\'
            }


def generate_pass(length=16):
    """Function to generate a password"""

    password = ''
    current_char_set = ''

    while len(password) < length:
        for i in char_set.iterkeys():
            current_char_set = char_set[i]
            a_char = urandom(1)
            if a_char in current_char_set and a_char not in password:
                if check_prev_char(password, current_char_set):
                    continue
                else:
                    password += a_char
    return password


def check_prev_char(password, char_set):
    """Function to ensure that there are no consecutive
    UPPERCASE/lowercase/numbers/special-characters."""

    index = len(password)
    if index == 0:
        return False
    else:
        prev_char = password[index - 1]
        if prev_char in char_set:
            return True
        else:
            return False

if __name__ == '__main__':
    print generate_pass()

