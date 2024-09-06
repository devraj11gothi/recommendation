import os
import json
from collections import defaultdict
from fastprogress import progress_bar

# Directory containing the JSON files
p=r'C:\Users\z004x90j\Desktop\COSINE_TEST\filtered_jsons'

# Required fields
REQ_FLDS = ["Overall switchgear interlocking", "Heater and Lighting", "Auxiliary Voltage", "Remote Control"]

def create_corpus_dict(p):
    print('inside create_corpus_dict')
    
    # Initialize a dictionary to accumulate data
    acc_dict_ = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))

    # List all JSON files in the directory
    fs = list(map(lambda y: os.path.join(p, y), filter(lambda x: x.endswith('.json'), os.listdir(p))))
    print('fs is:', fs)

    for file in progress_bar(fs):
        with open(file, 'r', encoding='UTF-8') as f:
            o = json.load(f)

        if 'content' not in o:
            print(f"'content' not in file: {file}")
            continue

        for entry in o['content']:
            for field in REQ_FLDS:
                if field in entry:
                    for sub_field, sub_value in entry[field].items():
                        value = sub_value['value']
                        acc_dict_[field][sub_field]['value'].append(value)
                        print(f"Adding value: {value} to field: {field}, sub_field: {sub_field}")

    # Convert defaultdict to regular dict
    acc_dict_ = {k: dict(v) for k, v in acc_dict_.items()}
    for field in acc_dict_:
        acc_dict_[field] = {k: dict(v) for k, v in acc_dict_[field].items()}

    # Write the aggregated data to a single JSON file
    output_file = 'aggregated_data.json'
    with open(output_file, 'w', encoding='UTF-8') as outfile:
        json.dump(acc_dict_, outfile, indent=4)

    print(f'Aggregated data has been written to {output_file}')

# Call the function with the directory path
# create_corpus_dict(p)













































    #     # if o['MODEL']['ELECTRICAL']['CREATED']['INSTANCE'] is None:
    #     #     continue

    #     # for item in o['MODEL']['ELECTRICAL']['CREATED']['INSTANCE']:
    #     #     name = item['name']
    #     #     for item1 in item['Overall switchgear interlocking']:
    #     #         # if item1['isVisible'] == 'N':
    #     #         #     continue
    #     #         if name in acc_dict_:
    #     #             if item1['name'] in acc_dict_[name]:
    #     #                 v = '_'.join(item1['value'].split()).lower()
    #     #                 if v not in acc_dict_[name][item1['name']] and item1['value'] != '':
    #     #                     acc_dict_[name][item1['name']].append(v)
    #     #             else:
    #     #                 acc_dict_[name][item1['name']] = []
    #     #         else:
    #     #             acc_dict_[name] = {item1['name']: [item1['value']]}
    #     # for item in o:
    #     #     # print(item)
    #     #     if item in REQ_FLDS:
    #     #         print("---",o[item])
    #     # #         acc_dict_.update( f"{item}__{o[item]}")
    #     # # print(acc_dict_)
    #     for item in o:
    #         print("____",item)
    #         for x in item:
    #            print('+++++',item[x])
    #            for i in item[x]:
    #             print("-------",item[x][i]["value"])
    #     # name = item['Overall switchgear interlocking']
    #     # dict_acc[(item['On Load Busbar Transfer:'], item['Load Shedding:'])] = ' '.join(list(map(lambda x: name+'__'+'_'.join(x['LV compartment lighting:'].split(' ')) + '__' + '_'.join(x['LV compartment Heater:'].split()), item['Heater and Lighting'])))
    #             acc_dict_.update(f"{i}__{item[x][i]["value"]}")
    # print('dict_acc>>>>>>>>>>>>>>>>>>>>>>>', acc_dict_)

    # with open('acc_dict.json','w') as f:
    #     json.dump(acc_dict_, f, indent=4)
    # print('created acc_dict json file')

