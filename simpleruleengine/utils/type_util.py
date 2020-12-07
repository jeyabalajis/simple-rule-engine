def numeric(val) -> bool:
    """ Validate whether the value sent is a numeric (integer or float
    :returns bool"""
    if type(val).__name__ in ('int', 'float'):
        return True

    return False


def string(val) -> bool:
    """ string validates whether the value sent is a string
    :returns bool"""
    if type(val).__name__ == 'str':
        return True

    return False


def string_list(val) -> bool:
    """ string validates whether the value sent is a string
    :returns bool"""
    if type(val).__name__ == 'list':
        for ind_val in val:
            if not string(ind_val):
                return False
        return True
    return False


def is_dict(val) -> bool:
    """ is_dict validates whether the value sent is a dict"""
    if type(val).__name__ == 'dict':
        return True
    return False
