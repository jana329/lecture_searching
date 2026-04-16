import os
import json

from generators import dna_sequence

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)

    with open(file_path, "r", encoding='utf-8') as file:
        data = json.load(file)

    if field not in data:
        return None

    return data[field]

def linear_search(sequence, target):
    positions = []

    for index, value in enumerate(sequence):
        if value == target:
            positions.append(index)

    return {
        'positons': positions,
        'count': len(positions)
    }

def binary_search(sequence, target):
    levy = 0
    pravy = len(sequence) - 1

    while levy <= pravy:
        stred = (levy + pravy) // 2

        if sequence[stred] == target:
            return stred

        elif sequence[stred] < target:
            levy = stred + 1

        else:
            pravy = stred - 1

    return None

def main():
    nactena_data = read_data('sequential.json', 'ordered_numbers')
    print(nactena_data)

    vysledek = linear_search(nactena_data, target=5)
    print(vysledek)

    binarni = binary_search(nactena_data, target=13)
    print(binarni)
    pass



if __name__ == '__main__':
    main()