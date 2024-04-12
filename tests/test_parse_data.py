import pytest
from src.parse_data import read_population_file, parse_line, \
    insert_population_data, parse_population_data


@pytest.fixture
def mock_file_data(mocker):
    file_content = ('Ukraine,1990,52000000\nPoland,1990,38000000\nUkraine,'
                    '1991,51000000')
    mocker.patch('builtins.open', mocker.mock_open(read_data=file_content))
    return file_content.split('\n')


@pytest.mark.parametrize("line, expected", [
    ('Ukraine,1990,52000000', ('Ukraine', 1990, 52000000)),
    ('Poland,1990,38000000', ('Poland', 1990, 38000000)),
])
def test_parse_line_correct_format(line, expected):
    assert parse_line(line) == expected


@pytest.mark.parametrize("line", [
    'Ukraine199052000000',
    'Poland,19903800000',
])
def test_parse_line_incorrect_format(line):
    with pytest.raises(ValueError):
        parse_line(line)


@pytest.mark.parametrize("line", [
    'Ukraine,1990,sdad',
    'Poland,1990,on',
])
def test_parse_line_type_error(line):
    with pytest.raises(TypeError):
        parse_line(line)


@pytest.fixture
def population_data():
    return {'Ukraine': {1990: 52000000}}


@pytest.mark.parametrize("country, year, population, expected", [
    ('Ukraine', 1991, 51000000,
     {'Ukraine': {1990: 52000000, 1991: 51000000}}),
    ('Poland', 1990, 38000000,
     {'Ukraine': {1990: 52000000}, 'Poland': {1990: 38000000}}),
])
def test_insert_population_data_no_duplicates(population_data, country, year,
                                              population,
                                              expected):

    insert_population_data(population_data, country, year, population)
    assert population_data == expected


@pytest.mark.parametrize("country, year, population", [
    ('Ukraine', 1990, 51000000),
])
def test_insert_population_data_duplicate_year(population_data, country, year,
                                               population):
    with pytest.raises(ValueError):
        insert_population_data(population_data, country, year, population)
