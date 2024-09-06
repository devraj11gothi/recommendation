import re
import shutil, os, json


def check_if_url(x):
    regex = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    return re.match(regex,x)

def unzip(file_path, root):
    root = os.path.join(os.path.expanduser('~'), 'data', root)
    shutil.rmtree(root, ignore_errors=True)
    shutil.unpack_archive(file_path, root)
    print('successfully unzipped the dataset')
    return root

def preprocess_json(file):
    with open(file, 'r') as f:
        o = json.load(f)

    dict_acc = []
    for item in o['content']:
        print("____",item)
        for x in item:
            print('+++++',item[x])
            for i in item[x]:
                print("-------",item[x][i]["value"])
        # name = item['Overall switchgear interlocking']
        # dict_acc[(item['On Load Busbar Transfer:'], item['Load Shedding:'])] = ' '.join(list(map(lambda x: name+'__'+'_'.join(x['LV compartment lighting:'].split(' ')) + '__' + '_'.join(x['LV compartment Heater:'].split()), item['Heater and Lighting'])))
                dict_acc.append(f"{i}__{item[x][i]["value"]}")
    print('dict_acc', dict_acc)
    return dict_acc
    # dict_acc = dict()
    # for item in o['content']:
    #     print("____", item)
    #     name = item['Overall switchgear interlocking']
    #     for x in item['Heater and Lighting']:
    #         print("x:", x)
    #         print("x['LV compartment lighting:']:", x['LV compartment lighting:'])
    #         print("x['LV compartment Heater:']:", x['LV compartment Heater:'])
    #     dict_acc[(item['On Load Busbar Transfer:'], item['Load Shedding:'])] = ' '.join(list(map(lambda x: name+'__'+'_'.join(x['LV compartment lighting:'].split(' ')) + '__' + '_'.join(x['LV compartment Heater:'].split()), item['Heater and Lighting'])))
    # # print('dict_acc', dict_acc)
    # return dict_acc
