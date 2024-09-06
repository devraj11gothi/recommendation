import os, requests
from train_recommender.utils import check_if_url

def download(x):
    assert check_if_url(x)
    file_name = x.split('/')[-1]
    os.makedirs(os.path.join(os.path.expanduser('~'), 'temp'), exist_ok=True)
    r = requests.get(x, stream=True)
    if r.status_code != 200:
        raise RuntimeError("Failed downloading url %s"%url)

    file_path = os.path.join(os.path.expanduser('~'), 'temp', file_name)

    with open(file_path, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
    print('successfully downloaded the json zip file')
    return file_path