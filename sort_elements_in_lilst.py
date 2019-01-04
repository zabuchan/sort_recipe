names = ['arnold schwarzenegger', 'alec baldwin', 'sandra bullock', 'keanu reeves',
         'al pacino', 'brad pitt', 'matt damon']


def sort_by_surname_in_desc(names):
    names.sort(key=lambda x: x.split(' ')[1])
    return names

