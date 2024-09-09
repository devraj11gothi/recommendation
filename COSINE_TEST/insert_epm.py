import requests, json

def insert_epm():
    url = "https://d01api.compasquality.siemens-info.com/report-data-rack/v1/datarack/map/Filter_SLD"
    with open('weighted_epm1.json') as f: obj = json.load(f)
    # headers = {"st_token": "ST-3-7eyBsiSGzTnTXhdzeYQ2-compasd01"}
    headers = {"st_token": "ST-15-ERgUdjCoo9uRUaQIKyZL-compasd01"}
    o = requests.post(url, data=json.dumps(obj), headers=headers)
    return o

if __name__ == "__main__":
    print(insert_epm())
