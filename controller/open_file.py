def open_file(filepath):
    data = [] # list of rules
    with open(filepath, 'r') as file:
        raw = file.readlines() # read file

        for rule in raw:
            data.append(rule.strip('\n')) # append rule to list

    return data # return list of rules