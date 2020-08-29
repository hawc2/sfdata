# source - https://www.machinelearningplus.com/nlp/topic-modeling-gensim-python/
from __future__ import unicode_literals, print_function
import numpy as np
import pandas as pd
import gensim
import gensim.corpora as corpora
from gensim.utils import simple_preprocess
from gensim.models import CoherenceModel
import pyLDAvis
import pyLDAvis.gensim
import matplotlib.pyplot as plt
import os
from importlib import reload
from pprint import pprint
import sys
#get_ipython().run_line_magic('matplotlib', 'inline')

def LDA(data):
    path = os.path.dirname(os.path.abspath(__file__))
    df = pd.read_csv(data)
    df.to_json (path + '/data/HL.json')
    data = df.text.values.tolist()

    def sent_to_words(sentences):
        for sentence in sentences:
          yield(gensim.utils.simple_preprocess(str(sentence), deacc=True))  # deacc=True removes punctuations

    data_words = list(sent_to_words(data))
    id2word = corpora.Dictionary(data_words)
    texts = data_words
    corpus = [id2word.doc2bow(text) for text in texts]

    lda_model = gensim.models.ldamodel.LdaModel(corpus=corpus,
                                           id2word=id2word,
                                           num_topics=20,
                                           random_state=100,
                                           update_every=2,
                                           chunksize=100,
                                           passes=20,
                                           alpha='auto',
                                           per_word_topics=True)

    vis = pyLDAvis.gensim.prepare(lda_model, corpus, id2word)
    pyLDAvis.save_html(vis, path + '/templates/LDAviz.html')
