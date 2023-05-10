# Module :: system update
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.corpus import stopwords
from dotenv import load_dotenv
from nltk import word_tokenize
from util import helper
import string
import nltk
import re

class System:
    def __init__(self):
        self.stop_words_ = set(stopwords.words('english'))
        nltk.download('averaged_perceptron_tagger')
        self.tfidf_vectorizer = TfidfVectorizer()
        self.stop = stopwords.words('english')
        self.wn = WordNetLemmatizer()
        nltk.download('punkt')
        nltk.download('stopwords')
        nltk.download('wordnet')
        load_dotenv() 
    
    def black_txt(self,token):
        return  token not in self.stop_words_ and token not in list(string.punctuation)  and len(token)>2   
    
    def clean_txt(self,text):
        clean_text = []
        clean_text2 = []
        text = re.sub("'", "",text)
        text=re.sub("(\\d|\\W)+"," ",text) 
        text = text.replace("nbsp", "")
        clean_text = [ self.wn.lemmatize(word, pos="v") for word in word_tokenize(text.lower()) if self.black_txt(word)]
        clean_text2 = [word for word in clean_text if self.black_txt(word)]
        return " ".join(clean_text2)
    
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
            cleanDataset['text'] = cleanDataset['text'].apply(self.clean_txt)
            self.tfidf_vector= self.tfidf_vectorizer.fit_transform((cleanDataset['text'])) 
            return {'status':1,'message':'System update successfully.'} if helper.saveModel({'vector':self.tfidf_vectorizer,'model':self.tfidf_vector}) else {'status':0,'message':'System update failed without any exception.'}
        except Exception as error:
            return {'status':0,'message':f'System update failed with exception! Error: {error}'}

    def update(self):
        return self.Train() if self.retrieveData() else {'status':0,'message':f'System update failed, Issue in retreiving Data.'}
        