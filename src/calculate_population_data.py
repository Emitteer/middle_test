def calculate_population_change(data):
    changes = {}
    for country, pops in data.items():
        sorted_years = sorted(pops.items())
        changes_list = []
        for i in range(1, len(sorted_years)):
            year1, pop1 = sorted_years[i - 1]
            year2, pop2 = sorted_years[i]
            change = pop2 - pop1
            changes_list.append((year2, change))
        changes[country] = changes_list
    return changes

