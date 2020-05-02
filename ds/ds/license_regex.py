import re


def validate_license(key: str) -> bool:
    """Write a regex that matches a PyBites license key
       (e.g. PB-U8N435EH-PG65PW87-IXPWQG5T-898XSZI4)
    """
    regex = r"^PB(-[A-Z0-9]{8}){4}$"
    if re.search(regex, key):
        return True
    return False


print(validate_license("PB-U8N435EH-PG65PW87-IXPWQG5T-898XSZI4"))
