import numbers
import decimal


def convert(value: float, fmt: str) -> float:
    #TODO: Complete this
    """Converts the value to the designated format.

    :param value: The value to be converted must be numeric or raise a TypeError
    :param fmt: String indicating format to convert to
    :return: Float rounded to 4 decimal places after conversion
    """
    if not isinstance(value, numbers.Real):
        raise TypeError()
    if fmt.lower() not in ['cm', 'in']:
        raise ValueError()
    if fmt.lower() == 'cm':
        return round(value / 0.39370, 2)
    else:
        decimal.getcontext().prec = 4
        return decimal.Decimal(str(value * 0.39370))
