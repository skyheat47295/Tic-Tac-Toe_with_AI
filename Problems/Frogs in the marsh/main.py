frogs = [120]


def number_of_frogs(year):

    if year == 1:
        return frogs[-1]  # first year of frogs
    else:
        frogs.append((2 * (frogs[- 1] - 50)))
    return number_of_frogs(year - 1)


