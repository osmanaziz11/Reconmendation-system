
from sklearn.metrics.pairwise import cosine_similarity
from util import helper
import pandas as pd

class ReconmendationSys:

    def __init__(self):
        self.vector=helper.loadVector()   # tf-idf Instance
        self.model=helper.loadModel()   # vector of dataset
        self.dataset=helper.readCSV()
    
    def collaborativeFilltering(self):
        pass

    def get_recommendation(top, df_all, scores):
        recommendation = pd.DataFrame(columns = ['name',  'description', 'score'])
        count = 0
        for i in top:
            recommendation.at[count, 'name'] = df_all['name'][i]
            recommendation.at[count, 'description'] = df_all['description'][i]
            recommendation.at[count, 'score'] =  scores[count]
            count += 1
        return recommendation
    
    def contentFiltering(self,visited_product):
        cleanDataset=helper.preprocess(visited_product)  # id, text 
        cleanDataset['text'] = cleanDataset['text'].apply(helper.clean_txt)
        visited_product_vector= self.vector.fit_transform((cleanDataset['text'])) 
        cos_similarity_tfidf = map(lambda x: cosine_similarity(visited_product_vector, x),self.model)
        output2 = list(cos_similarity_tfidf)
        top = sorted(range(len(output2)), key=lambda i: output2[i], reverse=True)[:10]
        list_scores = [output2[i][0][0] for i in top]
        results=self.get_recommendation(top,self.dataset, list_scores)
        return results



user_product=[{"id":"","name":"","description":"","categories":""}]
