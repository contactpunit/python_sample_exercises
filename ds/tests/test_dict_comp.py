from ds.ds.dict_comp import filter_bites, bites
import pytest
from collections.abc import MutableMapping


@pytest.mark.parametrize('key', [17, 15, 11])
def test_check_key_in_final_dict(key):
    assert key in filter_bites()


@pytest.mark.parametrize('key', [6, 10, 16, 18, 21])
def test_check_key_not_in_final_dict(key):
    assert key not in filter_bites()


@pytest.mark.xfail
@pytest.mark.parametrize('key', [10])
def test_xfail_entry(key):
    assert key in filter_bites()


def test_result_type_dict():
    assert isinstance(filter_bites(), MutableMapping)
