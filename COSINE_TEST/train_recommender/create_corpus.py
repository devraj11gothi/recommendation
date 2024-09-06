import os
from scipy import io
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

from train_recommender.utils import preprocess_json

def create_corpus():
    print('inside create corpus')
    corpus = []

    filtered_files = list(map(lambda y: os.path.join('filtered_jsons',y), filter(lambda x: x.endswith('.json'), os.listdir('filtered_jsons'))))
    print('filtered_files are:', filtered_files)
    for file in filtered_files:
        o = preprocess_json(file)
        corpus.append(' '.join(o))
    print('corpus is ', corpus)
    tfidf = TfidfVectorizer()
    query_matrix = tfidf.fit_transform(corpus)
    print('---------------------------------------query_matrix created---------------------------------------')
    io.mmwrite('sparse_matrix.mtx', query_matrix)
    with open('tfidf_recomender.pkl','wb') as f:
        pickle.dump(tfidf,f)
    print('exiting create corpus function')