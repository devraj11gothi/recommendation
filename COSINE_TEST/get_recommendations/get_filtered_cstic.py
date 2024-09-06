import requests, json

def get_filtered_cstic(epmname):
    url = "https://d01api.compasquality.siemens-info.com/report-data-rack/v1/datarack/map/Filter_SLD"
    obj = {"operation": "find",
            "query": {
                "EPMName": epmname
                },
            "fields": {}
            }
    # headers = {"st_token": "ST-3-7eyBsiSGzTnTXhdzeYQ2-compasd01"}
    headers = {"st_token": "ST-15-ERgUdjCoo9uRUaQIKyZL-compasd01"}
    o = requests.post(url, data=json.dumps(obj), headers=headers)

    try:
        o.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print("Error: ", e)
    filtered_vals = json.loads(o.text)['body'][0]['FilterJson']
    acc = []
    for item in filtered_vals['accepted_cstic']:
        for o in item['CSTIC']:
            acc.append((item['description'], o))
    return acc
