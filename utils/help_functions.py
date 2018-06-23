def has_capital(password):
    return any(char.isupper() for char in password)


def has_special_symbol(password):
    special_symbols = "!#$%&()*+,-./:;<=>?@[\]^_`{|}~"
    return any(char in special_symbols for char in password)
