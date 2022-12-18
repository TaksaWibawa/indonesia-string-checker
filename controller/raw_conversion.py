def raw_to_cfg(raw):
    cfg = [] # create new cfg

    for line in raw:
        cfg.append(line.split(' -> ')) # split rule

    for rule in cfg:
        rule[1] = set(rule[1].split(' | ')) # split body

    for rule in cfg:
        new_body = set() # create new body
        for element in rule[1]:
            element_to_tuple = tuple(element.split(' ')) # split element
            new_body.add(element_to_tuple) # add to new body
        rule[1] = new_body

    return cfg # return cfg

def create_html(raw): # create html from raw
    html_raw = '<p>' 
    for line in raw:
        html_raw += f'{line}<br>' 
    html_raw += '</p>' 
    return html_raw