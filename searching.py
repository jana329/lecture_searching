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


def main():
    print(read_data('sequential.json', 'dna_sequence'))
    pass


if __name__ == '__main__':
    main()