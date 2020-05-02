import pytest
from ds.ds.chessboard import create_chessboard


@pytest.mark.parametrize('num, index, expected', [
    (8, 0, ' # # # #'),
    (4, 1, '# # '),
    (2, 1, '# '),
    (8, 7, '# # # # ')

])
def test_check_output(capsys, num, index, expected):
    create_chessboard(num)
    out, err = capsys.readouterr()
    assert out.split('\n')[index] == expected