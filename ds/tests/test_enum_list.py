from ds.ds.enum_list import enumerate_names_countries, names, countries
import pytest

expected_lines = ['1. Julian      Australia',
                  '2. Bob         Spain',
                  '3. PyBites     Global',
                  '4. Dante       Argentina',
                  '5. Martin      USA',
                  '6. Rodolfo     Mexico'
                  ]


@pytest.mark.parametrize('record', expected_lines)
def test_enumerate_data(record):
    assert '1. Julian      Australia' in expected_lines
    assert '2. Bob         Spain' in expected_lines
    assert '3. PyBites     Global' in expected_lines
    assert '4. Dante       Argentina' in expected_lines
