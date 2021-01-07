from joblib import dump, load
from sklearn.feature_extraction.text import CountVectorizer

import pickle


def predict(text):
    clf = load("model.joblib")
    vec = CountVectorizer(decode_error="replace",
                          vocabulary=pickle.load(open("feature.pkl", "rb")))

    res = clf.predict(vec.transform([text]))[0]

    res_mapping = {0: "Laurynas",
                   1: "Augustinas"}

    return res_mapping[res]
