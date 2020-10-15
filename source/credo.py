from random import randint


def generate_phone():
    """

    :return: номер телефона в формате +ХХХ(ХХХ)ХХХ-ХХ-ХХ

    """
    country_code = randint(1, 999)
    n = '0000000000'
    while '9' in n[3:6] or n[3:6] == '000' or n[6] == n[7] == n[8] == n[9]:
        n = str(randint(10 ** 9, 10 ** 10 - 1))
    return f'+{country_code}({n[:3]}){n[3:6]}-{n[6:8]}-{n[8:]}'
