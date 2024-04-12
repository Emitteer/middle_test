def read_population_file(filename):
    with open(filename, 'r') as file:
        return file.readlines()


def parse_line(line):
    parts = line.strip().split(',')
    if len(parts) != 3:
        raise ValueError(f"Incorrect format")

    country, year, population = parts
    try:
        year = int(year)
        population = int(population)
    except ValueError:
        raise TypeError(f"Year and population values must be integers")
    return country, year, population


def insert_population_data(data, country, year, population):
    if country not in data:
        data[country] = {}
    if year in data[country]:
        raise ValueError(f"Year {year} is already exist in data for country: {country}")
    data[country][year] = population


def parse_population_data(filename):
    data = {}
    lines = read_population_file(filename)
    for line in lines:
        country, year, population = parse_line(line)
        insert_population_data(data, country, year, population)
    return data
