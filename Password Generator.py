import random


def gen_password(n, lower=True, upper=True, num=True, sym=True):
    """
    :param n: length of password
    :param lower: if True lowercase letters are a requirement
    :param upper: if True uppercase letters are a requirement
    :param num: if True numbers are a requirement
    :param sym: if True symbols are a requirement
    :return: a string that meets the requirements of the password
    """
    assert n > 0 and lower is True or upper is True or num is True or sym is True
    alpha_lower = 'abcdefghijklmnopqrstuvwxyz'
    alpha_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    nums = '1234567890'
    syms = '!@#$%^&*?'
    password = []
    if lower:
        password.append(alpha_lower[random.randint(0, 25)])
        n -= 1
    if upper:
        password.append(alpha_upper[random.randint(0, 25)])
        n -= 1
    if num:
        password.append(nums[random.randint(0, 9)])
        n -= 1
    if sym:
        password.append(syms[random.randint(0, 7)])
        n -= 1
    while True:
        if n == 0:
            break
        rand_i = random.randint(1, 4)
        if lower and rand_i == 1:
            password.append(alpha_lower[random.randint(0, 25)])
            n -= 1
        if upper and rand_i == 2:
            password.append(alpha_upper[random.randint(0, 25)])
            n -= 1
        if num and rand_i == 3:
            password.append(nums[random.randint(0, 9)])
            n -= 1
        if sym and rand_i == 4:
            password.append(syms[random.randint(0, 7)])
            n -= 1
    random.shuffle(password)
    password = ''.join(password)
    return password


def password_with_specs():
    while True:
        super_ans = input('Would you like your password to be a super password? Enter yes or no.')
        if super_ans != 'yes' and super_ans != 'no':
            print('Please enter a valid answer.')
        elif super_ans == 'yes':
            n = 18
            lower = True
            upper = True
            num = True
            sym = True
            break
        else:
            while True:
                n = input('How many characters would you like in you\'re password? Enter a number. (20 character limit)')
                try:
                    n = int(n)
                    if n < 1:
                        print('Please enter a number greater than 0.')
                    elif n > 20:
                        print('Please enter a lower number.')
                    else:
                        break
                except ValueError:
                    print('Please enter a number.')
            while True:
                low_ans = input('Do you need lowercase characters? Enter yes or no.')
                if low_ans == 'yes':
                    lower = True
                    break
                elif low_ans == 'no':
                    lower = False
                    break
                else:
                    print('Please enter a valid response.')
            while True:
                upper_ans = input('Do you need uppercase characters? Enter yes or no.')
                if upper_ans == 'yes':
                    upper = True
                    break
                elif upper_ans == 'no':
                    upper = False
                    break
                else:
                    print('Please enter a valid response.')
            while True:
                num_ans = input('Do you need numbers? Enter yes or no.')
                if num_ans == 'yes':
                    num = True
                    break
                elif num_ans == 'no':
                    num = False
                    break
                else:
                    print('Please enter a valid response.')
            while True:
                sym_ans = input('Do you need symbols? Enter yes or no.')
                if sym_ans == 'yes':
                    sym = True
                    break
                elif sym_ans == 'no':
                    sym = False
                    break
                else:
                    print('Please enter a valid response.')
            break
    try:
        password = gen_password(n, lower, upper, num, sym)
        return password
    except AssertionError:
        print('A password cannot be created with those parameters.')


password = password_with_specs()
print(f'Here is you\'re password:\n{password}')

