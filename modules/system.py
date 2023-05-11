# Module :: system update
from sklearn.feature_extraction.text import TfidfVectorizer
from dotenv import load_dotenv
from util import helper
import os

class System:
    def __init__(self):
        self.tfidf_vectorizer = TfidfVectorizer()
        helper.downloadNLTK()
        load_dotenv() 
    
    def retrieveData(self):
        try:
            categories = helper.getCategories()   # categories
            products=helper.parseProducts(categories)  # products
            writeCSV=helper.writeCSV(products)   # JSON to CSV
            return  True if writeCSV else False
        except Exception as error:
            return False

    def Train(self):
        try:
            rawDataset=helper.readCSV() 
            cleanDataset=helper.preprocess(rawDataset)
            cleanDataset['text'] = cleanDataset['text'].apply(helper.clean_txt)
            self.tfidf_vector= self.tfidf_vectorizer.fit_transform((cleanDataset['text'])) 
            return {'status':1,'message':'System update successfully.'} if helper.saveModel({'vector':self.tfidf_vectorizer,'model':self.tfidf_vector}) else {'status':0,'message':'System update failed without any exception.'}
        except Exception as error:
            return {'status':0,'message':f'System update failed with exception! Error: {error}'}

    def Update(self):
        return self.Train() if self.retrieveData() else {'status':0,'message':f'System update failed, Issue in retreiving Data.'}
        
