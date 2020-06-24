""" You are given a sequence of a journey in London, UK. The sequence will contain bus numbers and TFL tube names
as strings e.g.

['Northern', 'Central', 243, 1, 'Victoria']
Journeys will always only contain a combination of tube names and bus numbers. Each tube journey costs £2.40 and each
 bus journey costs £1.50. If there are 2 or more adjacent bus journeys, the bus fare is capped for sets of two adjacent
  buses and calculated as one bus fare for each set.

Your task is to calculate the total cost of the journey and return the cost rounded to 2 decimal places in the format
 (where x is a number): £x.xx

"""


def london_city_hacker(journey):
    total_cost = 0
    adjacent_bus_tour = 0
    for tour in journey:
        if type(tour) == str:
            adjacent_bus_tour = 0
            total_cost += 2.40
        else:
            adjacent_bus_tour += 1
            if adjacent_bus_tour == 2:
                adjacent_bus_tour = 0
            else:
                total_cost += 1.50
    return f'£{total_cost:.2f}'