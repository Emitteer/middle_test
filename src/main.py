from src.calculate_population_data import calculate_population_change
from src.parse_data import parse_population_data


def main():
    filename = 'test_data.txt'
    try:
        population_data = parse_population_data(filename)
        population_changes = calculate_population_change(population_data)

        for country, changes in population_changes.items():
            print(f"Population changes for {country}:")
            for year, change in changes:
                print(f" Year {year}: {change:+}")
            print()
    except Exception as e:
        print(f"Error processing data: {str(e)}")


if __name__ == '__main__':
    main()