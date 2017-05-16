
class Sum(object):
    def __init__(self, number, data):
        self.number = number
        self.data = data


def add_elem_and_frequency(total, first, frequencies):
    total.data.add(first)
    total.number += frequencies[first] if first in frequencies else 0


def name_list(people, frequencies):

    final_map = {}

    for person in people:
        second = people[person]
        if person not in final_map and second not in final_map:
            fperson = frequencies[person] if person in frequencies else 0
            fsecond = frequencies[second] if second in frequencies else 0
            total = Sum(fperson + fsecond, set([person, second]))
            final_map[person] = final_map[second] = total
        else:
            first_total = final_map[person] if person in final_map else None
            second_total = final_map[second] if second in final_map else None
            if first_total and second_total:
                for elem in list(second_total.data):
                    if elem not in first_total.data:
                        add_elem_and_frequency(first_total, elem, frequencies)
                        final_map[elem] = first_total
            else:
                print(person, second)
                p = person if person is not None else second
                total = first_total if p == person else second_total
                add_elem_and_frequency(total, p, frequencies)
                final_map[p] = total

    result = {}
    for elem in final_map:
        result[list(final_map[elem].data)[0]] = final_map[elem].number

    return result



people = {}

people['John'] = 'Johnny'
people['Jon'] = 'John'
people['Chris'] = 'Kris'
people['Cristopher'] = 'Chris'

freq = {
    'John': 15,
    'Jon': 12,
    'Chris': 13,
    'Kris': 4,
    'Cristopher': 19
}

print(name_list(people, freq))



    