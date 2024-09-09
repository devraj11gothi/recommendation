import os,json
import fastprogress

REQ_FLDS = ["Overall switchgear interlocking","Heater and Lighting", "Auxiliary Voltage","Remote Control"]

def  filter_json_files(p):
    print('inside filter_json_files')
    fs = list(map(lambda y: os.path.join(p,y), filter(lambda x: x.endswith('.json'), os.listdir(p))))
    # print('fs',fs)
    filter_items = ()
    os.makedirs('filtered_jsons', exist_ok = True)

    for k, file in enumerate(fastprogress.progress_bar(fs)):
        print("---------file",file)
        if os.path.isdir(file):
            
            continue
        with open(file,'r', encoding='utf-8') as f:
            o = json.load(f)
        acc_dict = []
        # print('o',o)

        # if o['MODEL']['ELECTRICAL']['CREATED'] == None:
        #     continue
        for item in o:
            d = dict()

            for r in REQ_FLDS:
                d[r] = o[f'{r}']

            # d['Overall switchgear interlocking'] = list(filter(lambda x: x['On Load Busbar Transfer:'] in [] or x['Load Shedding:'] in [] , o['Overall switchgear interlocking']))
            # d['Heater and Lighting'] = list(filter(lambda x: x['LV compartment Heater:'] in [] or x['LV compartment lighting:'] in [], o['Heater and Lighting']))

            acc_dict.append(d)
        print('successfully created acc_dict--------------------',acc_dict)
        json_out = json.dumps({'content':acc_dict})
        # print(acc_dict)
        with open(f'filtered_jsons/{os.path.basename(file)}','w') as out_file:
            out_file.write(json_out)
        print('raw data filtered and stored inside filtered_jsons folder')
