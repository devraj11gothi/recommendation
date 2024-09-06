import json

def process_node(o):
    d = dict()
    for i in o:
        if i[0] not in d:
            d[i[0]] = [list(i[1:])]
        else:
            d[i[0]].append(list(i[1:]))
    return d

def format_out(o):
    with open('aggregated_data.json','r') as f:
        acc_dict = json.load(f)

    d = dict()

    for i in o.split():
        a = i.split('__')
        if a[-1] == '':
            continue
        if a[-1] not in acc_dict[a[1]][a[2]] and acc_dict[a[1]][a[2]]:
            a[-1] = acc_dict[a[1]][a[2]][0]

        node = str(tuple(a[0].split('_')))

        if node in d:
            d[node].append(tuple(a[1:]))
        else:
            d[node] = [tuple(a[1:])]

    d1 = dict()

    for k,v in d.items():
        d1[k] = process_node(v)
    return d1