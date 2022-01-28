import random
# from creatures import characters


# get name list (french as an example)
def first_name():
    name_dictionary = {}
    name_file = open('./assets/names/French')
    for line in name_file:
        key, value = line.split()

        name_dictionary[key] = value

    # random.choice(list(name_dictionary.values()))
    return random.choice(list(name_dictionary.values()))
