import pytest
from ds.ds.license_regex import validate_license


@pytest.mark.parametrize('key, expected', [
    ('PB-U8N435EH-PG65PW87-IXPWQG5T-898XSZI4', True),
    ('pb-U8N435EH-PG65PW87-IXPWQG5T-898XSZI4', False),
    ('PB-U8N435EH-PG65PW87-IXPWQG5T-898XSZ..', False),
    ('bogus', False),
    ('SPB-U8N435EH-PG65PW87-IXPWQG5T-898XSZI4', False)
])
def test_check_regex(key, expected):
    assert validate_license(key) == expected
