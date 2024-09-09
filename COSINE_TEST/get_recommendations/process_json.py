import json

def process_json(o):
    with open ('acc_dict.json', 'r') as f:
        acc_dict = json.load(f)
    dict_acc = dict()

    for item in o['content']:
        name = item['name']
        sent_acc = []

        for x in item['Overall switchgear interlocking']:
            print('x',x)
            name_ = '_'.join(x['Overall switchgear interlocking :'].split(' '))
            print('name',name_)
            value_ = '_'.join(x['value'].split(' ')) if x['value'] != '' else "None" if len(acc_dict[name][name_]) == 0 else acc_dict[name][name_][0]
            print('value_',value_)
            sent_acc.append(name + '__' + name_ + '__' + value_)

        dict_acc[(item['parent'], item['number'])] = ' '.join(sent_acc)
        # dict_acc[(item['parent'], item['number'])] = ' '.join(list(map(lambda x: name + '__' + '_'.join(x['name'].split(' ')) + '__' + '_'.join(x['value'].split()), item['CSTIC'])))
    print('dict_acc:', dict_acc)
    return dict_acc
