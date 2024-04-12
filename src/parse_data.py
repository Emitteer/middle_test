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
