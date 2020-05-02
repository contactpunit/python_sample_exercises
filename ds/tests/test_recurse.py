from ds.ds.recurse import countdown_recursive
import pytest


@pytest.mark.parametrize('nums', [
    (12, '12\n11\n10\n9\n8\n7\n6\n5\n4\n3\n2\n1\ntime is up\n'),
    (10, '10\n9\n8\n7\n6\n5\n4\n3\n2\n1\ntime is up\n'),
    (5, '5\n4\n3\n2\n1\ntime is up\n')
])
def test_print_output(capsys, nums):
    countdown_recursive(nums[0])
    out, err = capsys.readouterr()
    assert out == nums[1]