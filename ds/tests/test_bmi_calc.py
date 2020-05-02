import pytest
from ds.ds.bmi_calc import handle_args, create_parser, calc_bmi


@pytest.fixture()
def return_parser():
    c = create_parser()
    return c


@pytest.mark.parametrize('options, expected', [
    (['-l', '187', '-w', '80'], "Your BMI is: 22.88"),
    (['-l', '200', '-w', '100'], "Your BMI is: 25.0")
])
def test_screen_display(capsys, return_parser, options, expected):
    c = create_parser()
    args = c.parse_args(options)
    handle_args(args)
    out, err = capsys.readouterr()
    assert expected in out
