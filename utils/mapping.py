import sys
sys.path.append('./utils')

import os
import re
import json
import pandas as pd

from translate import transdata
from dataloader import DataLoader
from comparison import *
from hyper import *


def preprocess_text(text):
    # Lowercase
    text = text.lower()
    # Remove leading and trailing whitespaces
    text = text.strip()
    # Remove excessive whitespaces
    text = re.sub(r'\s+', ' ', text)
    # Remove newlines
    text = re.sub(r'\n', ' ', text)

    return text

def percent_mapping(uv, jd):
    # compare
    percent = {}
    # gender
    percent['gender'] = binary_similar_compare(uv['gender'], jd['new_gioi_tinh']) if jd['new_gioi_tinh'] != 0 else 1
    # working form
    percent['working_form'] = binary_similar_compare(uv['working_form'], jd['new_hinh_thuc'])
    # rank
    percent['rank'] = binary_similar_compare(uv['rank'], jd['new_cap_bac'])
    # main career
    percent['main_career'] = binary_similar_compare(uv['main_career'], jd['new_nganh_nghe'])
    # sub career
    percent['sub_career'] = percent_similar_compare(uv['sub_career'], jd['new_tag'])
    # work province
    percent['work_province'] = binary_similar_compare(uv['work_province'], jd['new_city'])
    # work district
    percent['work_district'] = binary_similar_compare(uv['work_district'], jd['new_district'])
    # level learning
    percent['level_learning'] = binary_similar_compare(uv['level_learning'], jd['new_bang_cap']) if jd['new_bang_cap'] != 0 else 1
    # certificate
    percent['certificate'] = binary_similar_compare(uv['certificate'], jd['new_chung_chi'])
    # experience
    percent['experience'] = experience_compare(uv['experience'], jd['new_exp']) if jd['new_exp'] != 0 else 1
    # title
    percent['title'] = percent_similar_compare(uv['title'], jd['new_title'])
    # job description
    percent['job_description'] = cosine_similarity_compare(uv['mota_kinhnghiem'], jd['new_mota'])
    # job requirement
    percent['job_requirement'] = cosine_similarity_compare(uv['skill'], jd['new_yeucau'])
    # job benefit
    percent['job_benefit'] = cosine_similarity_compare(uv['job_benefit'], jd['new_tag'])
    # salary
    percent['salary'] = salary_compare(uv['salary'], jd['new_muc_luong'])

    return percent

def main(cv_path, ttuv, ttcvuvm, jd_path):
    # load data
    dataloader = DataLoader(cv_path, ttuv, ttcvuvm, jd_path)
    uv, jd = dataloader.load_data()
    percent = percent_mapping(uv, jd)

    res = sum([percent[key] * feature_weights[key] for key in percent.keys()])
    return int(round(res*100, 0))

if __name__ == '__main__':

    # load data
    with open(os.path.join(ROOT_DATADIR, 'cv.json'), 'r', encoding='utf-8') as f:
        cv = json.load(f)
    with open(os.path.join(ROOT_DATADIR, 'jd.txt'), 'r', encoding='utf-8') as f:
        jd = f.read()

    # get result
    res = percent_mapping(cv, jd)
    print(res)