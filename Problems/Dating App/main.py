
def select_dates(potential_dates):
    candi_dates = [potential_dates[name]['name']
                   for name in range(len(potential_dates))
                   if potential_dates[name]['age'] >= 30
                   and ('art' in potential_dates[name]['hobbies'])
                   and ('Berlin' in potential_dates[name]['city'])]
    return ', '.join(candi_dates)
