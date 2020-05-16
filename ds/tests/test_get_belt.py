import pytest

from ds.ds.get_belts import get_belt, scores, HONORS


@pytest.mark.parametrize("input_argument, expected_return", [
    (48, 'white'),
    (50, 'yellow'),
    (101, 'orange'),
])
def test_get_belt(input_argument, expected_return):
    assert get_belt(input_argument) == expected_return