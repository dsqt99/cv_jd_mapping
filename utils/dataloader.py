# import libraries
import os
import json
import requests

def load_api_phantichcv(cv_path):
    api_url = "https://api-cv.job3s.com/extract_feature"
    params = {
        "cv_path": cv_path
    }
    response = requests.post(api_url, params=params)

    if response.status_code == 200:
        data = response.json()
        data = data['data']['infos']
    else:
        data = None

    return data

def get_key_from_value(dict, value):
    return list(dict.keys())[list(dict.values()).index(value)]

class DataLoader:
    def __init__(self, cv_path=None, ttuv=None, ttcvuvm= None, jd_path=None):
        self.cv_path = cv_path
        self.ttuv = ttuv
        self.ttcvuvm = ttcvuvm
        self.jd_path = jd_path

    def load_data(self):
        uv, jd = {}, {}

        # load cv data
        with open(self.ttuv, 'r', encoding='utf-8') as f:
            ttuv = f.readlines()
        with open(self.ttcvuvm, 'r', encoding='utf-8') as f:
            ttcvuvm = f.readlines()
        
        cv = load_api_phantichcv(self.cv_path)

        # get data
        uv['gender'] = get_key_from_value(ttuv, cv['gender']) if cv['gender'] != '' else int(ttuv['use_gioi_tinh']) # gioi tinh
        uv['working_form'] = get_key_from_value(ttcvuvm, ttcvuvm['cv_loaihinh_id']) # hinh thuc lam viec
        uv['rank'] = cv['position'] # cap bac
        uv['main_career'] = ttcvuvm['cv_cate_id'] # nganh nghe chinh
        uv['sub_career'] = cv['work'] # nganh nghe phu
        



        # load jd data
        with open(self.jd_path, 'r', encoding='utf-8') as f:
            jd = f.readlines()

        return uv, jd