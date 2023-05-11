
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from dotenv import load_dotenv
from util import helper
import pandas as pd
import requests
import json
import os

class ReconmendationSys:

    def __init__(self):
        load_dotenv()
        self.model=helper.loadModel()   
        self.vector=helper.loadVector()   
        self.dataset=helper.readCSV()
    

    def collaborativeFilltering(self):
        pass

    def get_recommendation(self,top, df_all, scores):
        recommendation = pd.DataFrame(columns = ['id','name',  'description', 'score'])
        count = 0
        for i in top:
            recommendation.at[count, 'id'] = df_all['id'][i]
            recommendation.at[count, 'name'] = df_all['name'][i]
            recommendation.at[count, 'description'] = df_all['description'][i]
            recommendation.at[count, 'score'] =  scores[count]
            count += 1
        return recommendation
    
    def contentFiltering(self,visited_product):
        reconm=[]
        try:
            cleanDataset=helper.preprocess(pd.DataFrame(visited_product))  # id, text 
            cleanDataset['text'] = cleanDataset['text'].apply(helper.clean_txt)
            visited_product_vector= self.vector.transform((cleanDataset['text'])) 
            cos_similarity_tfidf = map(lambda x: cosine_similarity(visited_product_vector, x),self.model)
            output2 = list(cos_similarity_tfidf)
            top = sorted(range(len(output2)), key=lambda i: output2[i], reverse=True)[:10]
            list_scores = [output2[i][0][0] for i in top]
            results=self.get_recommendation(top,self.dataset, list_scores).iloc[1:5]
            for item in json.loads(results.to_json(orient='records')):
                reconm.append(json.loads(requests.get(f"{os.getenv('SERVER')}/products/{item['id']}").text)['product'])
            return reconm
        except Exception as e:
            print(f"contentFiltering :: {e}")
            return []



#  ---- Data should be in this format before send to model -----
# {
#     "id": ["6454eb23851766e7214c9d30"],
#     "name": ["Samsung Galaxy A12"],
#     "description": ["Samsung Galaxy A12, launched on November 24, 2020, is a budget-friendly and economical mobile phone by Samsung. The phone is powered by Mediatek Helio P35 processor and PowerVR GE8320 GPU. Moreover, it comes with 2 / 3 / 4 / 6 GB RAM and 32 / 64 / 128 GB storage memory.  Samsung Galaxy A12 boasts a 6.5-inch PLS IPS display with HD+, Infinity-V Display.  As regard cameras, Samsung Galaxy A12 comes with:  One (8 MP) camera on the front side and four (48 x 5 x 2 x 2 MP) cameras on the rear side. The front camera supports video recording up to 1080p at 30 fps. Whereas, the rear camera supports"],
#     "categories": ["Electronic Devices Mobile Phones Samsung"],"price":[""]
# }