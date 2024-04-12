import pytest
from src.calculate_population_data import calculate_population_change


@pytest.fixture
def population_data():
    return {
        'Ukraine': {1990: 52000000, 1991: 51000000, 1995: 50000000},
        'Poland': {1990: 38000000, 1991: 38050000, 1992: 38100000}
    }


@pytest.mark.parametrize("country, expected_changes", [
    ('Ukraine', [(1991, -1000000), (1995, -1000000)]),
    ('Poland', [(1991, 50000), (1992, 50000)]),
])
def test_calculate_population_change(population_data, country,
                                     expected_changes):
    changes = calculate_population_change(population_data)
    assert changes[country] == expected_changes
