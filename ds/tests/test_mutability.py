from ds.ds.mutability import duplicate_items, items
import pytest

keys = len(items)

original = items
duplicate = duplicate_items(items)


def original_keys():
    return [item.keys() for item in items]


def copied_keys():
    return [item.keys() for item in duplicate]


def original_values():
    return [item.values() for item in items]


def copied_values():
    return [item.values() for item in duplicate]


def get_key_params():
    return [(k1, k2) for k1, k2 in zip(original_keys(), copied_keys())]


def test_num_items_same():
    assert keys == len(duplicate)


@pytest.mark.parametrize('keys1, keys2', get_key_params())
def test_element_keys_same(keys1, keys2):
    assert keys1 == keys2


@pytest.mark.parametrize('v1, v2', [
    (original[0]['name'], duplicate[0]['name']),
    (original[-1]['id'], duplicate[-1]['id'])
])
def test_check_values(v1, v2):
    assert v1 == v2


duplicate[0]['name'] = 'Punit'
duplicate[-1]['id'] = 23


@pytest.mark.parametrize('v1, v2', [
    (original[0]['name'], 'laptop'),
    (original[-1]['id'], 3)
])
def test_changed_values(v1, v2):
    assert v1 == v2
