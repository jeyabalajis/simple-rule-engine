
def numeric(val) -> bool:
    """ Validate whether the value sent is a numeric (integer or float"""
    if type(val).__name__ not in ('int', 'float'):
        return False
    else:
        return True
