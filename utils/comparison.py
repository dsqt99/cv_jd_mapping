# import libraries
from pyvi import ViTokenizer
from sklearn.metrics.pairwise import cosine_similarity

from seq2vec import W2V_PHOBERT
from hyper import *

def remove_stopwords(text):
    stopwords = open(stop_words_path, 'r', encoding='utf-8').read().split('\n')
    text = text.lower()
    text = text.split()
    text = [word for word in text if word not in stopwords]
    text = ' '.join(text)
    return text


# text1: candidate's information; text2: job description

# compare two texts of gender, working form, rank, career, work location (province, district), degree, certificate
def binary_similar_compare(text1, text2):
    if text1 == text2:
        return 1
    else:
        return 0
    
# compare two texts of sub career, title
def percent_similar_compare(text1, text2):
    # tokenize text1
    tokenized1 = ViTokenizer.tokenize(text1)
    # tokenize text2
    tokenized2 = ViTokenizer.tokenize(text2)

    # remove stopwords
    text1 = remove_stopwords(text1)
    text2 = remove_stopwords(text2)

    # compare two texts
    for i in range(min(len(tokenized1), len(tokenized2))):
        count = 0
        if tokenized1[i] == tokenized2[i]:
            count += 1
    return count/min(len(tokenized1), len(tokenized2))


# mapping cv_text to jd_text
model_w2v = W2V_PHOBERT()
def cosine_similarity_compare(cv_text, jd_text):
    cv_vec = model_w2v.t2v(cv_text)
    jd_vec = model_w2v.t2v(jd_text)
    
    cs = cosine_similarity(cv_vec, jd_vec).item()
    return cs
    
# compare the number of years of experience of candidate and job description
def experience_compare(text1, text2):
    if text1 == text2:
        return 1
    elif abs(text1 - text2) == 1:
        return 0.67
    elif abs(text1 - text2) == 2:
        return 0.33
    else:
        return 0
    
# compare the salary of candidate and job description
def salary_compare(text1, text2):
    if text1 == text2:
        return 1
    elif text1 - text2 == -1:
        return 0.8
    elif text1 - text2 == -2:
        return 0.6
    elif text1 - text2 == -3:
        return 0.4
    else:
        return 0
    
