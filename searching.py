import os
import json
import time
import random
import matplotlib.pyplot as plt
from bisect import bisect_left

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

    velikosti = [100, 500, 1000, 10000]
    cas_sequence = []

    for n in velikosti:
        data = list(range(n))
        cil = -1

        start = time.perf_counter()
        linear_search(data, cil)
        konec = time.perf_counter()

        cas_sequence.append(konec - start)

    plt.plot(velikosti, cas_sequence, label="linear search")
    plt.xlabel("velikost")
    plt.ylabel("cas")
    plt.title("Srovnání")
    plt.legend()
    plt.show()
    pass



if __name__ == '__main__':
    main()