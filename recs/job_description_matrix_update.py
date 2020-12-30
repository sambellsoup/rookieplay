# library
import matplotlib.pyplot as plt
import pandas as pd
import nltk
nltk.download('stopwords')
nltk.download('punkt')
from rake_nltk import Rake
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
import pickle

from io import StringIO

import urllib

from io import BytesIO

to_add1 = pd.read_csv(r"C:\Users\sambe\Projects\rookieplay\data\compile\Job Descriptions 1.csv")
to_add2 = pd.read_csv(r"C:\Users\sambe\Projects\rookieplay\data\compile\Job Descriptions 2.csv")
to_add3 = pd.read_csv(r"C:\Users\sambe\Projects\rookieplay\data\compile\Job Descriptions 3.csv")

job_descriptions = pd.read_csv('pkl/job_descriptions.csv', index_col=0)

all_to_add = [to_add1, to_add2, to_add3]

result = pd.concat(all_to_add)

result = result.reset_index(drop=True)

result = result.rename(columns = {"JOB TITLE": "title", "JOB DESCRIPTION": "description", "JOB CATEGORY": "category", "LOCATION": "location"})

## Find key words from text using RAKE and transform those keywords into a bag of words
def text_to_bagofwords(df):
    df['rake_key_words'] = ''
    r = Rake()
    for index, row in df.iterrows():
        r.extract_keywords_from_text(row['description'])
        key_words_dict_scores = r.get_word_degrees()
        row['rake_key_words'] = list(key_words_dict_scores.keys())
# Transform key words into bag of words
    df['bag_of_words'] = ''
    for index, row in df.iterrows():
        words = ''
        words += ' '.join(row['rake_key_words']) + ' '
        row['bag_of_words'] = words
    verbose_documentdf = df
    return verbose_documentdf

result = text_to_bagofwords(result)

all_data = [job_descriptions, result]
final = pd.concat(all_data)

final.reset_index(drop=True)

final.to_csv("job_descriptions_dec2020.csv")

final = pd.read_csv('job_descriptions_dec2020.csv', index_col=0)

with open('job_descriptions_dec2020.pkl', 'wb') as f:
    pickle.dump(final, f)
