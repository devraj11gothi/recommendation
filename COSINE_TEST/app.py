from flask import Flask, request
import logging, shutil, pickle
from sklearn.metrics.pairwise import cosine_similarity
from flask_cors import CORS, cross_origin
from scipy import io
import numpy as np
import json

from train_recommender.download import download
from train_recommender.utils import unzip
from train_recommender.filter_json_files import filter_json_files
from train_recommender.create_corpus import create_corpus
from train_recommender.create_corpus_dict import create_corpus_dict

from get_recommendations.proc_file import preprocess_input
from get_recommendations.process_json import process_json
from get_recommendations.generate_combinations import generate_combinations
from get_recommendations.utils import format_out
import json
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


app = Flask(__name__)
cors = CORS(app)
logger = logging.getLogger(__name__)

query_matrix = io.mmread('sparse_matrix (2).mtx')
with open('C:\\Users\\z004zeee\\Downloads\\tfidf_recomender.pkl', 'rb') as f:
    tfidf = pickle.load(f)

# query_matrix = None
# tfidf = None
@app.route('/sldservice1/train_recomender', methods=['POST'])
@cross_origin()
def train_recommendation():
    args = request.get_json()
    json_url = args['json_url']
    print('json_url:', json_url)
    # p = download(json_url)
    # p = unzip(p, 'json_files')
    p=r'C:\Users\z004x90j\Desktop\github_test-main'
    o = filter_json_files(p)
    print('outside filter_json_files function')
    create_corpus()
    # create_corpus_dict(p)
    print('trained model successfully')
    # shutil.rmtree(p)
    # shutil.rmtree('filtered_jsons')
    return {'status': "training successful"}

@app.route('/sldservice1/recomender', methods=['POST'])
@cross_origin()



def get_recomendation():
    json_file = 'C:\\Users\\z004zeee\\Desktop\\SIEMENS\\JSON pred\\JSON_FROM_DOCX 1\\JSON_FROM_DOCX\\978848_TocLst_20200316.json'
    with open(json_file, 'r') as file:
        data = json.load(file)

    with open('acc.json', 'r') as file:
        acc = json.load(file)
    # print(data)


    preprocessed_inp = preprocess_input(data)
    rec_list = []

    for acc1 in preprocessed_inp:

        question_matrix = tfidf.transform([acc1])
        print("query matrix shape:::::::::", query_matrix.shape)
        print("qestion matrix shape:::::::::", question_matrix.shape)
        # rank_values = query_matrix @ question_matrix.T
        rank_values = cosine_similarity(query_matrix, question_matrix)
        print("rank_values -- ",rank_values)
        rank_values = np.array(rank_values).squeeze()
        print("rank_values ---- ",rank_values)
        top_5 = np.argsort(rank_values)[-5:]
        print("top_5 -- ",top_5)
        print(type(top_5[0]))
        print(f"--------------{acc1}-------------")
        resp = {"recommendation": [acc[i] for i in list(top_5)]}
        print(resp)
        rec_list.append({"key":acc1.split("__")[0],
                         "value":acc1.split("__")[1],
                         "recommendation":[acc[i].split("__")[1] for i in list(top_5)]})
    return rec_list
        # print(d)
    return 'sus'

if __name__ == "__main__":
    app.run(debug=True, port=5002, host='0.0.0.0')
