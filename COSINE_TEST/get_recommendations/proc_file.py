# import logging
# logger = logging.getLogger(__name__)
import os
import json
from collections import defaultdict
from fastprogress import progress_bar
REQ_FLDS = ['Project Data', 'Documentation', 'Parameter Setting', 'Wiring Options', 'Auxiliary Voltage', 'Overall switchgear interlocking', 'Overall protection functions', 'Heater and Lighting', 'Remote Control', 'Typicals Section']

# def proc_file(o):
#     print('inside proc file')
#     acc_dict, filter_items = [], ()

#     # if o['MODEL']['ELECTRICAL']['CREATED'] == None:
#     #     logger.log('CREATED instance is empty')

#     # for item in o['MODEL']['ELECTRICAL']['CREATED']['INSTANCE']:
#     #     d = dict()
#     #     for r in REQ_FLDS:
#     #         d[r] = item[f'{r}']

#     #     d['CSTIC'] = list(filter(lambda x: x['isVisible'] == 'Y' or x['number'] in filter_items, item['CSTIC']))
     

#     for entry in o['content']:
#         for field in REQ_FLDS:
#             if field in entry:
#                 for sub_field, sub_value in entry[field].items():
#                     value = sub_value['value']
#                     acc_dict_[field][sub_field]['value'].append(value)
#                     print(f"Adding value: {value} to field: {field}, sub_field: {sub_field}")

#     # Convert defaultdict to regular dict
#     acc_dict_ = {k: dict(v) for k, v in acc_dict_.items()}
#     for field in acc_dict_:
#         acc_dict_[field] = {k: dict(v) for k, v in acc_dict_[field].items()}
#         acc_dict.append(d)
#     print('acc_dict:', acc_dict)
#     print('processed the input json')
#     return {'content': acc_dict}

# import os
# import json

# def proc_file(o):
#     # Required fields
#     REQ_FLDS = ["Overall switchgear interlocking", "Heater and Lighting", "Auxiliary Voltage", "Remote Control"]

#     dict_acc = []
#     for x in o:
#         print("xxxxxx",x)
#         if x in REQ_FLDS:
#             for i in o[x]:
#                 print("iiiiiiiii",o[x][i]['value'])
#                 # dict_acc.append({x:o[x][i]['value']})
#                 dict_acc.append(f"{x}__{o[x][i]['value']}")
#     print(">>>>>>>>>>>>>>>>>>>>",dict_acc)

#     return dict_acc
# o=r'C:\Users\z004zeee\Downloads\COSINE_TEST\COSINE_TEST\Pinos Puente 1- TOC_18_05_2021.json'
# REQ_FLDS = ["Overall switchgear interlocking", "Heater and Lighting", "Auxiliary Voltage", "Remote Control"]

# def proc_file(o):
#     print('inside create_corpus_dict')
#     print("OOOOO", o)

#     # Initialize acc_dict_
#     acc_dict_ = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))

#     for field in REQ_FLDS:
#         if field in o:
#             for sub_field, sub_value in o[field].items():
#                 if isinstance(sub_value, dict) and 'value' in sub_value:
#                     value = sub_value['value']
#                     acc_dict_[field][sub_field]['value'].append(value)
#                     print(f"Adding value: {value} to field: {field}, sub_field: {sub_field}")
#                 else:
#                     print(f"Skipped non-dict sub_value: {sub_value}")

#     # Convert defaultdict to regular dict
#     acc_dict_ = {k: dict(v) for k, v in acc_dict_.items()}
#     for field in acc_dict_:
#         acc_dict_[field] = {k: dict(v) for k, v in acc_dict_[field].items()}

#     print("ACCC_DICT", acc_dict_)
#     return acc_dict_

def clean_string(o):
    return str(o).replace(" ", "_").replace("\n", "_")

def preprocess_input(data):
    # preprocessed_inp = []
    # for item in data['Project Data']:
    #     for subitem in data['Project Data'][item]:
    #         preprocessed_inp.append(f"{item}__{data['Project Data'][item][subitem]}")
    #         print("preprocessed_inputtttttttttt", preprocess_input)
    # return preprocessed_inp

    # acc_list = []
    # for d in REQ_FLDS:
    #     for i, x in data[d].items():
    #         value = x["value"]
    #         print("VVVVAAALLLUUUEEE" ,value)
    #         print("iiiiiiiii", i)
    #         # if d not in ['Add Participants',' Select Typicals ']:
    #             # print([d][i])
    #             # acc_list[d][i]["value"].append(f"{clean_string(d)}__{clean_string([d][i])}")
    #         acc_list[d][i]["value"].append(value)
    #         print(f"value:{value} key: {d}")
    # return acc_list

    acc_list = []
    for d in data:
        for i in data[d]:
            if d not in ['Add Participants',' Select Typicals ']:
                print(data[d][i])
                acc_list.append(f"{clean_string(d)}__{clean_string(data[d][i])}")

    return acc_list

    # acc_list = []
    # for section, content in data.items():
    #     # Skip the sections if they are in the exclusion list
    #     if section not in ['Add Participants', 'Select Typicals']:
    #         for key, value in content.items():
    #             # Print the values and append to the recommendation list
    #             if isinstance(value, dict):
    #                 for sub_key, sub_value in value.items():
    #                     print(sub_value)
    #                     acc_list.append(f"{clean_string(section)}__{clean_string(sub_value)}")
    #             else:
    #                 print(value)
    #                 acc_list.append(f"{clean_string(section)}__{clean_string(value)}")

    # return acc_list


    # Write the aggregated data to a single JSON file
    # output_file = 'aggregated_data.json'
    # with open(output_file, 'w', encoding='UTF-8') as outfile:
    #     json.dump(acc_dict_, outfile, indent=4)

    # print(f'Aggregated data has been written to {output_file}')

              



