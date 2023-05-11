from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk import word_tokenize
import pandas as pd
import requests
import string
import pickle
import nltk
import json
import csv
import os
import re

app_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..')).replace('\\', '/')
# print(app_root)
def getCategories():
    try:
        return json.loads(requests.get(f"{os.getenv('SERVER')}/category/fetch").text)['categoryList']
    except Exception as e:
        print(f"getCategories :: {e}")
        return []

def getProducts(slug):
    try:
        return json.loads(requests.get(f"{os.getenv('SERVER')}/product/{slug}").text)['products']
    except Exception as e:
        print(f"getProducts :: {e}")
        return []
    
def findAncestors(categoryList, categoryId):
    ancestors = []
    discardList = ['']
    currentList = categoryList
    key = categoryId
    iteration = 0

    while True:
        if len(currentList) == iteration:
            discardList.append(currentList[iteration - 1]["parentId"])
            currentList = categoryList
            iteration = 0
            continue
        
        if currentList[iteration]['_id'] in discardList:

            iteration += 1
            continue

        if currentList[iteration]["_id"] == key:
            ancestors.insert(0, currentList[iteration]["name"])

            if "parentId" in currentList[iteration]:
                key = currentList[iteration]["parentId"]
                currentList = categoryList
                iteration = 0
                continue
            else:
                break

        elif len(currentList[iteration]["children"]) == 0:
            iteration += 1
            continue

        else:
            currentList = currentList[iteration]["children"]
            iteration = 0
            continue

    return ancestors

def parseProducts(categories):
    if len(categories) ==0:
         return False
    products=[]
    discardList=[]
    iteration=0
    currCategory=categories

    while True:
        
        if len(currCategory) == iteration:
            if "parentId" in currCategory[iteration-1]:

                discardList.append(currCategory[iteration-1]["parentId"])
                iteration=0
                currCategory=categories
                continue
            
            else:
                return products

        if currCategory[iteration]["_id"] in discardList:
            
            iteration+=1
            continue

        
        if len(currCategory[iteration]["children"]) !=0:  # if Category have sub cateogry
            currCategory=currCategory[iteration]["children"]
            iteration=0
            continue
        else:
            rawProducts=getProducts(currCategory[iteration]["slug"])
            print(f"---- Categroy: {currCategory[iteration]['name']} -----")
            if len(rawProducts)!=0:
                for product in rawProducts:
                    products.append({
                "id":product["_id"],
                "name":product["name"],
                "price":product["price"],
                "description":product["description"],
                "categories":findAncestors(categories,product["category"])
                })
                    print(f"Product: {product['name']}")

            discardList.append(currCategory[iteration]["_id"])
            iteration+=1

def writeCSV(products):
    try:
        if len(products)>0:
            with open(f"{app_root}/{os.getenv('DATASET_PATH')}", mode='w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=["id", "name", "price", "description", "categories"])
                writer.writeheader()
                for product in products:
                    product['categories']=' '.join(product['categories'])
                    writer.writerow(product)
            return True
        return False
    except Exception as error:
        print(f"writeCSV :: {error}")
        return False
    
def readCSV():
    try:
        return pd.read_csv(f"{app_root}/{os.getenv('DATASET_PATH')}",encoding="ISO-8859-1")
    except Exception as error:
        print(f"readCSV :: {error}")
        return False

def preprocess(rawData):
    try:
        rawData['text']=rawData['name']+ " "+rawData['description']+" "+rawData['categories']
        rawData=rawData.drop(['name','description','categories','price'],axis=1)
        return rawData
    except Exception as error:
        print(f"preprocess :: {error}")
        return False
    
def saveModel(JSON):
    try:
        with open(f"{app_root}/{os.getenv('VECTOR_PATH')}", 'wb') as f:
            pickle.dump(JSON['vector'], f)
        with open(f"{app_root}/{os.getenv('MODEL_PATH')}", 'wb') as f:
            pickle.dump(JSON['model'], f)
        return True
    except Exception as error:
        print(f"saveModel :: {error}")
        return False
    
def black_txt(token):
    stop_words_ = set(stopwords.words('english'))
    return  token not in stop_words_ and token not in list(string.punctuation)  and len(token)>2   
    
def clean_txt(text):
    wn = WordNetLemmatizer()
    # stop = stopwords.words('english')
    clean_text = []
    clean_text2 = []
    text = re.sub("'", "",text)
    text=re.sub("(\\d|\\W)+"," ",text) 
    text = text.replace("nbsp", "")
    clean_text = [ wn.lemmatize(word, pos="v") for word in word_tokenize(text.lower()) if black_txt(word)]
    clean_text2 = [word for word in clean_text if black_txt(word)]
    return " ".join(clean_text2)

def downloadNLTK():
    try:
        nltk.data.find('tokenizers/punkt')
        nltk.data.find('corpora/stopwords')
        nltk.data.find('taggers/averaged_perceptron_tagger')
        nltk.data.find('corpora/wordnet')
    except:
        nltk.download('averaged_perceptron_tagger')
        nltk.download('punkt')
        nltk.download('stopwords')
        nltk.download('wordnet')

def loadVector():
    try:
        with open(f"{app_root}/{os.getenv('VECTOR_PATH')}", 'rb') as f:
            model = pickle.load(f)
            return model
    except Exception as error:
        print(f"loadVector :: {error}")
        return False
    
def loadModel():
    try:
        with open(f"{app_root}/{os.getenv('MODEL_PATH')}", 'rb') as f:
            model = pickle.load(f)
            return model
    except Exception as error:
        print(f"loadModel :: {error}")
        return False

# For debugging 
def debug():
    os.system("pause")
    