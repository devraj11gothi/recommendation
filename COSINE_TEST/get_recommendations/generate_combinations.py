import networkx as nx
import json, re

# from get_recommendations.get_filtered_cstic import get_filtered_cstic

def generate_combinations(o, epmname):
    with open('acc_dict.json','r') as f:
        acc_dict = json.load(f)
    # accepted_cstic = get_filtered_cstic(epmname)
    # print('accepted cstics are:', accepted_cstic)
    #weightage defined from insert api in postman and fetched in lines 12 - 15.
    # acc_cstic = [(o[0], o[1][0]) for o in accepted_cstic]
    # # print('acc_cstic',acc_cstic)
    # acc_cstic_dict = {(o[0], o[1][0]) : o[1][1] for o in accepted_cstic}
    # print('acc_cstic_dict', acc_cstic_dict)
    # G = nx.DiGraph()
    # G.add_edges_from(list(o.keys()))
    sents = []

    for k,v in o.items():
        sent = [f'{k[0]}_{k[1]}__{v1}' for v1 in v.split(' ')]
        sents.append(' '.join(sent))
    # print('sents:', sents)
    acc, acc2 = [], []
    for o1 in ' '.join(sents).split():
        acc1 = []
        a1 = o1.split('__')
        # print('a1:',a1)
        print(o1)
        print('detailed a1',(a1[1], a1[2]))
        # if (a1[1], a1[2]) not in acc_cstic:
        #     continue

        for o2 in acc_dict[a1[1]][a1[2]]:
            print(o2)
            if a1[-1].lower() == '_'.join(o2.split()).lower():
                continue

            comb = []
            for o3 in ' '.join(sents).split():
                if o1.lower() == o3.lower():
                    comb.append('__'.join(o3.split('__')[:-1] + [o2]))
                else:
                    comb.append(o3)
            # print('comb',comb)
            acc1.append(' '.join(comb))
            # print('acc1:',acc1)
        acc.append(acc1)
        # acc2.append(acc_cstic_dict[(a1[1], a1[2])])
    # print('acc:', acc)
    print('acc2:',acc2)
    return acc, acc2

